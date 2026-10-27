# Data

Put the raw data file here, as `data.csv` or under its original name (then change `DATA_PATH` in the notebooks).

- **Never edit the raw file.** All cleaning happens in code, so that every change is documented and can be rerun.
- Prefer plain formats such as CSV or JSON over Excel files.
- Put the documentation you received or found (codebooks, survey descriptions, papers) into `data_documentation/`, and summarise the variables you use in `data_documentation/codebook.md`.
- If a test set is held back, keep it out of this folder until your final model is committed and tagged `final-model`.
