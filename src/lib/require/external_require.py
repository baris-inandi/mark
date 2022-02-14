from src.classes.node import Node


def external_require(name: str) -> Node:
    """
        External require:
            To require a common utility library.
            External requires are denoted using a "@" prefix on the uri.
            Eg. "require @lodash" will import lodash through a CDN.
    """
    print(f"external_require: {name}")
