from stage.YunWC2019.s1_print import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'print',
        'field_2': '~")'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
