import pytest
from stage.YunWC2019.s17_range import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': '5',
        'field_2': '6',
        'field_3': '11',
        'field_4': '10',
        'field_5': '0',
        'field_6': '-2'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
