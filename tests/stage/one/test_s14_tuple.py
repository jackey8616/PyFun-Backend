from stage.one.s14_tuple import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'tuple',
        'field_2': '0',
        'field_3': 'tuple_1'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
