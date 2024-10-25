import pandas as pd
import os
from dotenv import load_dotenv
import json
import time
from download_snapshot import download_snapshot
from trigger_data_collection import trigger_data_collection_api

load_dotenv()


def get_urls_from_csv(file):
    df = pd.read_csv(file)
    job_urls = [{"url": url} for url in df["Job Url"]]
    return job_urls


def trigger_linkedin_jobs_collection(data):
    api_key = os.getenv("BRIGHT_DATA_API_KEY")
    dataset_id = os.getenv("BRIGHT_DATA_LINKEDIN_JOBS_DATASET")
    response = trigger_data_collection_api(dataset_id, data, api_key)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        snapshot_id = data["snapshot_id"]
        return snapshot_id


def download_snapshot_into_json(snapshot_id, download_loc):
    api_key = os.getenv("BRIGHT_DATA_API_KEY")
    response = download_snapshot(api_key, snapshot_id)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        with open(download_loc, "w") as f:
            json.dump(data, f)


def main():
    date = time.strftime("%Y%m%d")
    FILENAME = "../path/to/your/file.csv"
    input_data = get_urls_from_csv(FILENAME)
    snapshot_id = trigger_data_collection_api(input_data)
    print(snapshot_id)

    download_snapshot_into_json(
        snapshot_id=snapshot_id,
        download_loc=f"../data/{date}/{snapshot_id}_linkedin_jobs.json",
    )


if __name__ == "__main__":
    main()
