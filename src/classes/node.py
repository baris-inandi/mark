from src.lib.error import throw
from termcolor import colored


class Node:
    def __init__(self, code: str, line: int):
        """
            class Node:
            represents a single HTML element Eg. <div>

            special nodes:
                _document
                    represents a piece of html that is imported using require.
                    its block_inner is the html code that is imported.
                _module
                    represents a module that is imported using require.
                    these modules should be parsed by the parser first.
                _plaintext
                    a text child of a node with no tags
                _null
                    does not represent an HTML element, used for internal
                    purposes in the Dom.to_html() method
        """

        # The HTML tag of the Node Eg. "div"
        self.tag = code.split()[0].lower()
        # Line number of the Node
        self.line = line
        # The input code of the Node Eg. "    div {...}"
        self.code = code.strip()
        # The indentation level of the Node Eg. 2
        self.indent = len(code) - len(code.lstrip())
        # The HTML attributes of the Node Eg. src="foo.png"
        self.attr = ""
        # The contents of a block, if the Node is a block Eg. JS or CSS code
        self.block_inner = ""

    def __repr__(self):
        return f"<{self.tag}/>"

    def props(self):
        out = self.code.split(" ", 1)[-1]
        if out.startswith("\"") or out.startswith("'"):
            return ""
        return out

    def opening_tag(self):
        if self.tag.startswith("_"):
            return self.block_inner
        return f"<{self.tag}{' ' if self.attr else ''}{self.attr}>"

    def closing_tag(self):
        return "" if self.tag.startswith("_") else f"</{self.tag}>"

    def open_close_tag(self):
        return f"{self.opening_tag()}{self.closing_tag()}"

    def parse_attr(self) -> str:
        """
            The constructor of Node will not parse attributes of the element.
            This is because of the extension "and" statement which makes it
            possible that the parser can change self.code when reading a line
            that starts with "and".

            Call this method to re-generate self.attr
            Eg. when self.code is changed.
        """

        if self.tag.startswith("_"):
            # protected tags start with an underscore, do not parse these tags
            return self.attr

        split_props = self.props().split("attr", 1)
        selectors = split_props[0].strip()
        custom_attr = split_props[1].strip() if len(split_props) > 1 else ""
        split_selectors = selectors.split(" ")

        # parse selectors and attributes
        has_an_id = False
        classes: set[str] = set()
        _id = ""
        for index, s in enumerate(split_selectors):
            if index == 0 and s == self.tag:
                # prevent no-selector elements' tags
                # from being parsed as selectors
                continue
            if s.startswith("."):
                # selector is class
                classes.add(s)
            elif s.startswith("#"):
                # selector is id
                if not has_an_id:
                    has_an_id = True
                    _id = f"id=\"{s[1:]}\""
                else:
                    throw("HTML elements must always have one id")
            elif s:
                """
                    selector is not a class nor an id
                    checks if s is empty string because
                    an html element with no id or class will
                    have an empty string in split_selectors
                    which should not raise an error
                """
                invalid_selector = colored(f'"{s}"', "yellow")
                throw([
                    f'Invalid selector: cannot resolve {invalid_selector}',
                    'selectors must start with a "." or "#"',
                ],
                      docs="selectors")
        class_attr = f'class=\"{" ".join([str(s[1:]) for s in classes])}\"'

        # construct a valid HTML attribute string
        attr = []
        if has_an_id:
            attr.append(_id)
        if classes:
            attr.append(class_attr)
        if len(custom_attr) > 0:
            attr.append(custom_attr)
        self.attr = " ".join(attr)
        return self.attr
