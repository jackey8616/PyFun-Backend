import json


async def test_for_loop_2(test_cli):
    req_data = json.dumps({
        'field_1': '5',
        'field_2': 'each + 45'
    })
    res = await test_cli.post('/stage/one/for_loop_2', data=req_data)
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
