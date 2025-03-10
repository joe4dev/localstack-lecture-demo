import pytest
import boto3

@pytest.fixture
def s3_client(mocker):
    def mock_api_call(self, operation_name, kwarg):
        if operation_name == "ListBuckets":
            return {"Buckets": [{"Name": "test123"}]}
    
    mocker.patch("botocore.client.BaseClient._make_api_call", new=mock_api_call)
    return boto3.client("s3")

def test_s3(s3_client):
    result = s3_client.list_buckets()["Buckets"]
    assert result == [{"Name": "test123"}]
