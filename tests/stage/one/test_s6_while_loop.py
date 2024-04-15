import pytest
from tests.utils import get, post


@pytest.mark.asyncio
async def test_lesson(stage_manager, test_cli):
    lesson = stage_manager.get_stages()['one'].get_lessons()['while_loop']
    url = lesson.setup.url

    await get(cli=test_cli, url=url)
    req_data = {
        'field_1': 'while',
        'field_2': 'indicator'
    }
    await post(cli=test_cli, url=url, data=req_data)
