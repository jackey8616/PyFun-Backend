from stage.one.s2_basic_type import route, data
from tests.utils import *

def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {'field_1': '90'}
    await post(test_cli, route['url'], data=req_data)
