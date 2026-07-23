from flask import Flask, jsonify, request

app = Flask(__name__)

# simulacija podataka
products = [
    {"id":1, "title":"Laptop","price":1200, "available":True},
    {"id":2, "title":"Keyboard","price":120, "available":False},
    {"id":3, "title":"Mouse","price":50, "available":True}
]

@app.get("/")
def home():
    #return "Pozdrav, pogledajte dokumentaciju. Server funkcionise."
    podaci = {"message":"API funkcionise, pogledajte dostupne putanje"}
    return jsonify(podaci)

@app.get("/products")
def get_products():
    return jsonify(products)

@app.get("/products/<int:product_id>")
def get_product(product_id):
    # prodji kroz listu proizvoda i pronadji specifican proizvod
    for product in products:
        print(product, product_id)
        if product["id"] == product_id:
            return jsonify(product)
  
    poruka = {"message":"Product not found"}
    return jsonify(poruka, 404)

# ruta - POST metod, za kreiranje proizvoda
@app.post("/products")
def create_product():
    # pokupiti od korisnika iz zahteva te podatke
    podaci = request.get_json()
    novi_proizvod = {
        "id":len(products) + 1,
        "title": podaci["title"],
        "price": podaci["price"],
        "available": podaci["available"]
    }
    products.append(novi_proizvod)
    return jsonify(novi_proizvod)

app.run(debug=True)