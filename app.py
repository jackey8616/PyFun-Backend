import sys, os, click
from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

from stage import add_route as stage_add_route


app = None


def path_check():
    path = os.path.join(os.getcwd(), 'tmp/')
    if not os.path.exists(path):
        os.mkdir(path)


@click.command()
@click.option('--host', default='0.0.0.0', type=str)
@click.option('--port', default=8000, type=int)
@click.option('--test', default=False, type=bool)
def run(host, port, test):
    path_check()
    global app
    app = Sanic()
    CORS(app)
    app.add_route(index, '/', methods=['GET'])
    stage_add_route(app)
    if not test:
        app.run(host=host, port=port)



async def index(request):
    return json({'success': True, 'data': 'Hello World!'})


if __name__ == '__main__':
    run()
