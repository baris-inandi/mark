from src.compiler.compiler import compile
from src.utils.error import throw
from src import config
from os.path import dirname
import pyinotify
from termcolor import cprint

f = ""


def on_modify(event):
    try:
        compile(f, time_message=True)
    except Exception:
        print("Compilation Error.")


def on_delete(event):
    throw("File deleted, closing watcher.")
    exit(1)


def watch(filename: str):
    global f
    f = filename
    config.ERROR_NO_EXIT = True
    wm = pyinotify.WatchManager()
    wm.add_watch(dirname(filename), pyinotify.IN_MODIFY, on_modify)
    notifier = pyinotify.Notifier(wm)
    cprint(f"[Watching {filename}]", "blue")
    notifier.loop()
