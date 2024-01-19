import pytest
from stage.YunWC2019.s14_list_functions import route, data
from tests.utils import get, post, check_attributes


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'append',
        'field_2': '3',
        'field_3': '\'d\'',
        'field_4': 'len',
        'field_5': 'index'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
