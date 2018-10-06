from stage.one.s9_functions import route, data
from tests.utils import *

def test_attributes():
    check_attributes(route, data)

async def test_lesson(test_cli):
    await get(cli=test_cli, url=route['url'])
    req_data = {
        'field_1': 'num1',
        'field_2': 'num2',
        'field_3': 'return'
    }
    await post(cli=test_cli, url=route['url'], data=req_data)
