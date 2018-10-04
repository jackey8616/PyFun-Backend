import pytest
import asyncio
from pytest_sanic.utils import TestClient

from sanic import Sanic
from app import index, path_check as pc
from stage import add_route as stage_add_route


@pytest.fixture(scope='module')
def path_check():
    pc()


@pytest.yield_fixture(scope='module')
def app(path_check):
    app = Sanic()
    app.add_route(index, '/', methods=['GET'])
    stage_add_route(app)
    yield app


@pytest.fixture(scope='module')
def loop():
    # Reference from pytest_sanic.plugin#loop to give a new scope.
    loop = asyncio.get_event_loop()
    yield loop


@pytest.fixture(scope='module')
def test_client(loop):
    # Reference from pytest_sanic.plugin#test_client to give a new scope.
    clients = []

    async def create_client(app, **kwargs):
        client = TestClient(app, loop=loop, **kwargs)
        await client.start_server()
        clients.append(client)
        return client

    yield create_client

    if clients:
        for client in clients:
            loop.run_until_complete(client.close())


@pytest.fixture(scope='module')
def test_cli(loop, app, test_client):
    yield loop.run_until_complete(test_client(app))
