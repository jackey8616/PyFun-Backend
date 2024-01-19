import pytest
from stage.YunWC2019.s7_comparisons import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'True',
        'field_2': 'True',
        'field_3': 'False',
        'field_4': 'False'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
