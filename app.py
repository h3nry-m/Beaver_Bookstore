from flask import Flask, redirect, render_template, json, request
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


@app.route("/books", methods=["GET", "POST"])
def CRUD_books():
    if request.method == "GET":
        query1 = "SELECT idBook, title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice FROM Books;"
        cursor = db.execute_query(db_connection=db_connection, query=query1)
        all_books = cursor.fetchall()

        query2 = "SELECT publisher FROM Books;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        all_publishers = cursor.fetchall()

        return render_template("books.j2", books=all_books, publishers=all_publishers)

    if request.method == "POST":
        if request.form.get("Add_Book"):
            title = request.form["title"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            isbn = request.form["isbn"]
            publisher = request.form["publisher"]
            publicationYear = request.form["publicationYear"]
            newStock = request.form["newStock"]
            newPrice = request.form["newPrice"]
            usedStock = request.form["usedStock"]
            usedPrice = request.form["usedPrice"]
            query = "INSERT INTO Books (title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor = db.execute_query(
                db_connection=db_connection,
                query=query,
                query_params=(
                    title,
                    firstName,
                    lastName,
                    isbn,
                    publisher,
                    publicationYear,
                    newStock,
                    newPrice,
                    usedStock,
                    usedPrice,
                ),
            )
        return redirect("/books")


@app.route("/edit_book/<int:id>", methods=["POST", "GET"])
def edit_book(id):
    if request.method == "GET":
        # to grab the current info of the book
        query = "SELECT * FROM Books WHERE idBook = '%s';"
        cursor = db.execute_query(
            db_connection=db_connection, query=query, query_params=(id,)
        )
        data = cursor.fetchall()

        # to grab the publisher from the dropdown menu
        query2 = "SELECT publisher FROM Books;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        all_publishers = cursor.fetchall()

        return render_template("edit_book.j2", data=data, publishers=all_publishers)

    if request.method == "POST":
        if request.form.get("Edit_Book"):
            title = request.form["title"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            isbn = request.form["isbn"]
            publisher = request.form["publisher"]
            publicationYear = request.form["publicationYear"]
            newStock = request.form["newStock"]
            newPrice = request.form["newPrice"]
            usedStock = request.form["usedStock"]
            usedPrice = request.form["usedPrice"]
            query = "UPDATE Books SET Books.title = %s, Books.firstName = %s, Books.lastName = %s, Books.isbn = %s, Books.publisher = %s, Books.publicationYear = %s, Books.newStock = %s, Books.newPrice = %s, Books.usedStock = %s, Books.usedPrice = %s WHERE Books.idBook = %s;"
            cursor = db.execute_query(
                db_connection=db_connection,
                query=query,
                query_params=(
                    title,
                    firstName,
                    lastName,
                    isbn,
                    publisher,
                    publicationYear,
                    newStock,
                    newPrice,
                    usedStock,
                    usedPrice,
                    id,
                ),
            )
            return redirect("/books")


@app.route("/delete_book/<int:id>")
def delete_book(id):
    query = "DELETE FROM Books WHERE idBook = '%s';"
    cursor = db.execute_query(
        db_connection=db_connection, query=query, query_params=(id,)
    )
    return redirect("/books")


@app.route("/reviews")
def CRUD_reviews():
    if request.method == "GET":
        query = "SELECT idReview, Customers.firstName, Customers.lastName, title, postTitle, postBody, stars \
         FROM Reviews INNER JOIN Customers ON Reviews.idCustomer = Customers.idCustomer INNER JOIN Books ON Reviews.idBook = Books.idBook \
         ORDER BY idReview ASC;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        query2 = "SELECT idCustomer, firstName, lastName FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        customer_data = cursor.fetchall()

        query3 = "SELECT idBook, title FROM Books;"
        cursor = db.execute_query(db_connection=db_connection, query=query3)
        book_data = cursor.fetchall()

    return render_template(
        "reviews.j2", reviews=results, customers=customer_data, books=book_data
    )


@app.route("/orders", methods=["POST", "GET"])
def CRUD_orders():
    if request.method == "GET":
        query = "SELECT idOrder, firstName, lastName, orderDate, orderTotal FROM Orders INNER JOIN Customers ON \
        Orders.idCustomer = Customers.idCustomer ORDER BY idOrder ASC;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        query2 = "SELECT idCustomer, firstName, lastName FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        customer_data = cursor.fetchall()

        return render_template("orders.j2", orders=results, customers=customer_data)
    # if request.method == "POST":
    #     if request.form.get()


@app.route("/customers", methods=["POST", "GET"])
def CRUD_customers():
    if request.method == "GET":
        query = "SELECT * FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        all_customers = cursor.fetchall()
        return render_template("customers.j2", customers=all_customers)

    if request.method == "POST":
        if request.form.get("Add_Customer"):
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phoneNumber = request.form["phoneNumber"]
            addressStreet = request.form["addressStreet"]
            addressState = request.form["addressState"]
            addressZip = request.form["addressZip"]
            query = "INSERT INTO Customers (firstName, lastName, email, phoneNumber, addressStreet, addressState, addressZip) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cursor = db.execute_query(
                db_connection=db_connection,
                query=query,
                query_params=(
                    firstName,
                    lastName,
                    email,
                    phoneNumber,
                    addressStreet,
                    addressState,
                    addressZip,
                ),
            )
            return redirect("/customers")


@app.route("/delete_customer/<int:id>")
def delete_customer(id):
    query = "DELETE FROM Customers WHERE idCustomer = '%s';"
    cursor = db.execute_query(
        db_connection=db_connection, query=query, query_params=(id,)
    )
    return redirect("/customers")


@app.route("/order_details")

@app.route('/order_details', methods=["POST", "GET"])
def CRUD_order_details():
    if request.method == "GET":
        query = "SELECT orderDetailsID, Orders.idOrder, Books.title, orderType, orderQty, orderPrice, idCoupon, discountedPrice FROM OrderDetails \
        INNER JOIN Books ON OrderDetails.idBook = Books.idBook INNER JOIN Orders ON OrderDetails.idOrder = Orders.idOrder ORDER BY orderDetailsID ASC;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

        query2 = "SELECT idOrder FROM Orders;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        order_data = cursor.fetchall()

        query3 = "SELECT idBook, title FROM Books;"
        cursor = db.execute_query(db_connection=db_connection, query=query3)
        book_data = cursor.fetchall()

        query4 = "SELECT idCoupon FROM Coupons;"
        cursor = db.execute_query(db_connection=db_connection, query=query4)
        coupon_data = cursor.fetchall()
        return render_template(
            "order_details.j2",
            orderDetails=results,
            orders=order_data,
            books=book_data,
            coupons=coupon_data,
        )

    elif request.method == "POST":
        if request.form.get("Add_Order_Details"):
            idOrder = request.form["idOrder"]
            idBook = request.form["idBook"]
            orderType = request.form["orderType"]
            orderQty = request.form["orderQty"]
            orderPrice = request.form["orderPrice"]
            idCoupon = request.form["idCoupon"]
            discountedPrice = request.form["discountedPrice"]
            if idCoupon == '0':
                query = "INSERT INTO OrderDetails (idOrder, idBook, orderQty, orderType, orderPrice, discountedPrice) VALUES (%s, %s, %s, %s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(idOrder, idBook, orderQty, orderType, orderPrice, discountedPrice))
                db_connection.commit()
            else:
                query = "INSERT INTO OrderDetails (idOrder, idBook, orderQty, orderType, orderPrice, idCoupon, discountedPrice) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(idOrder, idBook, orderQty, orderType, orderPrice, idCoupon, discountedPrice))
                db_connection.commit()
            return redirect('/order_details')
    return render_template("order_details.j2", orderDetails=results, orders=order_data, books = book_data, coupons = coupon_data)

@app.route("/coupons")
def CRUD_coupons():
    if request.method == "GET":
        query = "SELECT * FROM Coupons"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()

    return render_template("coupons.j2", coupons=results)


@app.route("/")
def root():
    return render_template("main.j2")


# Listener
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9013))  # 9114
    #                                 ^^^^
    #              You can replace this number with any valid port

    app.run(host="flip1.engr.oregonstate.edu", port=port, debug=True)
