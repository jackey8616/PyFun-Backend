
from sanic import Sanic
from sanic.response import json

from stage import add_route as stage_add_route

app = Sanic()
stage_add_route(app)

@app.route('/', methods=['GET'])
async def index(request):
    return json({ 'success': True, 'data': 'Hello World!' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
