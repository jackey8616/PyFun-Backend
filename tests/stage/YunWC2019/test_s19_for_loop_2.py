import pytest
from stage.YunWC2019.s19_for_loop_2 import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'for',
        'field_2': 'numbers',
        'field_3': 'n'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
