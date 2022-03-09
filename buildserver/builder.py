import boto3

import buildserver.mock


S3_ASSET_BUCKET = "energyhub-assets"


@buildserver.mock.mockAWS()
def list_assets():
    s3 = boto3.client("s3")
    output = s3.list_objects_v2(
        Bucket=S3_ASSET_BUCKET,
    )
    return output


@buildserver.mock.mockAWS()
def get_asset(build):
    return build
