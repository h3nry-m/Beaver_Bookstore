from flask import Flask, render_template, json, request
import database.db_connector as db
import os


reviews_from_app_py = []
orders_from_app_py = []

# Configuration
app = Flask(__name__)

# #database connection

db_connection = db.connect_to_database()
db_connection.ping(True)
# # Routes


@app.route('/books', methods=["GET", "POST"])
def CRUD_books():
    if request.method == "GET":
        query = "SELECT * FROM Books;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        all_books = cursor.fetchall()
        return render_template("books.j2", books=all_books)
    
    # does not currently work
    if request.method == "POST":
        if request.form.get("Add_Book"):
            title = request.form['title']
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            isbn = request.form['isbn']
            publisher = request.form['publisher']
            publicationYear = request.form['publicationYear']
            newStock = request.form['publicationYear']
            newPrice = request.form['newPrice']
            usedStock = request.form['usedStock']
            usedPrice = request.form['usedPrice']
            query = "INSERT INTO Books (title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor = mysql.connection.cursor()
            cursor.execute(query, (title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice))
            mysql.connection.commit()
            print('title', title)
            print('firstname', firstName)
        return redirect("/books")

# does not currently work. not sure yet if want to do edit in a separate page or use a function
@app.route("/edit_book/<int:id>", methods = ["POST", "GET"])
def edit_book(id):
    if request.method == "GET":
        # to grab the current info of the book
        query = ""
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # to grab the publisher from the dropdown menu
        query2 = ""
        cur = mysql.connection.cursor()
        cur.execute(query)
        publisher_data = cur.fetchall()

        return render_template("", data = data, publisher_data = publisher_data)

@app.route('/reviews')
def CRUD_reviews():
    if request.method == "GET":
        query = "SELECT idReview, Customers.firstName, Customers.lastName, title, postTitle, postBody, stars FROM Reviews INNER JOIN Customers ON Reviews.idCustomer = Customers.idCustomer INNER JOIN Books ON Reviews.idBook = Books.idBook ORDER BY idReview ASC;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        query2 = "SELECT idCustomer, firstName, lastName FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        customer_data = cursor.fetchall()

        query3 = "SELECT idBook, title FROM Books;"
        cursor = db.execute_query(db_connection=db_connection, query=query3)
        book_data = cursor.fetchall()

    return render_template("reviews.j2", reviews=results, customers=customer_data, books=book_data)


@app.route('/orders', methods=["POST", "GET"])
def CRUD_orders():
    if request.method == "GET":
        query = "SELECT idOrder, firstName, lastName, orderDate, orderTotal FROM Orders INNER JOIN Customers ON Orders.idCustomer = Customers.idCustomer ORDER BY idOrder ASC;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        query2 = "SELECT idCustomer, firstName, lastName FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        customer_data = cursor.fetchall()

        return render_template("orders.j2", orders=results, customers=customer_data)
    # if request.method == "POST":
    #     if request.form.get()
        
@app.route('/customers')
def CRUD_customers():
    # customers_from_app_py = [{
    #     "idCustomer": 1,
    #     "firstName": "Cara",
    #     "lastName": "Jacob",
    #     "email": "cara.jacob9@hotmail.com",
    #     "phoneNumber": "954-616-7898",
    #     "addressStreet": "667 Kenwood Place",
    #     "addressCity": "Fort Lauderdale",
    #     "addressState": "Florida",
    #     "addressZip": 33301
    # },
    #     {
    #     "idCustomer": 2,
    #     "firstName": "Gene",
    #     "lastName": "Fram",
    #     "email": "gene_fram7@hotmail.com",
    #     "phoneNumber": "612-775-0456",
    #     "addressStreet": "2128 Jewell Road",
    #     "addressCity": "Minneapolis",
    #     "addressState": "Minnesota",
    #     "addressZip": 55402
    # },
    #     {
    #     "idCustomer": 3,
    #     "firstName": "Keith",
    #     "lastName": "Hazlett",
    #     "email": "hazlett_keith3@hotmail.com",
    #     "phoneNumber": "505-248-2439",
    #     "addressStreet": "4455 Byrd Lane",
    #     "addressCity": "Albuquerque",
    #     "addressState": "New Mexico",
    #     "addressZip": 87102
    # }]
    if request.method == "GET":
        query = "SELECT * FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        all_customers = cursor.fetchall()
        return render_template("customers.j2", customers=all_customers)


@app.route('/order_details')
def CRUD_order_details():
    if request.method == "GET":
        query = "SELECT orderDetailsID, Orders.idOrder, Books.title, orderQty FROM OrderDetails INNER JOIN Books ON OrderDetails.idBook = Books.idBook INNER JOIN Orders ON OrderDetails.idOrder = Orders.idOrder ORDER BY orderDetailsID ASC;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        query2 = "SELECT idOrder FROM Orders;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        order_data = cursor.fetchall()

        query3 = "SELECT idBook, title FROM Books;"
        cursor = db.execute_query(db_connection=db_connection, query=query3)
        book_data = cursor.fetchall()
    return render_template("order_details.j2", orderDetails=results, orders=order_data, books = book_data)

@app.route('/coupons')
def CRUD_coupons():
    # if request.method == "GET":
    #     query = ""
    #     cursor = db.execute_query(db_connection=db_connection, query=query)
    #     results = cursor.fetchall()

    return render_template("coupons.j2" )


@app.route('/')
def root():
    return render_template("main.j2")


# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9011)) #9114
    #                                 ^^^^
    #              You can replace this number with any valid port

    app.run(host="flip2.engr.oregonstate.edu", port=port, debug = False)
