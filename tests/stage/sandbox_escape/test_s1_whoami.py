import pytest
from stage.sandbox_escape.s1_whoami import route, data
from tests.utils import get, post, check_attributes


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    def override(res_data):
        pass

    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'print(__import__("getpass").getuser())#'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
