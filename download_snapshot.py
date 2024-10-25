import requests
import json
import os
from dotenv import load_dotenv


def download_snapshot(api_key, snapshot_id):
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    params = {
        "format": "json",
    }
    response = requests.get(
        f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}",
        params=params,
        headers=headers,
    )
    return response


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("BRIGHT_DATA_API_KEY")
    snapshot_id = input("Snapshot ID: ")
    response = download_snapshot(api_key, snapshot_id)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        with open("../data/api_output.json", "w") as f:
            json.dump(data, f)