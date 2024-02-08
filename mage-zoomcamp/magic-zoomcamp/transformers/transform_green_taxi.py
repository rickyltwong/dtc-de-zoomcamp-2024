import pandas as pd
import re
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.date
    def camel_to_snake(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    data.columns = [camel_to_snake(column) for column in data.columns]

    print(data['lpep_pickup_date'].unique())
    
    # Assertions
    assert data['vendor_id'].isin(data['vendor_id'].unique()).all(), "vendor_id contains invalid values"
    assert (data['passenger_count'] > 0).all(), "passenger_count contains non-positive values"
    assert (data['trip_distance'] > 0).all(), "trip_distance contains non-positive values"

    return data


    # return data


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
