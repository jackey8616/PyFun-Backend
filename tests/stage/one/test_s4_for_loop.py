import pytest
from tests.utils import get, post, check_attributes


@pytest.mark.asyncio
async def test_lesson(stage_manager, test_cli):
    lesson = stage_manager.get_stages()['one'].get_lessons()['for_loop']
    url = lesson.setup.url

    await get(cli=test_cli, url=url)
    req_data = {
        'field_1': '0',
        'field_2': '10',
        'field_3': '2'
    }
    await post(cli=test_cli, url=url, data=req_data)
