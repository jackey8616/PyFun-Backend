import pytest

from sanic import Sanic
from sanic_testing import TestManager

from controller.index import index
from controller.stage import stage_blueprint, add_route_by_stages, add_route_by_imports
from manager import StageManager


@pytest.fixture(scope='session')
def stage_manager():
    stage_manager = StageManager().build_from_static()
    return stage_manager


@pytest.fixture(scope='session')
def app(stage_manager):
    app = Sanic('PyFun-Test')
    TestManager(app)
    app.blueprint(stage_blueprint)

    app.add_route(index, '/', methods=['GET'])
    add_route_by_stages(stage_blueprint, stage_manager.get_stages())
    add_route_by_imports(stage_blueprint)

    return app


@pytest.fixture(scope='session')
def test_cli(app):
    return app.asgi_client
