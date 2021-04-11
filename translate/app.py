from chalice import Chalice
from boto3 import client

app = Chalice(app_name='translate')

@app.route('/')
def index():
    return {'hello': 'world1'}