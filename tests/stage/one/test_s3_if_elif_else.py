import json


async def test_if_elif_else(test_cli):
    res = await test_cli.post('/stage/one/if_elif_else', data=json.dumps({'field_1': '\'test\''}))
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
