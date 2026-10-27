# [Project title]

**Author:** [Your name]
**Course:** [Course name, semester, university]
**Language:** Python (Jupyter)

---

## Setup checklist (delete this section when done)

- [ ] Fill in the title, your name and the course above.
- [ ] Create a virtual environment in the project folder and install the packages:
      `python -m venv .venv`, activate it (`source .venv/bin/activate` on macOS/Linux, `.venv\Scripts\activate` on Windows), then `pip install -r requirements.txt`.
- [ ] Whenever you install a new package, record the exact versions with `pip freeze > requirements.txt`.
- [ ] Put your raw data file into `data/` (as `data.csv`, or change `DATA_PATH` in the notebooks) and any documentation into `data/data_documentation/`.
- [ ] Fill in `data/data_documentation/codebook.md` for the variables you plan to use.
- [ ] Log your first judgment call in `judgment_calls.md`.
- [ ] Commit and push.

---

## Research question

> [Your research question: what you want to learn or predict, about which units, and what "new data" means for the answer.]

[What would the answer be used for, and by whom?]

## Data

- `data/data.csv`: [Where does the data come from? Who collected it, when and how? How many rows and columns? What is one row?]
- `data/data_documentation/`: [List each documentation file and what it contains.]
- **Test set:** [How is the test set defined, and who holds it? It is used only once, at the end, after the final model is committed and tagged `final-model`.]

## How to rerun this analysis

1. Clone this repository.
2. Create a virtual environment and install the recorded package versions:
   `python -m venv .venv`, activate it, then `pip install -r requirements.txt`.
3. Check that the raw data file is in `data/`.
4. Run the notebooks in `dslc_documentation/` in numeric order, each with "Restart kernel and run all cells":
   `01_cleaning.ipynb`, `02_eda.ipynb`, `03_clustering.ipynb`, `04_prediction.ipynb`.

[Anything else a reviewer needs to know: Python version, approximate run time, random seeds, known issues.]

## Folder structure

```
dslc-project/
├── README.md                this file
├── judgment_calls.md        log of every judgment call
├── requirements.txt         package versions (pip freeze)
├── data/
│   ├── data.csv             raw data, never edited
│   └── data_documentation/
│       └── codebook.md      what each variable means
└── dslc_documentation/
    ├── 01_cleaning.ipynb    background, data split, cleaning
    ├── 02_eda.ipynb         exploratory data analysis
    ├── 03_clustering.ipynb  dimensionality reduction and clustering
    ├── 04_prediction.ipynb  prediction and stability analysis
    └── functions/
        ├── __init__.py
        ├── split_data.py
        ├── clean_data.py
        └── preprocess_data.py
```

Not every project needs every stage. Delete or rename notebooks that don't fit your question, and keep the numbers in reading order.

## Main findings

[Fill in at the end: the answer to the research question in a few sentences, how predictable it is, and how stable it is under the perturbations you tried.]
