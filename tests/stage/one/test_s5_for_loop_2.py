from stage.one.s5_for_loop_2 import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': '5',
        'field_2': 'each + 45'
    }
    await post(test_cli, route['url'], data=req_data)
