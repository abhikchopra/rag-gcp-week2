from google.cloud import storage
import os


def download_pdfs(bucket_name, local_dir="temp_pdfs"):

    os.makedirs(local_dir, exist_ok=True)

    client = storage.Client()

    bucket = client.bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:

        if blob.name.endswith(".pdf"):

            local_path = os.path.join(
                local_dir,
                os.path.basename(blob.name)
            )

            blob.download_to_filename(local_path)

    return local_dir