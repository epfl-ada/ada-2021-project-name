# ada-2021-project-name

## Data download, filtering, and transformation
For end-to-end data preprocessing, run the following command:
```bash
bash download.sh
```
It consists of four main steps:
* Downloading the archived data from `zenodo` and unzipping archives
* Transformation of the data and selecting the quotes relevant to `bitcoin`, `crypto`, and related topics with `preprocess.py`.
* Merging data with `WikiData` with `merge.py`.
* Collecting vocabularies to match `WikiData` ids to human-readable entities with `build_vocab.py`.