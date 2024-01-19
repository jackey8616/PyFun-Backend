import pytest
from stage.YunWC2019.s4_string_operations import route, data
from tests.utils import get, post, check_attributes


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': '+',
        'field_2': '* 3'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
