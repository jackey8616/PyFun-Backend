
from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin

from stage import add_route as stage_add_route

app = Sanic()
CORS(app)
stage_add_route(app)

@app.route('/', methods=['GET'])
async def index(request):
    return json({ 'success': True, 'data': 'Hello World!' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
