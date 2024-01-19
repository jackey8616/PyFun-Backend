import pytest
from stage.YunWC2019.s22_functions_3 import route, data
from tests.utils import get, post, check_attributes


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'numbers',
        'field_2': '+=',
        'field_3': 's',
        'field_4': 'len'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
