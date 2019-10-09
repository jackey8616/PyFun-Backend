from stage.sandbox_escape.s4_whatsinreadme import route, data
from tests.utils import *


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    def override(res_data):
        pass

    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'print(__import__("os").system("README.md"))#'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
