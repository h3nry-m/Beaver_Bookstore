from flask import Flask, render_template
import os




reviews_from_app_py = []
orders_from_app_py = []

# Configuration
app = Flask(__name__)

# Routes 
@app.route('/books')
def CRUD_books():
    books_from_app_py =[{
    "title": "Euphoria",
    "firstName": "Lily",
    "lastName": "King",
    "isbn": "978-0-80-212255-1",
    "publisher": "Atlantic Monthly Press",
    "publicationYear": 2014,
    "newStock": 3,
    "newPrice": 11.70,
    "usedStock": 4,
    "usedPrice": 5.31},
    {
    "title": "Moonwalking with Einstein",
    "firstName": "Joshua",
    "lastName": "Foer",
    "isbn": "978-1-59-420229-2",
    "publisher": "The Penguin Press",
    "publicationYear": 2011,
    "newStock": 5,
    "newPrice": 9.79,
    "usedStock": 7,
    "usedPrice": 5.90},
    {
    "title": "Scarlet",
    "firstName": "Marissa",
    "lastName": "Meyer",
    "isbn": "978-1-25-000721-6",
    "publisher": "Square Fish",
    "publicationYear": 2013,
    "newStock": 2,
    "newPrice": 9.89,
    "usedStock": 6,
    "usedPrice": 4.84
}]
    return render_template("books.j2", books = books_from_app_py)

@app.route('/reviews')
def CRUD_reviews():
    return render_template("reviews.j2", reviews = reviews_from_app_py)

@app.route('/orders')
def CRUD_orders():
    orders_from_app_py = [
        [
            {
                "idOrder": 1,
                "firstName": "Gene",
                "lastName": "Fram",
                "orderDate": "2022-03-18",
                "orderTotal": 19.68,
                "orderType": "purchase" 
            },
            {
                "idOrder": 2,
                "firstName": "Jared",
                "lastName": "Collazo",
                "orderDate": "2022-01-02",
                "orderTotal": 22.68,
                "orderType": "purchase" 
            },
            {
                "idOrder": 3,
                "firstName": "Keith",
                "lastName": "Hazlett",
                "orderDate": "2022-02-16",
                "orderTotal": 11.70,
                "orderType": "purchase" 
            },
            {
                "idOrder": 4,
                "firstName": "Cara",
                "lastName": "Jacob",
                "orderDate": "2022-04-20",
                "orderTotal": 5.90,
                "orderType": "sale" 
            }
        ],
        [
            {
                "firstName": "Frank",
                "lastName": "Owens"
            },
            {
                "firstName": "Ethan",
                "lastName": "Lopez"
            }
        ]
    ]
    return render_template("orders.j2", orders = orders_from_app_py)

@app.route('/customers')
def CRUD_customers():
    customers_from_app_py = [{
    "firstName": "Cara",
    "lastName": "Jacob",
    "email": "cara.jacob9@hotmail.com",
    "phoneNumber": "954-616-7898",
    "addressStreet": "667 Kenwood Place",
    "addressCity": "Fort Lauderdale",
    "addressState": "Florida",
    "addressZip": 33301
    },
    {
    "firstName": "Gene",
    "lastName": "Fram",
    "email": "gene_fram7@hotmail.com",
    "phoneNumber": "612-775-0456",
    "addressStreet": "2128 Jewell Road",
    "addressCity": "Minneapolis",
    "addressState": "Minnesota",
    "addressZip": 55402
    },
    {
    "firstName": "Keith",
    "lastName": "Hazlett",
    "email": "hazlett_keith3@hotmail.com",
    "phoneNumber": "505-248-2439",
    "addressStreet": "4455 Byrd Lane",
    "addressCity": "Albuquerque",
    "addressState": "New Mexico",
    "addressZip": 87102
    }]
    return render_template("customers.j2", customers = customers_from_app_py)

@app.route('/')
def root():
    return render_template("main.j2")

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9113)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port) 