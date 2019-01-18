from stage.YunWC2019.s8_if import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': '9',
        'field_2': '"Good!"'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
