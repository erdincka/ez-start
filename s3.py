import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def upload_to_s3(endpoint: str, access_key: str, secret_key: str, bucket: str, file: str):
    """
    Upload the file to the external S3 bucket

    """

    from minio import Minio

    try:
        client = Minio(
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=True,
            # cert_check=False
        )

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


if __name__ == "__main__":
    ak = "5FLXTS1LV8UDC8TCGHOLRDXJUSRIGU6AOIRUJJ7FHNK6ZQBB1JP14RBQYHEUUCY8U8STOR7YAVN4D2PRBAKN1VUJQ5GAHQDNR8E0G6H9CBGDTSQ1AQ50"
    sk = "47O67YR0ZJKKKAEUUM48U1VAQ14Z3TAXAX6AEROJ4C3R01KGJ77X9AUI13UL8TAVN4G6UQU8X76THO62AT4L85DA0QQGO2AN230D1CT10HLI3H0PZUS"
    bk = "demobct"

    for file in os.listdir('data'):
        result = upload_to_s3(f"vm25.kayalab.uk:9000", ak, sk, bk, f"./data/{file}")
        if result is not None:
            print(result.object_name)
