from src import config
from src.compiler.compiler import compile
from livereload import Server
from wsgiref.simple_server import make_server
from os.path import dirname


class DevServer():
    def __init__(self, environment='', response=5500):
        self.dir = config.OUTPUT_DIRECTORY
        self.environment = environment
        self.response = response

    def __iter__(self):
        response_headers = [('Content-type', 'text/html')]
        self.response("200 OK", response_headers)
        yield bytes(compile("test.mark", True), "utf-8")

    def start_forever(self):
        with make_server('', 5500, DevServer) as server:
            print("Serving on port 5500...")
            server.serve_forever()

    def serve_live(self):
        config.ERROR_NO_EXIT = True
        server = Server(DevServer)
        server.watch(dirname("ignore/test.mark"))
        server.serve(port=3000)
