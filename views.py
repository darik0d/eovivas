import asyncio
import aiohttp.web

your_state_here = {'counter': 0}

active_clients = []

async def index(request):
    return aiohttp.web.Response(text='<your template here>')


async def do_update(request):
    # your logic here

    your_state_here['counter'] += 1

    for ws in active_clients:
        ws.send_str('updated %s' % your_state_here['counter'])

    return aiohttp.web.Response(text='Ok')


async def on_state_update(request):
    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)

    active_clients.append(ws)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                active_clients.remove(ws)
                await ws.close()

    return ws


def main():
    loop = asyncio.get_event_loop()
    app = aiohttp.web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('POST', '/do_update', do_update)
    app.router.add_route('GET', '/updates', on_state_update)
    aiohttp.web.run_app(app, port=3000)


if __name__ == '__main__':
    main()