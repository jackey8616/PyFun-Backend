import json


async def test_dict(test_cli):
    req_data = json.dumps({
        'field_1': 'counter',
        'field_2': 'counter'
    })
    res = await test_cli.post('/stage/one/dict', data=req_data)
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
