from mark.compiler.compiler import compile
from mark.utils.error import throw
from mark.config import config
from os.path import dirname, isfile, abspath
from termcolor import cprint, colored
from time import sleep
import pyinotify

f = ""


def on_modify(event):
    if not (event is not None and
            (event.pathname == abspath(config.user["outputFile"]))):
        try:
            compile(f, time_message=True)
        except Exception as e:
            cprint("Compilation Error.", "red")
            print(e)
    sleep(0.1)


def on_delete(event):
    throw("File deleted, closing watcher.")
    exit(1)


def watch(filename: str):
    if not isfile(filename):
        filename = colored(filename, "yellow")
        throw(f'File not found: "{filename}"')
    if not filename.endswith(config.EXTENSION):
        filename = colored(filename, "yellow")
        throw(
            f'File must end with ".{config.EXTENSION}" extension: "{filename}"'
        )
    global f
    f = filename
    config.ERROR_NO_EXIT = True
    wm = pyinotify.WatchManager()
    wm.add_watch(dirname(filename), pyinotify.IN_MODIFY, on_modify)
    notifier = pyinotify.Notifier(wm)
    cprint(f"[Watching {filename}]", "blue")
    on_modify(None)
    notifier.loop()
