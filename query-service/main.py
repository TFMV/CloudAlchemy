from fastapi import FastAPI, HTTPException
from google.cloud import storage
import duckdb
import pandas as pd
from io import BytesIO
import logging

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)

@app.get("/query")
async def query_parquet_file(bucket: str, file: str, query: str):
    try:
        logging.debug("Initializing Google Cloud Storage client")
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket)
        blob = bucket.blob(file)
        
        logging.debug("Reading Parquet file from GCS")
        data = blob.download_as_bytes()
        parquet_file = BytesIO(data)
        
        logging.debug("Loading Parquet file into DuckDB")
        conn = duckdb.connect(database=':memory:')
        df = pd.read_parquet(parquet_file)
        conn.register('df', df)
        
        logging.debug("Executing the query")
        result_df = conn.execute(query).fetchdf()
        
        logging.debug("Converting result to dictionary")
        result = result_df.to_dict(orient='records')
        return result
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        raise HTTPException(status_code=500, detail=str(e))
