import click
from functools import partial
from sanic import Sanic
from sanic.worker.loader import AppLoader
from sanic_cors import CORS

from controller.index import favicon, index
from controller.stage import stage_blueprint, add_route_by_imports, add_route_by_stages
from manager import StageManager

def create_app(app_name: str) -> Sanic:
    app = Sanic(app_name)
    stage_manager = StageManager().build_from_static()

    add_route_by_imports(stage_blueprint)
    add_route_by_stages(stage_blueprint, stage_manager.get_stages())

    app.blueprint(stage_blueprint)

    app.add_route(favicon, '/favicon.ico', methods=['GET'])
    app.add_route(index, '/', methods=['GET'])

    CORS(app)

    return app

@click.command()
@click.option('--host', default='0.0.0.0', type=str)
@click.option('--port', default=8000, type=int)
@click.option('--ssl', default=True, type=bool)
@click.option('--ssl-cert', default='./server.pem', type=str)
@click.option('--ssl-key', default='./server.key', type=str)
@click.option('--test', default=False, type=bool)
def run(host, ssl, ssl_cert, ssl_key, port, test):
    if test:
        return

    ssl_config = {
        "cert": ssl_cert,
        "key": ssl_key,
    } if ssl else None
    app_name = 'PyFun'
    loader = AppLoader(factory=partial(create_app, app_name))
    app = loader.load()
    app.prepare(host=host, port=port, ssl=ssl_config)
    Sanic.serve(primary=app, app_loader=loader)


if __name__ == '__main__':
    run()
