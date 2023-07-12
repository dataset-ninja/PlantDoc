Dataset **PlantDoc** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/P/d/HN/jRsYPbc7dqMuYYFYSFbJrZmSD3GcIXI1UHDLVBxp3616gYhb0uRtobr1nBZQyoFdg8F6TrbPqsHEJZwLRZyUitmC28nPNPI05zXp1BTtWp3up6q30oJXUmvikhcE.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PlantDoc', dst_path='~/dtools/datasets/PlantDoc.tar')
```
The data in original format can be 🔗[downloaded here](https://github.com/pratikkayal/PlantDoc-Object-Detection-Dataset/archive/refs/heads/master.zip)