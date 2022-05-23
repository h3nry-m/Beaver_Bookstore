/* 
----------------------------------------------------------


Sample Database Manipulation queries for Beaver Bookstore


----------------------------------------------------------
*/




/* 
----------------------------------------------------------

Read Operations Section

----------------------------------------------------------
*/

-- Query used to populate all rows for the main table on the Books page
SELECT idBook, title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice 
FROM Books;

-- Display Customers
SELECT * FROM Customers; 


-- Query used to populate all rows for the main table on the Coupons Page
SELECT * FROM Coupons;


-- Query used to populate all rows for the main table on the Orders page
SELECT idOrder, firstName, lastName, orderDate, orderTotal
FROM Orders
INNER JOIN Customers ON Orders.idCustomer = Customers.idCustomer
ORDER BY idOrder ASC;


-- Query used to populate all rows for the main table on the orders page and substitutes foreign key IDs for titles and names
SELECT orderDetailsID, Orders.idOrder, Books.title, orderType, orderQty, orderPrice, idCoupon, discountedPrice 
FROM OrderDetails 
INNER JOIN Books ON OrderDetails.idBook = Books.idBook 
INNER JOIN Orders ON OrderDetails.idOrder = Orders.idOrder 
ORDER BY orderDetailsID ASC;


-- Query used to populate all rows for the main table on the Reviews page and substitutes foreign key IDs for customers and titles of books
SELECT idReview, Customers.firstName, Customers.lastName, title, postTitle, postBody, stars 
FROM Reviews
INNER JOIN Customers ON Reviews.idCustomer = Customers.idCustomer
INNER JOIN Books ON Reviews.idBook = Books.idBook
ORDER BY idReview ASC;

/* 
--------------------------------------------

DROPDOWN WHEEL AND UPDATE POPULATION QUERIES 

---------------------------------------------
*/

-- Display Customer IDs and Names for Dropdown on Orders Table;
SELECT idCustomer, firstName, lastName FROM Customers;
-- Display Order IDs for Dropdown on Order Details 
SELECT idOrder FROM Orders;
-- Display Book Titles corresponding to Book ID for Dropdown on Order Details 
SELECT idBook, title FROM Books;
-- Display Coupon IDs for Dropdown on Order Details 
SELECT idCoupon FROM Coupons;



-- Query used to populate one row for the update form for Books
SELECT * FROM Books WHERE idBook = :idBook;





/* 
----------------------------------------------------------

Create Operations Section

----------------------------------------------------------
*/

-- add a new book into the Books table
INSERT INTO Books (title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice) 
VALUES (:titleInput, :firstNameInput, :lastNameInput, :isbnInput, :publisherInput, :publicationYearInput, :newStockInput, :newPriceInput, :usedStockInput, :usedPriceInput);


-- add a new customer into the Customers table
INSERT INTO Customers (firstName, lastName, email, phoneNumber, addressStreet, addresssCity, addressState, addressZip) 
VALUES (:firstNameInput, :lastNameInput, :emailInput, :phoneNumberInput, :addressStreetInput, :addressCityInput, :addressStateInput, :addressZipInput);


-- add a new order into the Orders table
INSERT INTO Orders (idCustomer, orderDate, orderTotal)
VALUES
(:idCustomer,:orderDate, :orderTotal);


-- Query that adds a new OrderDetails into the OrderDetails table and accounts for a user inputs a NULL for coupon code
INSERT INTO OrderDetails (idOrder, idBook, orderQty, orderType, orderPrice, discountedPrice) 
VALUES 
(:idOrder,:idBook, :orderTotal, :orderQty, :orderType, :orderPrice, :discountedPrice);

-- Query that add a new OrderDetails into the OrderDetails table and accounts for available coupon code
INSERT INTO OrderDetails (idOrder, idBook, orderQty, orderType, orderPrice, idCoupon, discountedPrice)
VALUES
(:idOrder,:idBook, :orderTotal, :orderQty, :orderType, :orderPrice, :idCoupon, :discountedPrice);


-- add a new review into the Reviews table
INSERT INTO Reviews (idCustomer, idBook, postTitle, postBody, stars) 
VALUES (:idCustomer_from_review_table, :idBook_from_review_table, :postTitleInput, :postBodyInput, :starsInput);


-- add a new coupon into the Coupons table
INSERT INTO Coupons (expirationDate, discountCode, discountPercent)
VALUES (:expirationDateInput, :discountCodeInput, :discountPercentInput)


/* 
----------------------------------------------------------

Delete Operations Section

----------------------------------------------------------
*/

-- delete a book
DELETE FROM Books WHERE idBook = :book_ID_selected_from_book_table;

-- delete a customer
DELETE FROM Customers WHERE idCustomer = :customer_ID_selected_from_customer_table;

-- delete a order from the Orders table
DELETE 
FROM 
Orders
WHERE orderID = :orderID_selected_from_browse_orders_page;

-- delete a order from the Orders table
DELETE 
FROM 
OrderDetails
WHERE orderDetailsID = :orderDetailsID_selected_from_browse_orders_page;

-- TODO
-- delete a review (not sure if we have to dis-associate here because technically the review ID will also hold the idBook + idCustomer and there's a CASCADE on delete)
DELETE 
FROM Rewiews 
WHERE idReview = :ID_review_selected_from_review_table;

-- delete a coupon from the Coupons table
DELETE 
FROM Coupons 
WHERE idCoupon = :couponID_selected_from_coupons_page;


/* 
----------------------------------------------------------

Update Operations Section

----------------------------------------------------------
*/

-- update a book
UPDATE Books 
SET title = :titleInput, 
firstName = :firstNameInput, 
lastName = :lastNameInput, 
isbn = :isbnInput, 
publisher = :publisherInput, 
publicationYear = :publicationYearInput, 
newStock = :newStockInput, 
newPrice = :newPriceInput, 
usedStock = :usedStockInput, 
usedPrice = :usedPriceInput
WHERE id= :book_ID_from_the_update_form;

-- update a customer
UPDATE Customers 
SET firstName = :firstNameInput, 
lastName = :lastNameInput, 
email = :emailInput, 
phoneNumber = :phoneNumberInput, 
addressStreet = :addressStreetInput, 
addressCity = :addressCityInput, 
addressState = :addressStateInput, 
addressZip = :addressZipInput
WHERE id= :customer_ID_from_the_update_form;

-- update a order from the Update table
UPDATE Orders
SET idCustomer = :idCustomerInput,
orderDate = :orderDateInput,
orderTotal = :orderTotal
WHERE idOrder = :orderID_selected_from_the_update_form;

-- update a order from the Update table
UPDATE OrderDetails
SET idOrder = :idOrderInput,
idBook = :idBookInput,
orderQty = :orderQty,
orderType = :orderType,
orderPrice = :orderPrice,
idCoupon = :idCoupon,
discountedPrice = :discountedPrice
WHERE orderDetailsID = :orderDetailsID_selected_from_the_update_form;

-- update a review
UPDATE Reviews 
SET idCustomer = :idCustomer_from_review_table, 
idBook = :idBook_from_review_table, 
postTitle = :postTitleInput, 
postBody = :postBodyInput, 
stars = :starsInput
WHERE id= :ID_review_from_the_update_form;

-- update a coupon
UPDATE Coupon 
SET expirationDate = :expirationDateInput, 
discountCode = :discountCodeInput, 
discountPercent= :discountPercentInput
WHERE id = :couponID_from_the_update_form;
