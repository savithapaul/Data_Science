from azure.storage.blob import BlobServiceClient
import pandas as pd 

# Initialize connection to Azure Blob Storage
connect_str = "DefaultEndpointsProtocol=https;AccountName=dedupe;AccountKey=XXXXXXXXXXXXXXX"
container_name = "dedupe-container"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)

# List blobs in the container
blob_list = container_client.list_blobs()

# Read blob data into a DataFrame
blobs = []
for blob in blob_list:
    blob_client = container_client.get_blob_client(blob)
    blob_data = blob_client.download_blob().readall()
    blobs.append({
        'file_id': blob.name,
        'content': blob_data.decode('utf-8')  # Adjust decoding based on your data type
    })

df = pd.DataFrame(blobs)
