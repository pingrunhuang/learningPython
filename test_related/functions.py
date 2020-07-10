import os
import requests
import pandas as pd


class RemovalService:
    # in this case, path.isfile and remove should be mocked
    def rm(self, path):
        res = os.path.isfile(path)
        if res:
            os.remove(path)



def http_get_data():
    r = requests.get('localhost:8080/endpoint1')
    if r.status_code == 200:
        return r.json()
    return None



def get_df1(conn):
    df = pd.read_sql("", conn)
    return df.rename(columns={'foo_id':'bar_id'})


def get_df2(path):
    with open(path) as fp:
        df = pd.read_excel(fp, sheet_name=0)
    return df.rename(columns={'foo_id':'bar_id'})

