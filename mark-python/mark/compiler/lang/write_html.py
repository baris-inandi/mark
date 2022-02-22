from mark.utils.utils import newdir
from mark.config import config


def write_html(code: str, filename: str):
    """
        Writes code to html file.
    """
    # newdir(config.user["outputFile"])
    with open(config.user["outputFile"], "w") as f:
        f.write(f"<!DOCTYPE html>\n<!--- {config.PACKAGE_COMMENT} --->\n{code}"
                )  # noqa
