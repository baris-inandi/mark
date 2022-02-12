from src.lib.error import throw, error_file
from src.lib.utils import minimal_indentation


def get_styling_language(line: str):
    if "lang='sass'" in line or 'lang="sass"' in line:
        return "sass"
    elif "lang='scss'" in line or 'lang="scss"' in line:
        return "scss"
    elif "lang='css'" in line or 'lang="css"' in line:
        return "css"
    elif "lang='less'" in line or 'lang="less"' in line:
        return "less"
    elif "lang='" in line or 'lang="' in line:
        throw([
            "Unknown styling language specified in style block.",
            "Valid languages are: sass, scss, css, less"
        ],
              docs="preprocess")


def to_css(code: str, lang: str, filename: str = ""):
    indented = lang == "sass"
    if indented and not filename:
        """
            libsass requires the first selector or at-rule to have
            zero indentation, this is why the smallest indentation level
            should be removed from all lines in the block
            so that the first selector/rule is certainly at level 0.
        """
        code = "\n".join(minimal_indentation(code.split("\n")))
    try:
        if filename != "":
            error_file(filename)
        if lang in {"scss", "sass"}:
            import sass as libsass
            return libsass.compile(string=code,
                                   indented=indented,
                                   output_style='compressed')
        elif lang == "less":
            import lesscpy
            from six import StringIO
            from src.lib import minify
            # lesscpy.compile() does not properly minify, so use minify.css()
            return minify.css(lesscpy.compile(StringIO(code)))
    except Exception as e:
        throw(
            (f'Cannot compile {lang.upper()}\nPreprocessor Message:\n\n    ' +
             str(e).replace('\n', '\n    ')),
            docs='preprocess',
        )
