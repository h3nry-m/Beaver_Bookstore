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
###################################################################################
#                                                                                 #  
#                                                                                 #   
#                                   Books                                         #   
#                                                                                 #   
#                                                                                 #   
###################################################################################
@app.route("/books", methods=["GET", "POST"])
def create_read_books():
    if request.method == "GET":
        search_query = request.query_string.decode() 
        if search_query: 
            query = f"SELECT * FROM Books WHERE MATCH (title, firstName, lastName, isbn, publisher) AGAINST ('{search_query[2:]}' IN NATURAL LANGUAGE MODE);"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            books_data = cursor.fetchall()

        else:
            query1 = "SELECT idBook, title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice FROM Books;"
            cursor = db.execute_query(db_connection=db_connection, query=query1)
            books_data = cursor.fetchall()
        return render_template("books.j2", books=books_data)

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

        return render_template("edit_templates/edit_book.j2", data=data)

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


###################################################################################
#                                                                                 #  
#                                                                                 #   
#                                   Reviews                                       #   
#                                                                                 #   
#                                                                                 #   
###################################################################################
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
    elif request.method == "POST":
        if request.form.get("Add_Review"):

            idCustomer = request.form["idCustomer"]
            idBook = request.form["idBook"]
            postTitle = request.form["postTitle"]
            postBody = request.form["postBody"]
            stars = request.form["stars"]
            if postTitle == '' and postBody == '':
                query = "INSERT INTO Reviews (idCustomer, idBook, stars) \
                VALUES (%s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, idBook, stars))
                db_connection.commit()
            elif postTitle == '':
                query = "INSERT INTO Reviews (idCustomer, idBook, postBody, stars) \
                VALUES (%s, %s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, idBook, postBody, stars))
                db_connection.commit()
            elif postBody == '':
                query = "INSERT INTO Reviews (idCustomer, idBook, postTitle, stars) \
                VALUES (%s, %s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, idBook, postTitle, stars))
                db_connection.commit()
            else:
                query = "INSERT INTO Reviews (idCustomer, idBook, postTitle, postBody, stars) \
                VALUES (%s, %s, %s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, idBook, postTitle, postBody, stars))
                db_connection.commit()
            return redirect("/reviews")
    return render_template("reviews.j2", reviews=results, customers=customer_data, books=book_data)

@app.route("/delete_reviews/<int:idReview>")
def delete_review(idReview):
    query = "DELETE FROM Reviews WHERE idReview = %s;"
    cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(idReview,) )
    db_connection.commit()
    return redirect('/reviews')

@app.route("/edit_reviews/<int:idReview>", methods=["POST", "GET"])
def edit_revieW(idReview):
    if request.method == "GET":
        query = "SELECT * FROM Reviews WHERE idReview = %s"
        cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(idReview,) )
        results = cursor.fetchall()

        query2 = "SELECT idCustomer, firstName, lastName FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        customer_data = cursor.fetchall()

        query3 = "SELECT idBook, title FROM Books;"
        cursor = db.execute_query(db_connection=db_connection, query=query3)
        book_data = cursor.fetchall()
    elif request.method == "POST":
        if request.form.get("Edit_Reviews"):

            idCustomer = request.form["idCustomer"]
            idBook = request.form["idBook"]
            postTitle = request.form["postTitle"]
            postBody = request.form["postBody"]
            stars = request.form["stars"]

            if postTitle == '' and postBody == '':
                query = "UPDATE Reviews SET idCustomer = %s, idBook = %s, stars = %s WHERE idReview= %s;"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, idBook, stars, idReview))
                db_connection.commit()
            elif postTitle == '':
                query = "UPDATE Reviews SET idCustomer = %s, idBook = %s, postBody = %s, stars = %s WHERE idReview= %s;"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, idBook, postBody, stars, idReview))
                db_connection.commit()
            elif postBody == '':
                query = "UPDATE Reviews SET idCustomer = %s, idBook = %s, postTitle = %s, stars = %s WHERE idReview= %s;"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, idBook, postTitle, stars, idReview))
                db_connection.commit()
            else:
                query = "UPDATE Reviews SET idCustomer = %s, idBook = %s, postTitle = %s, postBody = %s, stars = %s WHERE idReview= %s;"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, idBook, postTitle, postBody, stars, idReview))
                db_connection.commit()

            return redirect("/reviews")
    return render_template("edit_templates/edit_reviews.j2", results=results, customer_info=customer_data, book_data=book_data )



###################################################################################
#                                                                                 #  
#                                                                                 #   
#                                   Orders                                        #   
#                                                                                 #   
#                                                                                 #   
###################################################################################
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
    elif request.method == "POST":
        if request.form.get("Add_Order"):

            idCustomer = request.form["fullName"]
            orderDate = request.form["orderDate"]
            orderTotal = request.form["orderTotal"]

            query = "INSERT INTO Orders (idCustomer, orderDate, orderTotal) VALUES (%s, %s, %s);"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, orderDate, orderTotal))
            db_connection.commit()
            return redirect("/orders")
    return render_template("orders.j2", orders=results, customers=customer_data)

@app.route("/delete_orders/<int:idOrder>")
def delete_order(idOrder):
    query = "DELETE FROM Orders WHERE idOrder = %s;"
    cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(idOrder,) )
    db_connection.commit()
    return redirect('/orders')

@app.route("/edit_orders/<int:idOrder>", methods={"POST", "GET"})
def edit_order(idOrder):
    if request.method == "GET":
        query = "SELECT * FROM Orders WHERE idOrder = '%s'"
        cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(idOrder,))
        results = cursor.fetchall()

        query2 = "SELECT idCustomer, firstName, lastName FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query = query2)
        customer_info = cursor.fetchall()
    if request.method == "POST":
        if request.form.get("Edit_Orders"):

            idCustomer = request.form['idCustomer']
            orderDate = request.form['orderDate']
            orderTotal = request.form['orderTotal']

            query = "UPDATE Orders SET idCustomer = %s, orderDate = %s, orderTotal = %s WHERE idOrder = %s;"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idCustomer, orderDate, orderTotal, idOrder))
            return redirect("/orders")
    return render_template("edit_templates/edit_orders.j2", results=results, customer_info=customer_info )


###################################################################################
#                                                                                 #  
#                                                                                 #   
#                                   Customers                                     #   
#                                                                                 #   
#                                                                                 #   
###################################################################################
@app.route("/customers", methods=["POST", "GET"])
def create_read_customers():
    if request.method == "GET":
        search_query = request.query_string.decode() 
        if search_query: 
            query = f"SELECT * FROM Customers WHERE MATCH (firstName, lastName, email, phoneNumber, addressStreet, addressCity, addressState, addressZip) AGAINST ('{search_query[2:]}' IN NATURAL LANGUAGE MODE);"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            customers_data = cursor.fetchall()
        else:
            query = "SELECT * FROM Customers;"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            customers_data = cursor.fetchall()
        return render_template("customers.j2", customers=customers_data)

    if request.method == "POST":
        if request.form.get("Add_Customer"):
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phoneNumber = request.form["phoneNumber"]
            addressStreet = request.form["addressStreet"]
            addressCity = request.form["addressCity"]
            addressState = request.form["addressState"]
            addressZip = request.form["addressZip"]
            print(f'addresStreet and city {addressStreet} and {addressCity}')
            query = "INSERT INTO Customers (firstName, lastName, email, phoneNumber, addressStreet, addressCity, addressState, addressZip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            cursor = db.execute_query(
                db_connection=db_connection,
                query=query,
                query_params=(
                    firstName,
                    lastName,
                    email,
                    phoneNumber,
                    addressStreet,
                    addressCity,
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

@app.route("/edit_customer/<int:id>", methods=["POST", "GET"])
def edit_customer(id):
    if request.method == "GET":
        # to grab the current info of the book
        query = "SELECT * FROM Customers WHERE idCustomer = '%s';"
        cursor = db.execute_query(
            db_connection=db_connection, query=query, query_params=(id,)
        )
        data = cursor.fetchall()

        return render_template("edit_templates/edit_customer.j2", data=data)

    if request.method == "POST":
        if request.form.get("Edit_Customer"):
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            email = request.form["email"]
            phoneNumber = request.form["phoneNumber"]
            addressStreet = request.form["addressStreet"]
            addressCity = request.form["addressCity"]
            addressState = request.form["addressState"]
            addressZip = request.form["addressZip"]
            query = "UPDATE Customers SET Customers.firstName = %s, Customers.lastName = %s, Customers.email = %s, Customers.phoneNumber = %s, Customers.addressStreet = %s, Customers.addressCity = %s, Customers.addressState = %s, Customers.addressZip = %s WHERE Customers.idCustomer = %s;"
            cursor = db.execute_query(
            db_connection=db_connection,
            query=query,
            query_params=(
                firstName,
                lastName,
                email,
                phoneNumber,
                addressStreet,
                addressCity,
                addressState,
                addressZip,
                id,
            ),
        )
        return redirect("/customers")


###################################################################################
#                                                                                 #  
#                                                                                 #   
#                                   Order Details                                 #   
#                                                                                 #   
#                                                                                 #   
###################################################################################
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

@app.route('/delete_order_details/<int:orderDetailsID>', methods=["GET", "DELETE"])
def delete_order_details(orderDetailsID):
    # table_info = {   
    #         'page-title': 'Order Details',
    #         'table-header': ['Order-Details ID', 'Order ID', 'Book Title', 'Order Type', 'Order Quantity', 'Order Price', 'Coupon ID', 'Discounted Price']
    #         }
        
    # if request.method == "GET":
    #     query = "SELECT orderDetailsID, Orders.idOrder, Books.title, orderType, orderQty, orderPrice, idCoupon, discountedPrice FROM OrderDetails \
    #     INNER JOIN Books ON OrderDetails.idBook = Books.idBook INNER JOIN Orders ON OrderDetails.idOrder = Orders.idOrder WHERE OrderDetails.orderDetailsID = %s ORDER BY orderDetailsID ASC;"
    #     cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(orderDetailsID,))
    #     results = cursor.fetchall()

    # elif request.method == "DELETE":
    #     if request.form.get("Delete_Order_Details"):
    #         query = "DELETE FROM OrderDetails WHERE orderDetailsID = %s;"
    #         cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(orderDetailsID,) )
    #         db_connection.commit()
    #         return redirect('/order_details')
    query = "DELETE FROM OrderDetails WHERE orderDetailsID = %s;"
    cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(orderDetailsID,) )
    db_connection.commit()
    return redirect('/order_details')
    # return render_template("delete_temp.j2", table_header=table_info, delete_info=results)

@app.route('/edit_order_details/<int:orderDetailsID>', methods=["POST", "GET"])
def edit_order_details(orderDetailsID):
    if request.method == "GET":
        query = "SELECT * FROM OrderDetails WHERE orderDetailsID = '%s'"
        cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(orderDetailsID,))
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
    elif request.method == "POST":
        if request.form.get("Edit_Order_Details"):

            idOrder = request.form['idOrder']
            idBook = request.form['idBook']
            orderType = request.form['orderType']
            orderQty = request.form['orderQty']
            orderPrice = request.form['orderPrice']
            idCoupon = request.form['idCoupon']
            discountedPrice = request.form['discountedPrice']

            if idCoupon == '0':
                query = "UPDATE OrderDetails SET \
                idOrder = %s, idBook = %s, orderType = %s, orderQty = %s, orderPrice = %s, idCoupon = NULL, discountedPrice = %s WHERE orderDetailsID = %s;"
                cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(idOrder, idBook, orderType, orderQty, orderPrice, discountedPrice, orderDetailsID))
                db_connection.commit()
            else:
                query =  "UPDATE OrderDetails SET \
                idOrder = %s, idBook = %s, orderType = %s, orderQty = %s, orderPrice = %s, idCoupon = %s, discountedPrice = %s WHERE orderDetailsID = %s;"
                cursor = db.execute_query(db_connection=db_connection, query = query, query_params=(idOrder, idBook, orderType, orderQty, orderPrice, idCoupon, discountedPrice, orderDetailsID))
                db_connection.commit()
            return redirect("/order_details")
    return render_template("edit_templates/edit_order_details.j2", results=results, orders=order_data, books = book_data, coupons = coupon_data )


###################################################################################
#                                                                                 #  
#                                                                                 #   
#                                   Coupons                                       #   
#                                                                                 #   
#                                                                                 #   
###################################################################################
@app.route('/coupons')
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
    port = int(os.environ.get("PORT", 9012))  # 9114
    #                                 ^^^^
    #              You can replace this number with any valid port

    app.run(host="flip1.engr.oregonstate.edu", port=port, debug=True)
