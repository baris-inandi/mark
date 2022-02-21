from mark.utils.error import throw, error_file
from mark.utils.utils import minimal_indentation
from mark.config import config


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
            from mark.compiler.lang import minify
            # lesscpy.compile() does not properly minify, so use minify.css()
            out = lesscpy.compile(StringIO(code))
            if config.MINIFY:
                return minify.css(out)
            else:
                return out
    except Exception as e:
        throw(
            (f'Cannot compile {lang.upper()}\nPreprocessor Output:\n\n    ' +
             str(e).replace('\n', '\n    ')),
            docs='preprocess',
        )
