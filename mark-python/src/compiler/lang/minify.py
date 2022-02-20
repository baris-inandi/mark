def js(code: str) -> str:
    try:
        import rjsmin
        return rjsmin.jsmin(code)
    except Exception:
        return code


def css(code: str) -> str:
    try:
        import rcssmin
        return rcssmin.cssmin(code)
    except Exception:
        return code


def html(code: str) -> str:
    # TODO: htmlmin is pretty unreliable
    return code
