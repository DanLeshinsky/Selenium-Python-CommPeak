import hashlib
import os
import requests


def get_md5_checksum(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def download_file(url, dest_folder, file_name):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    file_path = os.path.join(dest_folder, file_name)

    with requests.get(url, stream=True) as rqst:
        rqst.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in rqst.iter_content(chunk_size=1024):
                f.write(chunk)
    return file_path