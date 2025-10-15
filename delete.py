from http.server import BaseHTTPRequestHandler,HTTPServer
import json

data = [{
    'name':'Sam larry',
    'track':'Ai Engineer'
}]


class BaseAPI(BaseHTTPRequestHandler):
    def send_data(self,payload,status=200):
        self.send_response(status)
        self.send_header('content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_PUT(self):
        content_size = int(self.headers.get('content-Length',0))
        raw_data=self.rfile.read(content_size)
        new_data=json.loads(raw_data.decode())
        for i in data:
            if i['name']== new_data['name']:
                del i  #like saving to a database
        
def run():
    HTTPServer(('localhost',8000),BaseAPI).serve_forever()


print('Application is running')
run()