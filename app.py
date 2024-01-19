import os
import click
from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
from stage import add_route as stage_add_route, stageBp


async def favicon(request):
    return json({})


async def index(request):
    return json({'success': True, 'data': 'Hello World!'})


app = Sanic('PyFun')
app.blueprint(stageBp)

app.add_route(favicon, '/favicon.ico', methods=['GET'])
app.add_route(index, '/', methods=['GET'])
stage_add_route()

CORS(app)

@click.command()
@click.option('--host', default='0.0.0.0', type=str)
@click.option('--port', default=8000, type=int)
@click.option('--ssl-cert', default='./server.pem', type=str)
@click.option('--ssl-key', default='./server.key', type=str)
@click.option('--test', default=False, type=bool)
def run(host, ssl_cert, ssl_key, port, test):
    if not test:
        ssl = {
            "cert": ssl_cert,
            "key": ssl_key,
        }
        app.run(host=host, port=port, ssl=ssl)


if __name__ == '__main__':
    run()
