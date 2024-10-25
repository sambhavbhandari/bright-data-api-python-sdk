import requests
import os
from dotenv import load_dotenv


def trigger_data_collection_api(dataset_id, data, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    params = {
        "dataset_id": dataset_id,
    }

    response = requests.post(
        "https://api.brightdata.com/datasets/v3/trigger",
        params=params,
        headers=headers,
        json=data,
    )

    return response

def main():
    load_dotenv()
    api_key = os.getenv("BRIGHT_DATA_API_KEY")
    dataset_id = os.getenv("BRIGHT_DATA_DATASET_ID")

    input_data = [
        {"url": "https://www.linkedin.com/in/ryanroslansky/"},
    ]

    response = trigger_data_collection_api(dataset_id, input_data, api_key)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        snapshot_id = data["snapshot_id"]
        print(f"Snapshot ID: {snapshot_id}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()
