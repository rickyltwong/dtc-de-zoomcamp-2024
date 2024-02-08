from io import BytesIO
import pandas as pd
import gzip
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs) -> pd.DataFrame:
    df_list: List[pd.DataFrame] = []
    
    for i in range(10, 13):
        url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{i:02d}.csv.gz"
        response = requests.get(url)
        
        if response.status_code == 200:
            # Read the content of the response into a Pandas DataFrame
            with BytesIO(response.content) as data:
                df_month = pd.read_csv(data, compression='gzip', header=0, sep=',', quotechar='"')
                df_list.append(df_month)
        else:
            print(f"Failed to download data for month {i}: HTTP {response.status_code}")

    # Concatenate all monthly data into a single DataFrame
    df = pd.concat(df_list, ignore_index=True)
    
    # Additional processing (datatypes, date parsing, etc.) can be added here

    return df


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
