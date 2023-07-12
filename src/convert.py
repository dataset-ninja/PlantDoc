# https://github.com/pratikkayal/PlantDoc-Object-Detection-Dataset

import csv
import os
from collections import defaultdict

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_name,
    get_file_name_with_ext,
)

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


project_name = "Plant Disease Detection"
dataset_path = "./APP_DATA"
batch_size = 30

train_anns_file_name = "train_labels.csv"
test_anns_file_name = "test_labels.csv"
train_data_folder = "TRAIN"
test_data_folder = "TEST"
ds_name_to_images = {"train": train_data_folder, "test": test_data_folder}


def create_ann(image_path, image_name_to_data):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    image_name = get_file_name_with_ext(image_path)
    curr_bboxes_class_data = image_name_to_data[image_name]
    for data in curr_bboxes_class_data:
        obj_class = data[1]
        bbox = list(map(int, data[0]))
        rect = sly.Rectangle(top=bbox[1], left=bbox[0], bottom=bbox[3], right=bbox[2])
        curr_label = sly.Label(rect, obj_class)
        labels.append(curr_label)

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta()

    class_name_to_obj_class = {}

    for file_name in [test_anns_file_name, train_anns_file_name]:
        ds_name = file_name.split("_")[0]
        images_folder_name = ds_name_to_images[ds_name]
        images_path = os.path.join(dataset_path, images_folder_name)
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        image_name_to_data = defaultdict(list)

        ann_csv_path = os.path.join(dataset_path, file_name)
        with open(ann_csv_path, "r") as file:
            csvreader = csv.reader(file)
            for idx, row in enumerate(csvreader):
                if idx == 0:
                    continue
                if row[3] not in list(class_name_to_obj_class.keys()):
                    new_obj_class = sly.ObjClass(row[3], sly.Rectangle)
                    class_name_to_obj_class[row[3]] = new_obj_class
                    meta = meta.add_obj_class(new_obj_class)

                curr_image_path = os.path.join(images_path, row[0])
                if file_exists(curr_image_path):
                    image_name_to_data[row[0]].append((row[4:], class_name_to_obj_class[row[3]]))

        api.project.update_meta(project.id, meta.to_json())

        images_names = list(image_name_to_data.keys())

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            img_pathes_batch = [os.path.join(images_path, im_name) for im_name in img_names_batch]
            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path, image_name_to_data) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))

    return project
