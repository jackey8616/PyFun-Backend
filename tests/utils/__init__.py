from json import loads as json_loads
from json import dumps as json_dumps
from sanic_testing.testing import SanicASGITestClient

def check_attributes(route, data):
    assert route['type'] is not None
    assert route['url'] is not None
    assert route['methods'] is not None

    assert data['title'] is not None
    assert data['description'] is not None
    assert data['code'] is not None


async def get(cli: SanicASGITestClient, url: str, callback=None):
    _, res = await cli.get(url)
    assert res.status == 200

    res_data = json_loads(res.body)

    if callback:
        callback(res_data)


async def post(cli: SanicASGITestClient, url: str, data, callback=None):
    if type(data) is not str:
        data = json_dumps(data)
    _, res = await cli.post(url, data=data)
    assert res.status == 200, res.status
    res_data = json_loads(res.body)
    assert res_data['data']['result'] is True, \
        '\n{0}'.format(json_dumps(res_data, indent=4))

    if callback:
        callback(res_data)
