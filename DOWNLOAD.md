Dataset **PlantDOC** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/L/B/QS/8daoOWs7dLylqA01eaTYFSkub2cfN1SivmgfWulpNhnomxV9OZuQkdZDiPMzv2FP4XMijk4X3mr57sbE65qvt4i4FXM1HkdD6AHmHDB7UPuuLy2XUOa8lPOgfYgp.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PlantDOC', dst_path='~/dtools/datasets/PlantDOC.tar')
```
The data in original format can be 🔗[downloaded here](https://github.com/pratikkayal/PlantDoc-Object-Detection-Dataset/archive/refs/heads/master.zip)