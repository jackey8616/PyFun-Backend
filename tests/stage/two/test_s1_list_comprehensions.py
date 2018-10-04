import json


async def test_list_comprehensions(test_cli):
    req_data = json.dumps({
        'field_1': 'for',
        'field_2': 'in',
        'field_3': 'range',
        'field_4': '10'
    })
    res = await test_cli.post('/stage/two/list_comprehensions', data=req_data)
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
