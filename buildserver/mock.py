import contextlib

import moto
import boto3

import buildserver.builder


class mockAWS(contextlib.ContextDecorator):
    mock_s3 = moto.mock_s3()

    def __enter__(self):
        self.mock_s3.start()
        s3 = boto3.client("s3")

        # create bucket
        s3.create_bucket(
            Bucket=buildserver.builder.S3_ASSET_BUCKET,
        )

        # create assets
        for build, image in [
            (
                "ci-main-3230",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:322",
            ),
            (
                "ci-main-3231",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:323",
            ),
            (
                "ci-main-3233",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:324",
            ),
            (
                "ci-main-3234",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:325",
            ),
            (
                "ci-main-3582",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:326",
            ),
            (
                "ci-main-3590",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:327",
            ),
            (
                "ci-main-3620",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:328",
            ),
            (
                "ci-devspike-3028",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:329",
            ),
            (
                "ci-devspike-3029",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:332",
            ),
            (
                "ci-devspike-3030",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:333",
            ),
            (
                "ci-devspike-3031",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:334",
            ),
            (
                "local-devspike-3031",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:335",
            ),
            (
                "local-devspike-3032",
                b"asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:336",
            ),
        ]:
            s3.put_object(
                Bucket=buildserver.builder.S3_ASSET_BUCKET,
                Key=build,
                Body=image,
            )
        return self

    def __exit__(self, *exc):
        self.mock_s3.stop()
