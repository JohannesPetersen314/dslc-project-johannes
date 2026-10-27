"""Clean the raw data.

Raw data in, clean data out. Every judgment call is an argument with a
default value, so that alternative cleaned datasets for the stability
analysis are one function call away, for example:

    clean_data(data_raw, some_choice="alternative")

Log each argument in judgment_calls.md.
"""


def clean_data(data_raw):
    """Return a cleaned copy of the raw data."""
    data_clean = data_raw.copy()

    # TODO: add your cleaning steps here, with a comment explaining why

    return data_clean
