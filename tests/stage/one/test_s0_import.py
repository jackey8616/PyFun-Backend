from stage.one.s0_import import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1':'import',
        'field_2':'pyperclip'

    }
    await post(cli=test_cli, url=route['url'], data=req_data)
