import json


async def test_while_loop(test_cli):
    res = await test_cli.post('/stage/one/while_loop', data=json.dumps({'field_1': 'while', 'field_2': 'indicator'}))
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
