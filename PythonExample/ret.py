from http.client import HTTPConnection

conn = HTTPConnection("example.com")

conn.request("GET", "/")

result = conn.getresponse()

contents = result.read()

print(contents)