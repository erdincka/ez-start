import os
import logging
import sys

from minio import Minio

import common

logger = logging.getLogger(__name__)
# logger.setLevel(logging.WARNING)


def get_client(endpoint: str, access_key: str, secret_key: str):
    """
    Get Minio client
    """
    return Minio(
        endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=True,
        cert_check=False
    )


def upload_to_s3(endpoint: str, access_key: str, secret_key: str, bucket: str, file: str):
    """
    Upload the file to the external S3 bucket

    """

    try:
        client = get_client(endpoint, access_key, secret_key)
        # Make the bucket if it doesn't exist.
        found = client.bucket_exists(bucket)
        if not found:
            client.make_bucket(bucket)
            logger.info("Created bucket %s", bucket)
        else:
            logger.info("Bucket %s already exists", bucket)

        # Upload the file, renaming it in the process
        return client.fput_object(
            bucket,
            os.path.basename(file),
            file,
        )

    except Exception as error:
        logger.warning(error)
        return None


def download_from_s3(endpoint: str, access_key: str, secret_key: str, bucket: str, obj: str):
    """
    Get the file from the S3
    """

    client = get_client(endpoint, access_key, secret_key)

    try:
        result = client.fget_object(bucket, os.path.basename(obj), obj)
        return result

    except Exception as error:
        logger.error(error)
        return None


if __name__ == "__main__":
    ep = "vm25.kayalab.uk:9000"
    ak = "5FLXTS1LV8UDC8TCGHOLRDXJUSRIGU6AOIRUJJ7FHNK6ZQBB1JP14RBQYHEUUCY8U8STOR7YAVN4D2PRBAKN1VUJQ5GAHQDNR8E0G6H9CBGDTSQ1AQ50"
    sk = "47O67YR0ZJKKKAEUUM48U1VAQ14Z3TAXAX6AEROJ4C3R01KGJ77X9AUI13UL8TAVN4G6UQU8X76THO62AT4L85DA0QQGO2AN230D1CT10HLI3H0PZUS"
    bk = "demobct"

    if len(sys.argv) == 2:
        if sys.argv[1] == 'upload':
            for file in os.listdir('data'):
                result = upload_to_s3(ep, ak, sk, bk, f"./data/{file}")
                if result is not None:
                    print(result.object_name)

        elif sys.argv[1] == 'download':
            result = download_from_s3(ep, ak, sk, bk,'Training_set_ccpp.csv')
            if result:
                print(result)

        else: print("Don't know how to do anything but upload|download")


    else:
        print(f'Usage: python3 {sys.argv[0]} upload|download')