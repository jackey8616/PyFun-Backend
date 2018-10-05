
import json


async def test_if(test_cli):
    req_data = json.dumps({
        'field_1': 'x',
        'field_2': '>',
        'field_3': '18'})
    
    res = await test_cli.post('/stage/two/list_comprehensions', data=req_data)
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
