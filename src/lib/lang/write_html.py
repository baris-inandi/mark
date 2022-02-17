# TODO: implement
def write_html(code: str):
    """
        Writes code to html file.
    """
    with open("index.html", "w") as f:
        f.write(code)
