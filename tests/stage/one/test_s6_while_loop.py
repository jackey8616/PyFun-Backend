from stage.one.s6_while_loop import route, data
from tests.utils import check_attributes, post


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    req_data = {
        'field_1': 'while',
        'field_2': 'indicator'
    }
    await post(test_cli, route['url'], data=req_data)
