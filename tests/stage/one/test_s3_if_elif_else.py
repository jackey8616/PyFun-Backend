import pytest
from stage.one.s3_if_elif_else import route, data
from tests.utils import get, post, check_attributes


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {'field_1': '\'test\''}
    await post(test_cli, route['url'], data=req_data)
