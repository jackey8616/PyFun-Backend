from stage.YunWC2019.s21_functions_2 import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'y',
        'field_2': 'return',
        'field_3': '10'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
