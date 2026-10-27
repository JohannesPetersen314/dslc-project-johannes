"""Pre-process the cleaned data for a specific algorithm.

Cleaning makes the data reflect reality as closely as possible;
pre-processing adapts it to what an algorithm needs (for example scaling,
dummy variables or imputation). As in clean_data(), every judgment call is
an argument with a default value. Log each argument in judgment_calls.md.
"""


def preprocess_data(data_clean):
    """Return a pre-processed copy of the cleaned data."""
    data_preprocessed = data_clean.copy()

    # TODO: add your pre-processing steps here, with a comment explaining why

    return data_preprocessed
