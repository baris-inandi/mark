from mark.config import config
from os import makedirs, path


def write_html(code: str, filename: str):
    """
        Writes code to html file.
    """
    makedirs(path.basename(config.user["outputFile"]), exist_ok=True)
    with open(config.user["outputFile"], "w") as f:
        f.write(f"<!DOCTYPE html>\n<!--- {config.PACKAGE_COMMENT} --->\n{code}"
                )  # noqa
