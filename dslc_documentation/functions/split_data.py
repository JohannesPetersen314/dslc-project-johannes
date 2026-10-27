"""Split the data into training, validation and test sets.

Use this function in every notebook, so that all notebooks work with the
same split. The split should mimic how future data relates to the data you
have: later in time (time-based split), new groups such as hospitals or
households (group-based split), or exchangeable observations (random split).
Justify the split in 01_cleaning.ipynb and log it in judgment_calls.md.
"""


def split_data(data, seed=1234):
    """Return a tuple (data_train, data_val, data_test).

    If a test set is held back for you, return only (data_train, data_val).
    """
    # TODO: write your split here, using `seed` for every random step,
    # then delete the line below
    raise NotImplementedError("split_data() is not written yet")

    return data_train, data_val, data_test
