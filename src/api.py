import requests as r
url="https://jsonplaceholder.typicode.com/users/1"


data={
    'name':'Chandler  Bing'
}
r2=r.patch(url,json=data)
print(r2.status_code)
response=r.get(url)
print(response.status_code)
print(type(response.json()))
for i in response.json().items():
    print(i)

    