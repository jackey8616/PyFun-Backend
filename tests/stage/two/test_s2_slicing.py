from stage.two.s2_slicing import route, data
from tests.utils import check_attributes, post


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    def override(res_data):
        pass

    req_data = {
        'field_1': 3,
        'field_2': 8,
        'field_3': 3,
        'field_4': 8,
        'field_5': -1,
        'field_6': 7,
        'field_7': 2,
        'field_8': -1
    }
    await post(cli=test_cli, url=route['url'], data=req_data, callback=override)
