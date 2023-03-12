from chalice import Chalice, Response, CORSConfig

app = Chalice(app_name='myapp')
app.debug = True

cors_config = CORSConfig(
    allow_origin=['http://localhost/*'],
    allow_headers=['X-Requested-With', 'Content-Type', 'Accept'],
)

@app.route('/', methods=['GET'], cors=cors_config)
def index():
    with open('./frontend/dist/index.html', 'r') as f:
       body = f.read()
    return Response(body=body, headers={'Content-Type': 'text/html'})

@app.route('/test/<path:path>', methods=['GET'], cors=cors_config)
def assets(path):
    asset = app.current_request.static_asset(path)
    with open('./frontend/dist/index.html', 'r') as f:
       body = f.read()
    return Response(body=body, headers={'Content-Type': 'text/html'})
  
@app.route('/assets/<path:path>', methods=['GET'], cors=cors_config)
def assets(path):
    asset = app.current_request.static_asset(path)
    if asset is not None:
        return Response(body=asset.data, headers={'Content-Type': asset.content_type})
    else:
        return Response(body='File not found', status_code=404)