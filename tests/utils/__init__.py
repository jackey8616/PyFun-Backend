
import json

def check_attributes(route, data):
    assert route['type'] is not None
    assert route['url'] is not None
    assert route['methods'] is not None

    assert data['title'] is not None
    assert data['description'] is not None
    assert data['code'] is not None
    assert data['fields'] is not None


async def post(cli, url, data, callback=None):
    if type(data) is not str:
        data = json.dumps(data)
    res = await cli.post(url, data=data)
    # POST status code
    assert res.status == 200, res.status
    # Function
    res_data = await res.json()
    assert res_data['data']['result'] is True, \
           '\n{0}'.format(json.dumps(res_data, indent=4))

    if callback:
        callback(res_data)
