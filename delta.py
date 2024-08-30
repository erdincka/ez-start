import logging
import os
import sys

import pandas as pd
from deltalake import DeltaTable, write_deltalake

import common

logger = logging.getLogger(__name__)


def upsert_to_delta(table_path: str, records: pd.DataFrame):
    """
    Write list of dicts into Delta Lake table
    """

    try:
        table_uri = f"/mapr/{os.environ['MAPR_CLUSTER']}{table_path}"

        df = pd.DataFrame().from_records(records)

        write_deltalake(table_or_uri=table_uri, data=df, mode="append", schema_mode="merge")
        logger.info("Loaded to table in %s", table_uri)

    except Exception as error:
        logger.error("Failed to write: %s", table_path)
        logger.error(error)
        return False

    return True


def get_from_delta(table_path, query: str = None):
    """
    Returns all records from the binary table as DataFrame
    """

    fullpath = f"/mapr/{os.environ['MAPR_CLUSTER']}{table_path}"

    if not os.path.exists(fullpath):
        logger.warning("%s not created yet", fullpath)
        return pd.DataFrame()

    try:
        if query is None or query == "":
            return DeltaTable(fullpath).to_pandas()
        else:
            fraud = "fraud" # for query string
            return DeltaTable(fullpath).to_pandas().query(query)

    except Exception as error:
        logger.error("Failed to read: %s", fullpath)
        logger.error(error)
        return pd.DataFrame()


if __name__ == "__main__":
    table_path = "/apps/deltatable1"

    if len(sys.argv) == 2:
        if sys.argv[1] == 'upsert':
            data = pd.read_csv("./data/Training_set_ccpp.csv")
            result = upsert_to_delta(table_path, data)
            if result is not None:
                print(result)

        elif sys.argv[1] == 'read':
            result = get_from_delta(table_path)
            print(result)

        else: print("Don't know how to do anything but upsert|read")

    else:
        print(f'Usage: python3 {sys.argv[0]} upsert|read')
