import json


async def test_functions(test_cli):
    req_data = json.dumps({
        'field_1': 'num1',
        'field_2': 'num2',
        'field_3': 'return'
    })
    res = await test_cli.post('/stage/one/functions', data=req_data)
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
