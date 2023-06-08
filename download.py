import requests

def download_public_file(url, destination):
    response = requests.get(url)
    response.raise_for_status()
    with open(destination, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded to {destination}.")

url = "https://storage.googleapis.com/cloud-samples-data/bigquery/sample-transactions/transactions.csv"
destination = "transactions.csv"

download_public_file(url, destination)
