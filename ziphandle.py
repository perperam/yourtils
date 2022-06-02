import requests
import shutil
from pathlib import Path

def load_zip_url(url, filename="download", timeout=None):
    filename = filename.replace(".zip", "")
    r"""
    download a zip file that is behind a given url to a zip file named filename
    """
    try:
        r = requests.get(url, allow_redirects=False, timeout=timeout)
    except requests.exceptions.Timeout as err:
        print(err)

    with open(f"{filename}.zip", "wb") as file:
        file.write(r.content)

def upack_zip(zipfile, outputdir):
    shutil.unpack_archive(zipfile, outputdir, "zip")


def pack_zip(inputdir):
    path = Path(inputdir)
    zipfile = inputdir.parent / (inputdir.name + ".zip")

    shutil.make_archive(zipfile, "zip", path.as_posix())
