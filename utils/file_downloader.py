import os
import uuid
from urllib.parse import urlparse
import requests

class FileDownloader:
    @staticmethod
    def download_file(url):
        response = requests.get(url)
        response.raise_for_status()
        parsed_url = urlparse(url)
        root, extension = os.path.splitext(parsed_url.path)
        unique_name = str(uuid.uuid4())
        
        media_dir = "./media"
        os.makedirs(media_dir, exist_ok=True)

        file_path = os.path.join(media_dir, unique_name + extension)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return file_path