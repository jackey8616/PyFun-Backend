import json


async def test_basic_type(test_cli):
    req_data = json.dumps({'field_1': '90'})
    res = await test_cli.post('/stage/one/basic_type', data=req_data)
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
