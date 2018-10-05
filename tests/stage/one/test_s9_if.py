
import json


async def test_if(test_cli):
    req_data = json.dumps({
        'field_1': 'age>18'})
    
    res = await test_cli.post('/stage/one/if', data=req_data)
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
