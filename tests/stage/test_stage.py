import pytest
from tests.utils import get

@pytest.mark.asyncio
async def test_index_get(app):
    def override(res_data):
        data = res_data['data']
        assert 'one' in data, data
        one = data['one']
        assert 'index' in one, one
        assert 'url' in one, one
        index = one['index']
        url = one['url']
        assert index == 1, index
        assert url == '/stage/one/', url
    
    await get(cli=app.asgi_client, url='/stage/', callback=override)

@pytest.mark.asyncio
async def test_lesson_get(app):
    def override(res_data):
        data = res_data['data']
        assert 'hello_python' in data, data
        hello_python = data['hello_python']
        assert 'index' in hello_python, hello_python
        assert 'url' in hello_python, hello_python
        index = hello_python['index']
        url = hello_python['url']
        assert index == '1', index
        assert url == '/stage/one/hello_python'

    await get(cli=app.asgi_client, url='/stage/one', callback=override)

@pytest.mark.asyncio
async def no_stage_lesson_get(app):
    def override(res_data):
        assert res_data['error'] == 'No such stage.'

    await get(cli=app.asgi_client,
              url='/stage/there.is&No.This-stage',
              callback=override)
