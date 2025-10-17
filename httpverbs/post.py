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
        content_size = int(self.headers.get('content-Length',0)) #get the length of the header and convert to integer
        parsed_data=self.rfile.read(content_size) # read the content length
        post_data=json.loads(parsed_data) # output it in json format you can decode it first with .decode
        data.append(post_data) #like saving to a database
        self.send_data({
            'Message':'Data received',
            'data': post_data
        }) # then send a response whose content is this

def run():
    HTTPServer(('localhost',8000),BaseAPI).serve_forever()

print('Application is running')
run()