import click
from sanic import Sanic
from sanic_cors import CORS

from controller.index import favicon, index
from controller.stage import stage_blueprint, add_route_by_imports, add_route_by_stages
from manager import StageManager

app = Sanic('PyFun')
stage_manager = StageManager().build_from_static()

add_route_by_imports(stage_blueprint)
add_route_by_stages(stage_blueprint, stage_manager.get_stages())

app.blueprint(stage_blueprint)

app.add_route(favicon, '/favicon.ico', methods=['GET'])
app.add_route(index, '/', methods=['GET'])

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
