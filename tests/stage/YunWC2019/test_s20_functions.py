import pytest
from stage.YunWC2019.s20_functions import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'def',
        'field_2': ':',
        'field_3': 'hello'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
