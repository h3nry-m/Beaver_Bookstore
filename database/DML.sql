-- Books
-- get all book info for the Books table 
SELECT * FROM Books;

-- add a new book into the Books table
INSERT INTO Books (title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice) 
VALUES (:titleInput, :firstNameInput, :lastNameInput, :isbnInput, :publisherInput, :publicationYearInput, :newStockInput, :newPriceInput, :usedStockInput, :usedPriceInput);

-- delete a book
DELETE FROM Books WHERE idBook = :book_ID_selected_from_book_table;

-- update a book
UPDATE Books SET title = :titleInput, firstName = :firstNameInput, lastName = :lastNameInput, isbn = :isbnInput, publisher = :publisherInput, publicationYear = :publicationYearInput, newStock = :newStockInput, newPrice = :newPriceInput, usedStock = :usedStockInput, usedPrice = :usedPriceInput
WHERE id= :book_ID_from_the_update_form;

-- Customers
-- get all customer info for the Customers table 
SELECT * FROM Customers; 

-- add a new customer into the Customers table
INSERT INTO Customers (firstName, lastName, email, phoneNumber, addressStreet, addresssCity, addressState, addressZip) 
VALUES (:firstNameInput, :lastNameInput, :emailInput, :phoneNumberInput, :addressStreetInput, :addressCityInput, :addressStateInput, :addressZipInput);

-- delete a customer
DELETE FROM Customers WHERE idCustomer = :customer_ID_selected_from_customer_table;

-- update a customer
UPDATE Customers SET firstName = :firstNameInput, lastName = :lastNameInput, email = :emailInput, phoneNumber = :phoneNumberInput, addressStreet = :addressStreetInput, addressCity = :addressCityInput, addressState = :addressStateInput, addressZip = :addressZipInput
WHERE id= :customer_ID_from_the_update_form;

-- Orders
-- get all orders for the Orders table
SELECT idOrder, firstName, lastName, orderDate, orderTotal, orderType
FROM Orders
INNER JOIN Customers ON Orders.idCustomer = Customers.idCustomer
ORDER BY idOrder ASC;

-- add a new order into the Orders table
INSERT INTO Orders (idCustomer, orderDate, orderTotal, orderType)
VALUES
(:idCustomer,:orderDate, :orderTotal, :orderType);
-- delete a order from the Orders table
DELETE 
FROM 
Orders
WHERE orderID = :orderID_selected_from_browse_orders_page;
-- update a order from the Update table
UPDATE Orders
SET idCustomer = :idCustomerInput,
    orderDate = :orderDateInput,
    orderTotal = :orderTotal,
    orderType = orderType
WHERE orderID = :orderID_selected_from_the_update_form;


--Order_Details
-- get all orders for the Order_Details table
SELECT orderDetailsID, idOrder, idBook, orderQty
FROM OrderDetails;

-- add a new order into the Orders table
INSERT INTO OrderDetails (idOrder, idBook, orderQty)
VALUES
(:idOrder,:idBook, :orderTotal, :orderQty);

-- delete a order from the Orders table
DELETE 
FROM 
OrderDetails
WHERE orderDetailsID = :orderDetailsID_selected_from_browse_orders_page;

-- update a order from the Update table
UPDATE OrderDetails
SET idOrder = :idOrderInput,
    idBook = :idBookInput,
    orderQty = :orderQty,
WHERE orderDetailsID = :orderDetailsID_selected_from_the_update_form;
-- Reviews
-- get all review info for the Reviews table 
SELECT idCustomer, idBook, postTitle, postBody, stars 
FROM Reviews;

-- add a new review into the Reviews table
INSERT INTO Reviews (idCustomer, idBook, postTitle, postBody, stars) 
VALUES (:idCustomer_from_review_table, :idBook_from_review_table, :postTitleInput, :postBodyInput, :starsInput);
-- TODO
-- delete a review (not sure if we have to dis-associate here because technically the review ID will also hold the idBook + idCustomer and there's a CASCADE on delete)
DELETE 
FROM Rewiews 
WHERE idReview = :ID_review_selected_from_review_table;

-- update a review
UPDATE Reviews 
SET idCustomer = :idCustomer_from_review_table, 
    idBook = :idBook_from_review_table, 
    postTitle = :postTitleInput, 
    postBody = :postBodyInput, 
    stars = :starsInput
WHERE id= :ID_review_from_the_update_form;

