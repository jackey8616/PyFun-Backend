import pytest

from sanic import Sanic
from sanic_testing import TestManager

from controller.index import index
from controller.stage import stage_blueprint


@pytest.fixture(scope='session')
def app():
    app = Sanic('PyFun-Test')
    TestManager(app)
    app.blueprint(stage_blueprint)

    app.add_route(index, '/', methods=['GET'])

    return app


@pytest.fixture(scope='session')
def test_cli(app):
    return app.asgi_client
