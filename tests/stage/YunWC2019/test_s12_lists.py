import pytest
from stage.YunWC2019.s12_lists import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': '0',
        'field_2': '2',
        'field_3': '2',
        'field_4': 'numbers'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
