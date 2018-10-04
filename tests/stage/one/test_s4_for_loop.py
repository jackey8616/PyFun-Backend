import json


async def test_for_loop(test_cli):
    req_data = json.dumps({
        'field_1': '0',
        'field_2': '10',
        'field_3': '2'
    })
    res = await test_cli.post('/stage/one/for_loop', data=req_data)
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
