import os
from click.testing import CliRunner

from app import run


def test_run():
    runner = CliRunner()
    result = runner.invoke(run, ['--test', 'True'])
    assert result.exit_code == 0


async def test_index(test_cli):
    res = await test_cli.get('/')
    assert res.status == 200
    res_data = await res.json()
    assert res_data['success'] is True
    await test_cli.close()
