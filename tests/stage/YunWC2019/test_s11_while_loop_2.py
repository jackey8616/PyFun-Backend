from stage.YunWC2019.s11_while_loop_2 import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'num < 5'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
