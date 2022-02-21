from mark.utils.utils import newdir
from mark.config import config


def write_html(code: str, filename: str):
    """
        Writes code to html file.
    """
    dist = config.OUTPUT_DIRECTORY
    newdir(f"{dist}")
    with open(f"{dist}/{filename}", "w") as f:
        f.write(f"<!DOCTYPE html>\n<!--- {config.PACKAGE_COMMENT} --->\n{code}"
                )  # noqa