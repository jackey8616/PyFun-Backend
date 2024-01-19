import pytest
from stage.YunWC2019.s6_in_place_operators import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': '+=',
        'field_2': '*=',
        'field_3': '+ 16',
        'field_4': '7'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
