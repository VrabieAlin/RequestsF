from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["POST"])
def hello():
    return jsonify({"message": "Hello world!"})

users = [
    {"id": 1, "name": "Alex"},
    {"id": 2, "name": "Andrei"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    new_user["id"] = len(users) + 1
    users.append(new_user)
    print(users)
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    my_user = None
    for user in users:
        if user["id"] == user_id:
            my_user = user

    if my_user != None:
        data = request.get_json()
        my_user.update(data)
        return jsonify(my_user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"})

#query param: /id?my_id=1
@app.route('/id')
def get_id():
    id = request.args.get("my_id")
    if id != None:
        print(f"Am primit de la client id-ul: {id}")
    else:
        print("Nu exista id-ul!")

    return jsonify({"Message": "Id primit!"})

# 1. Creează o rută `/search/products` care să accepte query parameters:
#    - `category` pentru a filtra produsele după categorie.
#    - `price_min` și `price_max` pentru a filtra produsele care
# au un preț în intervalul specificat.

products = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 1000},
    {"id": 2, "name": "Headphones", "category": "electronics", "price": 150},
    {"id": 3, "name": "Coffee Maker", "category": "home_appliances", "price": 80}
]

@app.route('/search/products')
def search_product():
    category = request.args.get('category')

    filtred_products = products

    if category:
        filtred_products = [p for p in filtred_products if p['category'] == category]

    return jsonify(filtred_products)

#GET /search/products?category=electronics&price_min=100&price_max=500

#Creează un API care să gestioneze produse într-un magazin virtual.
# Trebuie să implementezi următoarele rute:

#1. GET `/products`: Returnează lista completă de produse.
#2. POST `/products`: Adaugă un produs nou.
# Fiecare produs trebuie să aibă un `id` unic și un `name`. Returnează produsul creat.
#3. GET `/products/<int:product_id>`: Returnează un produs specific după `id`.
# Dacă produsul nu există, returnează o eroare cu status 404.
#4. PUT `/products/<int:product_id>`: Actualizează un produs specific după `id`.
#Dacă produsul nu există, returnează o eroare 404. Actualizează doar `name`.

# products = [
#     {"id": 1, "name": "Laptop"},
#     {"id": 2, "name": "Telefon"}
# ]

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [product for product in products if product["id"] != product_id]
    return jsonify({"Message": "Product deleted!"})

app.run(debug=True)


# 1. Creează o rută `/operation/<string:op>/<int:num1>/<int:num2>` care să efectueze
# operații matematice simple.
#    - Dacă `op` este `"add"`, returnează suma celor două numere.
#    - Dacă `op` este `"subtract"`, returnează diferența dintre cele două numere.
#    - Dacă `op` este `"multiply"`, returnează produsul.
#    - Dacă `op` este `"divide"`, returnează rezultatul împărțirii.
#    - Dacă operația nu este validă, returnează un mesaj de eroare.