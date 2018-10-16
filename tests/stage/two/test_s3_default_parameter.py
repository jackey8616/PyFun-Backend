from stage.two.s3_default_parameter import route, data
from tests.utils import check_attributes, post


def test_attributes():
    check_attributes(route, data)


async def test_lesson(test_cli):
    def override(res_data):
        pass

    req_data = {
        'field_1': 'v2',
        'field_2': 'v2',
        'field_3': 'v2 = "foo2"'
    }

    await post(cli=test_cli, url=route['url'], data=req_data, callback=override)


async def test_lesson_stderr(test_cli):
    def override(res_data):
        pass

    req_data = {
        'field_1': 'v2',
        'field_2': 'v2',
        'field_3': 'v2'
    }

    await post(cli=test_cli, url=route['url'], data=req_data, callback=override)

