import requests

url = "https://jsonplaceholder.typicode.com/posts/"

response = requests.get(url)
# print(response.status_code)

# print(response.json())

postovi = response.json()
print(len(postovi))

prvi_post = postovi[0]
print(prvi_post)

assert len(postovi) > 0

# ocekivani kljucevi userId, id, title, body
assert "userId" in prvi_post
assert "id" in prvi_post
assert "title" in prvi_post
assert "body" in prvi_post