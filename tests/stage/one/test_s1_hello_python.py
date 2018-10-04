
import json

async def test_hello_python(test_cli):
    res = await test_cli.post('/stage/one/hello_python', data=json.dumps({'field_1': 'print', 'field_2': 'Hello Python'}))
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] == True
    await test_cli.close()

