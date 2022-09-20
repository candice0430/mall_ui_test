from utils.file_handle import FileHandle
# import pytest
import yaml

def get_data(yaml_file_name):
    try:
        data_file_path = FileHandle.absolute_path('data',yaml_file_name)
        f = open(data_file_path,'r')
        yaml_data = yaml.safe_load(f)
        # yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        print("ex:",str(ex))
        # pytest.skip("parse error....")
    else:
        return yaml_data