from flask import Flask, render_template, json, request
import database.db_connector as db
import os


reviews_from_app_py = []
orders_from_app_py = []

# Configuration
app = Flask(__name__)

# #database connection

db_connection = db.connect_to_database()

# # Routes


@app.route('/books')
def CRUD_books():
    books_from_app_py = [{
        "idBook": 1,
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
        "idBook": 2,
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
        "idBook": 3,
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
    return render_template("books.j2", books=books_from_app_py)


@app.route('/reviews')
def CRUD_reviews():
    reviews_from_app_py = [
        [
            {
                "idReview": 1,
                "idCustomer": 3,
                "idBook": 2,
                "postTitle": "Great Book",
                "postBody": "The best book I've read my entire life",
                "stars": 5
            },
            {
                "idReview": 2,
                "idCustomer": 2,
                "idBook": 3,
                "postTitle": "Mediocre",
                "postBody": "The book was predictable and not very exciting",
                "stars": 3
            },
            {
                "idReview": 3,
                "idCustomer": 4,
                "idBook": 4,
                "postTitle": "Not Bad",
                "postBody": "The character development was not bad but could use work",
                "stars": 4
            }
        ],
        [
            {
                "firstName": "Keith",
                "lastName": "Hazlett"
            },
            {
                "firstName": "Gene",
                "lastName": "Fram"
            },
            {
                "firstName": "Frank",
                "lastName": "Ownens"
            }
        ],
        [
            {
                "title": "Moonwalking with Einstein"
            },
            {
                "title": "Scarlet"
            },
            {
                "title": "The Thousand Autumns of Jacob de Zoet"
            }
        ]
    ]
    return render_template("reviews.j2", reviews=reviews_from_app_py)


@app.route('/orders', methods=["POST", "GET"])
def CRUD_orders():
    if request.method == "GET":
        query = "SELECT idOrder, firstName, lastName, orderDate, orderTotal, orderType FROM Orders INNER JOIN Customers ON Orders.idCustomer = Customers.idCustomer ORDER BY idOrder ASC;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        query2 = "SELECT idCustomer, firstName, lastName FROM Customers"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        customer_data = cursor.fetchall()
        return render_template("orders.j2", orders=results, customers=customer_data)
    # if request.method == "POST":
    #     if request.form.get()
        
@app.route('/customers')
def CRUD_customers():
    customers_from_app_py = [{
        "idCustomer": 1,
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
        "idCustomer": 2,
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
        "idCustomer": 3,
        "firstName": "Keith",
        "lastName": "Hazlett",
        "email": "hazlett_keith3@hotmail.com",
        "phoneNumber": "505-248-2439",
        "addressStreet": "4455 Byrd Lane",
        "addressCity": "Albuquerque",
        "addressState": "New Mexico",
        "addressZip": 87102
    }]
    return render_template("customers.j2", customers=customers_from_app_py)


@app.route('/order_details')
def CRUD_order_details():
    orders_details_from_app_py = [
        [{
            "orderDetailsID": 1,
            "idOrder": 1,
            "idBook": 2,
            "orderQty": 1
        },
        {
            "orderDetailsID": 2,
            "idOrder": 1,
            "idBook": 3,
            "orderQty": 1
        },
        {
            "orderDetailsID": 3,
            "idOrder": 2,
            "idBook": 4,
            "orderQty": 1
        }
        ]
    
    ]
    return render_template("order_details.j2", orderDetails=orders_details_from_app_py)


@app.route('/')
def root():
    return render_template("main.j2")


# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9010)) #9114
    #                                 ^^^^
    #              You can replace this number with any valid port

    app.run(port=port)
