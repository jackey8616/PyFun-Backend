from stage.YunWC2019.s16_dictionaries import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': '{',
        'field_2': '}',
        'field_3': '\'age\'',
        'field_4': '1970/01/01'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
