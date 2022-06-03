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

-- Query used to return a specifc book that is inputed through a search bar for the books page
SELECT * FROM Books WHERE MATCH (title, firstName, lastName, isbn, publisher) AGAINST ('{search_query[2:]}' IN NATURAL LANGUAGE MODE)


-- Query used to populate rows with book attributes for the main table on the Books page
SELECT idBook, title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice 
FROM Books;


-- Query used to populate one row for the update form for Books
SELECT * FROM Books WHERE idBook = :idBook;


-- Query used to populate all rows for the main table on the Customer page
SELECT * FROM Customers; 


-- Query used to populate one row for the update form for Customers
SELECT * FROM Customers WHERE idCustomer = '%s';


-- Query used to populate all rows for the main table on the Orders page and is joined to the Customer entity to retrieve first and last name of each customer on an order.
SELECT idOrder, firstName, lastName, orderDate, orderTotal
FROM Orders
INNER JOIN Customers ON Orders.idCustomer = Customers.idCustomer
ORDER BY idOrder ASC;

-- Query used to populate one row for the update form for Orders
SELECT * FROM Orders WHERE idOrder = '%s'

-- Query used to populate all rows for the main table on the orders details page and joins both books and orders table to retrieve the order numbers and title of books.
SELECT orderDetailsID, Orders.idOrder, Books.title, orderType, orderQty, orderPrice, idCoupon, discountedPrice 
FROM OrderDetails 
INNER JOIN Books ON OrderDetails.idBook = Books.idBook 
INNER JOIN Orders ON OrderDetails.idOrder = Orders.idOrder 
ORDER BY orderDetailsID ASC;

-- Query used to populate one row for the main table on the update orders details page.
SELECT * FROM OrderDetails WHERE orderDetailsID = '%s';

-- Query used to populate all rows for the main table on the Reviews page and joins both customers/books table to retrieve first and last name of customer and title of a book.
SELECT idReview, Customers.firstName, Customers.lastName, title, postTitle, postBody, stars 
FROM Reviews
INNER JOIN Customers ON Reviews.idCustomer = Customers.idCustomer
INNER JOIN Books ON Reviews.idBook = Books.idBook
ORDER BY idReview ASC;

-- Query used to populate one row for the main table on the update Reviews page.
SELECT * FROM Reviews WHERE idReview = %s


-- Query used to populate all rows for the main table on the Coupons Page
SELECT * FROM Coupons;



/* 
--------------------------------------------

DROPDOWN WHEEL QUERIES 

---------------------------------------------
*/

-- Query used to display Customer IDs and Names for Dropdown on Orders Table;
SELECT idCustomer, firstName, lastName FROM Customers;

-- Query used to display Order IDs for Dropdown on Order Details 
SELECT idOrder FROM Orders;

-- Query used to display Book Titles corresponding to Book ID for Dropdown on Order Details 
SELECT idBook, title FROM Books;

-- Query used to display Coupon IDs for Dropdown on Order Details 
SELECT idCoupon FROM Coupons;




/* 
----------------------------------------------------------

Create Operations Section

----------------------------------------------------------
*/

-- Query that adds a new book into the Books table
INSERT INTO Books (title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice) 
VALUES (:titleInput, :firstNameInput, :lastNameInput, :isbnInput, :publisherInput, :publicationYearInput, :newStockInput, :newPriceInput, :usedStockInput, :usedPriceInput);


--  Query that adds a new customer into the Customers table
INSERT INTO Customers (firstName, lastName, email, phoneNumber, addressStreet, addresssCity, addressState, addressZip) 
VALUES (:firstNameInput, :lastNameInput, :emailInput, :phoneNumberInput, :addressStreetInput, :addressCityInput, :addressStateInput, :addressZipInput);


--  Query that adds a new order into the Orders table
INSERT INTO Orders (idCustomer, orderDate, orderTotal)
VALUES
(:idCustomer,:orderDate, :orderTotal);


-- Query that adds a new OrderDetails into the OrderDetails table and accounts for a NULL coupon code
INSERT INTO OrderDetails (idOrder, idBook, orderQty, orderType, orderPrice, discountedPrice) 
VALUES 
(:idOrder,:idBook, :orderTotal, :orderQty, :orderType, :orderPrice, :discountedPrice);

-- Query that add a new OrderDetails into the OrderDetails table and accounts for available coupon code
INSERT INTO OrderDetails (idOrder, idBook, orderQty, orderType, orderPrice, idCoupon, discountedPrice)
VALUES
(:idOrder,:idBook, :orderTotal, :orderQty, :orderType, :orderPrice, :idCoupon, :discountedPrice);




--  Query that adds a new review into the Reviews table
INSERT INTO Reviews (idCustomer, idBook, postTitle, postBody, stars) 
VALUES (:idCustomer_from_review_table, :idBook_from_review_table, :postTitleInput, :postBodyInput, :starsInput);

-- Query that adds a new review into the reviews table but accounts for no title
INSERT INTO Reviews (idCustomer, idBook, postBody, stars)
VALUES (idCustomer = :idCustomer_from_review_table, idBook = :idBook_from_review_table, postBody = :postBodyInput, stars = :starsInput);

-- Query that adds a new review into the reviews table but accounts for no body
INSERT INTO Reviews (idCustomer, idBook, postTitle, stars)
VALUES (idCustomer = :idCustomer_from_review_table, idBook = :idBook_from_review_table, postTitle = :postTitleInput, stars = :starsInput);

-- Query that adds a new review into the reviews table but accounts for no body or title
INSERT INTO Reviews (idCustomer, idBook, stars)
VALUES (idCustomer = :idCustomer_from_review_table, idBook = :idBook_from_review_table, stars = :starsInput);




/* 
----------------------------------------------------------

Delete Operations Section

----------------------------------------------------------
*/

-- Query that deletes a book
DELETE FROM Books WHERE idBook = :book_ID_selected_from_book_table;

-- Query that deletes a customer
DELETE FROM Customers WHERE idCustomer = :customer_ID_selected_from_customer_table;

-- Query that deletes a order from the Orders table
DELETE 
FROM 
Orders
WHERE orderID = :orderID_selected_from_browse_orders_page;

-- Query that deletes a order from the Orders table
DELETE 
FROM 
OrderDetails
WHERE orderDetailsID = :orderDetailsID_selected_from_browse_orders_page;


-- Query that deletes a review from the Reviews table
DELETE 
FROM Reviews 
WHERE idReview = :ID_review_selected_from_review_table;


/* 
----------------------------------------------------------

Update Operations Section

----------------------------------------------------------
*/

-- Query that updates a book
UPDATE Books 
SET Books.title = :titleInput, 
Books.firstName = :firstNameInput, 
Books.lastName = :lastNameInput, 
Books.isbn = :isbnInput, 
Books.publisher = :publisherInput, 
Books.publicationYear = :publicationYearInput, 
Books.newStock = :newStockInput, 
Books.newPrice = :newPriceInput, 
Books.usedStock = :usedStockInput, 
Books.usedPrice = :usedPriceInput
WHERE idBook = :book_ID_from_the_update_form;

-- Query that updates a customer
UPDATE Customers 
SET Customers.firstName = :firstNameInput, 
Customers.lastName = :lastNameInput, 
Customers.email = :emailInput, 
Customers.phoneNumber = :phoneNumberInput, 
Customers.addressStreet = :addressStreetInput, 
Customers.addressCity = :addressCityInput, 
Customers.addressState = :addressStateInput, 
Customers.addressZip = :addressZipInput
WHERE idCustomer = :customer_ID_from_the_update_form;

-- Query that updates a order from the Update table
UPDATE Orders
SET idCustomer = :idCustomerInput,
orderDate = :orderDateInput,
orderTotal = :orderTotal
WHERE idOrder = :orderID_selected_from_the_update_form;

-- Query that updates a order from the Update table
UPDATE OrderDetails
SET idOrder = :idOrderInput,
idBook = :idBookInput,
orderQty = :orderQty,
orderType = :orderType,
orderPrice = :orderPrice,
idCoupon = :idCoupon,
discountedPrice = :discountedPrice
WHERE orderDetailsID = :orderDetailsID_selected_from_the_update_form;

-- Query that updates a order without idCoupon for the Update Table
UPDATE OrderDetails
SET idOrder = :idOrderInput,
idBook = :idBookInput,
orderQty = :orderQty,
orderType = :orderType,
orderPrice = :orderPrice,
discountedPrice = :discountedPrice
WHERE orderDetailsID = :orderDetailsID_selected_from_the_update_form;


-- Query that updates a review
UPDATE Reviews 
SET idCustomer = :idCustomer_from_review_table, 
idBook = :idBook_from_review_table, 
postTitle = :postTitleInput, 
postBody = :postBodyInput, 
stars = :starsInput
WHERE idReview= :ID_review_from_the_update_form;


-- Query that updates a review with no title
UPDATE Reviews 
SET idCustomer = :idCustomer_from_review_table, 
idBook = :idBook_from_review_table, 
postBody = :postBodyInput, 
stars = :starsInput
WHERE idReview= :ID_review_from_the_update_form;


-- Query that updates a review with no body

UPDATE Reviews 
SET idCustomer = :idCustomer_from_review_table, 
idBook = :idBook_from_review_table, 
postTitle = :postTitleInput, 
stars = :starsInput
WHERE idReview= :ID_review_from_the_update_form;


-- Query that updates a review with no title or body
UPDATE Reviews 
SET 
idCustomer = idCustomer_from_review_table, 
idBook = :idBook_from_review_table, 
stars = :starsInput
WHERE 
idReview= ID_review_from_the_update_form;
