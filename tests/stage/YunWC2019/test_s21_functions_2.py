import pytest
from stage.YunWC2019.s21_functions_2 import route, data
from tests.utils import get, post, check_attributes


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'y',
        'field_2': 'return',
        'field_3': '10'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
