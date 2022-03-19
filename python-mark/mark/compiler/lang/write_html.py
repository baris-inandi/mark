from mark.config import config
from os import makedirs, path


def write_html(code: str):
    output_dirname = path.dirname(config.user["outputFile"])
    if output_dirname != "":
        makedirs(path.dirname(config.user["outputFile"]), exist_ok=True)
    with open(config.user["outputFile"], "w") as f:
        n = "" if config.user["minify"] else "\n"
        f.write(
            f"<!DOCTYPE html>{n}<!--- {config.PACKAGE_COMMENT} --->{n}{code}"
        )  # noqa
