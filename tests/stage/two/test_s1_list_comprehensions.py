import pytest
from stage.two.s1_list_comprehensions import route, data
from tests.utils import check_attributes, post


def test_attributes():
    check_attributes(route, data)

@pytest.mark.asyncio
async def test_lesson(test_cli):
    def override(res_data):
        pass

    req_data = {
        'field_1': 'for',
        'field_2': 'in',
        'field_3': 'range',
        'field_4': '10'
    }
    await post(cli=test_cli, url=route['url'], data=req_data, callback=override)
