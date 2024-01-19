import pytest
from stage.one.s4_for_loop import route, data
from tests.utils import get, post, check_attributes


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': '0',
        'field_2': '10',
        'field_3': '2'
    }
    await post(test_cli, route['url'], data=req_data)
