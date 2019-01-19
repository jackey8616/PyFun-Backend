from stage.YunWC2019.s18_for_loop import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'for',
        'field_2': 'in',
        'field_3': '3',
        'field_4': 'n'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
