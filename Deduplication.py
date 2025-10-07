
for cluster in df['cluster'].unique():
    if cluster != -1:
        duplicates = df[df['cluster'] == cluster]
        for index, row in duplicates.iterrows():
            if index != duplicates.index[0]:
                blob_client = container_client.get_blob_client(row['file_id'])
                blob_client.delete_blob()

print("Deduplication complete.")
