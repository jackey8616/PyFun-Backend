import pytest
from stage.one.s8_dict import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'counter',
        'field_2': 'counter'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
