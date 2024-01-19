import pytest
from click.testing import CliRunner
from json import loads as json_loads
from app import run


def test_run():
    runner = CliRunner()
    result = runner.invoke(run, ['--test', 'True'])
    assert result.exit_code == 0

@pytest.mark.asyncio
async def test_index(test_cli):
    _, res = await test_cli.get('/')
    assert res.status == 200
    res_data = json_loads(res.body)
    assert res_data['success'] is True
