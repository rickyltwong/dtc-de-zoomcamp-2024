from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from google.cloud import storage
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    """
    Load data from a Google Cloud Storage bucket and count the number of folders.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'mage-zoomcamp-ricky-wong'
    project_id = 'true-shore-412221'
    table_name = "green_cab_data"

    root_path = f'{bucket_name}/{table_name}'

    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    folders = set()

    # List blobs in the specified bucket and path
    blobs = client.list_blobs(bucket_name, prefix=root_path, delimiter='/')

    for blob in blobs:
        # Extract the folder name from the blob's name
        folder_path = "/".join(blob.name.split('/')[:-1])
        if folder_path and folder_path not in folders:
            folders.add(folder_path)

    folder_count = len(folders)
    print(f"Number of folders under '{root_path}': {folder_count}")

    return folder_count


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
