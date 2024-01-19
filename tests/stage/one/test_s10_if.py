import pytest
from stage.one.s10_if import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'age>18',
    }
    await post(test_cli, route['url'], data=req_data)
