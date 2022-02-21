from mark.utils.error import throw
from mark.compiler.classes.node import Node
from collections import defaultdict

refs: defaultdict[str, str] = defaultdict(lambda: "")
refs["tailwind"] = '<script src="https://cdn.tailwindcss.com"></script>'
refs["bootstrap"] = """
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
""" # noqa
refs[
    "jquery"] = '<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js" integrity="sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>'  # noqa
refs[
    "lodash"] = '<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js" integrity="sha256-qXBd/EfAdjOA2FGrGAG+b3YBn2tn5A6bhz+LSgYD96k=" crossorigin="anonymous"></script>'  # noqa
refs[
    "fontawesome"] = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" integrity="sha512-9usAa10IRO0HhonpyAIVpjrylPvoDwiPUiKdWk5t3PyolY1cOd4DSE0Ga+ri4AuTroPR5aQvXU9xC6qOPnzFeg==" crossorigin="anonymous" referrerpolicy="no-referrer" />'  # noqa
refs[
    "petite-vue"] = '<script src="https://unpkg.com/petite-vue" defer init></script>'  # noqa
refs[
    "popper"] = '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>'  # noqa


def external_require(name: str, line_number: int, indent: int) -> Node:
    """
        External require:
            To require a common utility library.
            External requires are denoted using a "@" prefix on the uri.
            Eg. "require @lodash" will import lodash through a CDN.

            require @tailwind
            require @bootstrap
            require @jquery
            require @lodash
            require @fontawesome
            require @petite-vue
    """
    name = name[1:]  # remove the @ prefix
    innerhtml = refs[name]
    if innerhtml == "":
        throw(f"Unknown external require: @{name}", docs="require")
    n = Node("_document", line_number)
    n.block_inner = innerhtml
    n.indent = indent
    return n
