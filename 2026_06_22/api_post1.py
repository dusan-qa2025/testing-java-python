import requests

url = "https://jsonplaceholder.typicode.com/posts/"
posts = requests.get(url).json()

assert len(posts) > 0

for post in posts:
    # ocekivani kljucevi userId, id, title, body
    assert "userId" in post
    assert "id" in post
    assert "title" in post
    assert "body" in post

# dohvati listu postova - imamo gore u posts
# uzmi jedan iz liste - id - uzimamo iz petlje
# otvori detalje tog posta - otvaramo u petlji
# proveri detalje - proveravamo u petlji
{"id":123, "userId":543543, "title":"fsdfdsfds", "body": "fdsfsdfds"}
for post in posts:
    post_id = post["id"]
    post_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    odgovor = requests.get(post_url)
    print(odgovor.json())
    # proveriti kljuceve ili proveriti dobijene vrednosti ako treba