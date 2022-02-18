import asyncio

import websockets
from src.compiler.compiler import compile


# create handler for each connection
async def handler(websocket):

    code = compile("ignore/test.mark",
                   time_message=True,
                   return_as_string=True)
    await websocket.send(code)


def start(filename: str):
    start_server = websockets.serve(handler, "localhost", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
