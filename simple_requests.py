import requests

url = 'https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html'
r = requests.get(url)

print(r.text)
# content = r.headers['content-type']
# print(content)

# status = r.status_code
# print(status)

# encoding = r.encoding
# print(encoding)