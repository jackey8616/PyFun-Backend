
import os
from click.testing import CliRunner

from app import path_check, run


def test_path_check():
    path = os.path.join(os.getcwd(), 'tmp/')
    if not os.path.exists(path):
        path_check()
    assert os.path.exists(path)


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
