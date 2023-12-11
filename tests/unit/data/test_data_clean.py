from new_model.data.data_clean import clean_data
from new_model.data.data_clean import fill_missing_data


def test_clean_data(dataset):
    """Test clean_data function"""

    data = dataset[1]
    expected_data = data

    cleaned_data_set = clean_data(data)

    assert cleaned_data_set.equals(expected_data)


def test_fill_missing_data(dataset):
    """Test clean_data function"""

    data = dataset[1]

    expected_data = data

    cleaned_data_set = fill_missing_data(data)

    assert cleaned_data_set.equals(expected_data)
