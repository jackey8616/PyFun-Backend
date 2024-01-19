import pytest
from sanic_testing.reusable import ReusableClient

import pytest
from stage.two.s4_comment import route, data
from tests.utils import check_attributes, get, post


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
            'field_1': '#',
            'field_2': '\'\'\'',
            'field_3': '\'\'\'',
    }
    await post(test_cli, route['url'], data=req_data)
