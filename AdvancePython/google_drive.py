from contextlib import contextmanager
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import hashlib

@contextmanager
def retry_strategy():
    retry = Retry(
        total=5,
        status_forcelist=[413, 429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        yield session
    finally:
        session.close()

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768
        md5hash = hashlib.md5()

        with open(destination, "wb") as f:
            if response.status_code != 416:
                try:
                    response.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    raise Exception(e)

                for chunk in response.iter_content(CHUNK_SIZE):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        md5hash.update(chunk)
        
        return md5hash

    URL = "https://drive.google.com/uc?export=download"

    with retry_strategy() as session:
        response = session.get(URL, params = { 'id' : id }, stream = True)
        token = get_confirm_token(response)

        if token:
            params = { 'id' : id, 'confirm' : token }
            response.close()
            response = session.get(URL, params = params, stream = True)

    md5hash = save_response_content(response, destination)
    print(md5hash.hexdigest())    


if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        print("Usage: python google_drive.py drive_file_id destination_file_path")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        download_file_from_google_drive(file_id, destination)