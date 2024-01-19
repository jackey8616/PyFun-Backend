import pytest

from sanic import Sanic
from sanic_testing import TestManager
from app import index
from stage import add_route as stage_add_route, stageBp


@pytest.fixture(scope='session')
def app():
    app = Sanic('PyFun-Test')
    TestManager(app)

    app.add_route(index, '/', methods=['GET'])
    stage_add_route()
    app.blueprint(stageBp)

    return app


@pytest.fixture(scope='session')
def test_cli(app):
    return app.asgi_client
