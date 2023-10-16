from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "PlantDoc"
PROJECT_NAME_FULL: str = "PlantDoc: A Dataset for Visual Plant Disease Detection"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0(source_url="https://github.com/pratikkayal/PlantDoc-Object-Detection-Dataset/blob/master/LICENSE.txt")
APPLICATIONS: List[Union[Industry, Research, Domain]] = [Research.Agricultural()]
CATEGORY: Category = Category.Agriculture()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2019-10-16"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://github.com/pratikkayal/PlantDoc-Object-Detection-Dataset"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1651674
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/PlantDoc"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://github.com/pratikkayal/PlantDoc-Object-Detection-Dataset/archive/refs/heads/master.zip"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "Potato leaf": [230, 25, 75],
    "Cherry leaf": [60, 180, 75],
    "Tomato two spotted spider mites leaf": [255, 225, 25],
    "grape leaf black rot": [0, 130, 200],
    "Bell_pepper leaf": [245, 130, 48],
    "Raspberry leaf": [145, 30, 180],
    "Tomato mold leaf": [70, 240, 240],
    "Tomato leaf": [240, 50, 230],
    "Corn rust leaf": [210, 245, 60],
    "Bell_pepper leaf spot": [250, 190, 212],
    "grape leaf": [0, 128, 128],
    "Apple leaf": [220, 190, 255],
    "Squash Powdery mildew leaf": [170, 110, 40],
    "Peach leaf": [255, 250, 200],
    "Potato leaf early blight": [128, 0, 0],
    "Tomato leaf bacterial spot": [170, 255, 195],
    "Potato leaf late blight": [128, 128, 0],
    "Blueberry leaf": [255, 215, 180],
    "Corn leaf blight": [0, 0, 128],
    "Tomato leaf mosaic virus": [128, 128, 128],
    "Corn Gray leaf spot": [208, 2, 27],
    "Apple rust leaf": [245, 166, 35],
    "Tomato Septoria leaf spot": [248, 231, 28],
    "Apple Scab Leaf": [139, 87, 42],
    "Soyabean leaf": [126, 211, 33],
    "Tomato leaf late blight": [65, 117, 5],
    "Tomato Early blight leaf": [189, 16, 224],
    "Strawberry leaf": [74, 144, 226],
    "Tomato leaf yellow virus": [80, 227, 194],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://arxiv.org/abs/1911.10317"
CITATION_URL: Optional[
    str
] = "https://github.com/pratikkayal/PlantDoc-Object-Detection-Dataset#bibtex"
AUTHORS: Optional[List[str]] = [
    "Singh, Davinder",
    "Jain, Naman",
    "Jain, Pranjali",
    "Kayal, Pratik",
    "Kumawat, Sudhakar",
    "Batra, Nipun",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Indian Institute of Technology Gandhinagar"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://iitgn.ac.in/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
