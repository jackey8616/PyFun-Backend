import json


async def test_list(test_cli):
    res = await test_cli.post('/stage/one/list', data=json.dumps({'field_1': 'sort', 'field_2': 'reverse'}))
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
