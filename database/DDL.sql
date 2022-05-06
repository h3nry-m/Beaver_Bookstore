SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;


DROP TABLE IF EXISTS `Customers`;
DROP TABLE IF EXISTS `Orders`;
DROP TABLE IF EXISTS `Books`;
DROP TABLE IF EXISTS `OrderDetails`;
DROP TABLE IF EXISTS `Reviews`;

-- -----------------------------------------------------
-- Table Customers
-- -----------------------------------------------------
CREATE TABLE Customers (
    idCustomer INT NOT NULL UNIQUE AUTO_INCREMENT,
    firstName VARCHAR(45) NOT NULL,
    lastName VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    phoneNumber VARCHAR(45) NOT NULL,
    addressStreet VARCHAR(45) NOT NULL,
    addresssCity VARCHAR(45) NOT NULL,
    addressState VARCHAR(45) NOT NULL,
    addressZip VARCHAR(10) NOT NULL,
    PRIMARY KEY (idCustomer)
);

-- -----------------------------------------------------
-- Table Books
-- -----------------------------------------------------
CREATE TABLE Books (
    idBook INT NOT NULL UNIQUE AUTO_INCREMENT,
    title VARCHAR(45) NOT NULL,
    firstName VARCHAR(45) NOT NULL,
    lastName VARCHAR(45) NOT NULL,
    isbn VARCHAR(17) NOT NULL,
    publisher VARCHAR(45) NOT NULL,
    publicationYear SMALLINT(2) NOT NULL,
    newStock INT NOT NULL,
    newPrice DECIMAL(5,2) NOT NULL,
    usedStock INT NOT NULL,
    usedPrice DECIMAL(5,2) NOT NULL,
    PRIMARY KEY(idBook)
);

-- -----------------------------------------------------
-- Table Orders
-- -----------------------------------------------------
CREATE TABLE Orders (
    idOrder INT NOT NULL UNIQUE AUTO_INCREMENT,
    idCustomer INT,
    orderDate DATE,
    orderType VARCHAR(8) NOT NULL CHECK (orderType IN ('sale', 'purchase'))
    orderTotal DECIMAL(8,2),
    PRIMARY KEY (idOrder),
    FOREIGN KEY (idCustomer) REFERENCES Customers (idCustomer)
);

-- -----------------------------------------------------
-- Intersecting Table OrderDetails
-- -----------------------------------------------------
CREATE TABLE OrderDetails (
    orderDetailsID INT NOT NULL UNIQUE AUTO_INCREMENT,
    idOrder INT,
    idBook INT,
    orderQty INT,
    PRIMARY KEY (orderDetailsID),
    FOREIGN KEY (idOrder) REFERENCES Orders (idOrder),
    FOREIGN KEY (idBook) REFERENCES Books (idBook)
);

-- -----------------------------------------------------
-- Intersecting Table Reviews
-- -----------------------------------------------------

Create TABLE Reviews (
    idReview INT NOT NULL UNIQUE AUTO_INCREMENT,
    idCustomer INT,
    idBook INT,
    postTitle VARCHAR(45),
    postBody TEXT(1000),
    stars TINYINT(5) NOT NULL,
    PRIMARY KEY (idReview),
    FOREIGN KEY (idCustomer) REFERENCES Customers (idCustomer),
    FOREIGN KEY (idBook) REFERENCES Books (idBook)
);


INSERT INTO Customers (firstName, lastName, email, phoneNumber, addressStreet, addresssCity, addressState, addressZip)
VALUE
('Cara', 'Jacob', 'cara.jacob9@hotmail.com', '954-616-7898', '667 Kenwood Place','Fort Lauderdale', 'Florida', '33301'),
('Gene', 'Fram', 'gene_fram7@hotmail.com', '612-775-0456', '2128 Jewell Road', 'Minneapolis', 'Minnesota', '55402'),
('Keith', 'Hazlett', 'hazlett_keith3@hotmail.com', '505-248-2439', '4455 Byrd Lane', 'Albuquerque', 'New Mexico', '87102'),
('Frank', 'Owens', 'frank_owens2@hotmail.com','412-280-7116', '4938 Jacobs Street', 'Pittsburgh','Pennsylvania','15222'),
('Jared', 'Collazo', 'jard.collaz@hotmail.com', '714-201-2358', '3593 Half and Half Drive', 'Five Points', 'California', '93624');



INSERT INTO Books (title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice)
VALUE
('Euphoria', 'Lily','King',"978-0-80-212255-1", 'Atlantic Monthly Press', 2014, 3, 11.70, 4, 5.31 ),
('Moonwalking with Einstein', 'Joshua', 'Foer', '978-1-59-420229-2','The Penguin Press', 2011, 5, 9.79, 7, 5.90),
('Scarlet', 'Marissa', 'Meyer','978-1-25-000721-6', 'Square Fish', 2013, 2, 9.89, 6, 4.84),
('The Thousand Autumns of Jacob de Zoet', 'David', 'Mitchell', '978-0-34-092157-9', 'Random House', 2010, 5, 12.90, 4, 5.33),
('Throne of Glass', 'Sarah', 'Mass', '978-1-40-883233-2', 'Bloomsbury Publishing PLC', 2012, 1, 9.96, 5, 2.19);


INSERT INTO Orders (idCustomer, orderDate, orderTotal, orderType) 
VALUE
((SELECT idCustomer FROM Customers WHERE idCustomer = 2), '2022-03-18', 19.68, 'purchase'),
((SELECT idCustomer FROM Customers WHERE idCustomer = 5), '2022-01-02', 22.86, 'purchase'),
((SELECT idCustomer FROM Customers WHERE idCustomer = 3), '2022-02-16', 11.70, 'purchase'),
((SELECT idCustomer FROM Customers WHERE idCustomer = 4), '2022-04-20', 5.90, 'purchase'),
((SELECT idCustomer FROM Customers WHERE idCustomer = 2), '2022-04-20', 10.62, 'purchase'),
((SELECT idCustomer FROM Customers WHERE idCustomer = 1), '2022-04-25', 4.84, 'purchase');


INSERT INTO Reviews (idCustomer, idBook, postTitle, postBody, stars)
VALUE 
((SELECT idCustomer FROM Customers WHERE idCustomer = 3), (SELECT idBook FROM Books WHERE idBook = 2), 'Great book', "The best book I've read my entire life", 5),
((SELECT idCustomer FROM Customers WHERE idCustomer = 2), (SELECT idBook FROM Books WHERE idBook = 3), 'Mediocre', "This book was predictable and not very exciting", 3),
((SELECT idCustomer FROM Customers WHERE idCustomer = 4), (SELECT idBook FROM Books WHERE idBook = 4), 'Not bad', "The character development was not bad but could use work", 4),
((SELECT idCustomer FROM Customers WHERE idCustomer = 1), (SELECT idBook FROM Books WHERE idBook = 2), 'Not good', "Terrible book, do not recommend", 1),
((SELECT idCustomer FROM Customers WHERE idCustomer = 1), (SELECT idBook FROM Books WHERE idBook = 1), 'Pretty good', "Good for a quick relaxing read", 4);

INSERT INTO OrderDetails (idOrder, idBook, orderQty)
VALUE
((SELECT idOrder FROM Orders WHERE idOrder = 1), (SELECT idBook FROM Books WHERE idBook = 2), 1),
((SELECT idOrder FROM Orders WHERE idOrder = 1), (SELECT idBook FROM Books WHERE idBook = 3), 1),
((SELECT idOrder FROM Orders WHERE idOrder = 2), (SELECT idBook FROM Books WHERE idBook = 4), 1),
((SELECT idOrder FROM Orders WHERE idOrder = 2), (SELECT idBook FROM Books WHERE idBook = 5), 1),
((SELECT idOrder FROM Orders WHERE idOrder = 3), (SELECT idBook FROM Books WHERE idBook = 1), 1),
((SELECT idOrder FROM Orders WHERE idOrder = 4), (SELECT idBook FROM Books WHERE idBook = 2), 1),
((SELECT idOrder FROM Orders WHERE idOrder = 5), (SELECT idBook FROM Books WHERE idBook = 1), 2),
((SELECT idOrder FROM Orders WHERE idOrder = 6), (SELECT idBook FROM Books WHERE idBook = 3), 1);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;
