from src.lib.utils import newdir
from src import config


def write_html(code: str, filename: str):
    """
        Writes code to html file.
    """
    dist = config.OUTPUT_DIRECTORY
    newdir(f"{dist}")
    with open(f"{dist}/{filename}", "w") as f:
        f.write(code)
