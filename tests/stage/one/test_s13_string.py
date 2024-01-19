import pytest
from stage.one.s13_string import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
            'field_1': 'len',
            'field_2': 'split',
            'field_3': 'replace',
            'field_4': '41',
            'field_5': '42',
            'field_6': '43'
    }
    await post(test_cli, route['url'], data=req_data)
