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

    def do_POST(self):
        content_size = int(self.headers.get('content-Length',0))
        parsed_data=self.rfile.read(content_size)
        post_data=json.loads(parsed_data)
        data.append(post_data) #like saving to a database
        self.send_data({
            'Message':'Data received',
            'data': post_data
        })

def run():
    HTTPServer(('localhost',8000),BaseAPI).serve_forever()


print('Application is running')
run()