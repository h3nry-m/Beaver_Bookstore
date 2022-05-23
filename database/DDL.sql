SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;


DROP TABLE IF EXISTS `Customers`;
DROP TABLE IF EXISTS `Orders`;
DROP TABLE IF EXISTS `Books`;
DROP TABLE IF EXISTS `OrderDetails`;
DROP TABLE IF EXISTS `Reviews`;
DROP TABLE IF EXISTS `Coupons`;

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
    addressCity VARCHAR(45) NOT NULL,
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
    orderDate DATE NOT NULL,
    orderTotal DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (idOrder),
    FOREIGN KEY (idCustomer) REFERENCES Customers (idCustomer) ON DELETE CASCADE
);

-- -----------------------------------------------------
-- Table Coupons
-- -----------------------------------------------------
CREATE TABLE Coupons (
    idCoupon INT UNIQUE AUTO_INCREMENT,
    expirationDate DATE NOT NULL,
    discountCode VARCHAR(45),
    discountPercent DECIMAL(3,2) NOT NULL,
    PRIMARY KEY (idCoupon)
);


-- -----------------------------------------------------
-- Intersecting Table OrderDetails
-- -----------------------------------------------------
CREATE TABLE OrderDetails (
    orderDetailsID INT NOT NULL UNIQUE AUTO_INCREMENT,
    idOrder INT,
    idBook INT,
    idCoupon INT DEFAULT NULL,
    orderQty INT NOT NULL,
    orderType VARCHAR(8) NOT NULL CHECK (orderType IN ('sale', 'purchase')),
    orderPrice DECIMAL(5,2) NOT NULL,
    discountedPrice DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (orderDetailsID),
    FOREIGN KEY (idOrder) REFERENCES Orders (idOrder) ON DELETE CASCADE,
    FOREIGN KEY (idBook) REFERENCES Books (idBook) ON DELETE CASCADE,
    FOREIGN KEY (idCoupon) REFERENCES Coupons (idCoupon) ON DELETE CASCADE
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
    FOREIGN KEY (idCustomer) REFERENCES Customers (idCustomer) ON DELETE CASCADE,
    FOREIGN KEY (idBook) REFERENCES Books (idBook) ON DELETE CASCADE
);


INSERT INTO Customers (firstName, lastName, email, phoneNumber, addressStreet, addressCity, addressState, addressZip)
VALUE
('Cara', 'Jacob', 'cara.jacob9@hotmail.com', '954-616-7898', '667 Kenwood Place','Fort Lauderdale', 'FL', '33301'),
('Gene', 'Fram', 'gene_fram7@hotmail.com', '612-775-0456', '2128 Jewell Road', 'Minneapolis', 'MN', '55402'),
('Keith', 'Hazlett', 'hazlett_keith3@hotmail.com', '505-248-2439', '4455 Byrd Lane', 'Albuquerque', 'NM', '87102'),
('Frank', 'Owens', 'frank_owens2@hotmail.com','412-280-7116', '4938 Jacobs Street', 'Pittsburgh','PA','15222'),
('Jared', 'Collazo', 'jard.collaz@hotmail.com', '714-201-2358', '3593 Half and Half Drive', 'Five Points', 'CA', '93624');



INSERT INTO Books (title, firstName, lastName, isbn, publisher, publicationYear, newStock, newPrice, usedStock, usedPrice)
VALUE
('Euphoria', 'Lily','King','978-0-80-212255-1', 'Atlantic Monthly Press', 2014, 3, 11.70, 4, 5.31 ),
('Moonwalking with Einstein', 'Joshua', 'Foer', '978-1-59-420229-2','The Penguin Press', 2011, 5, 9.79, 7, 5.90),
('Scarlet', 'Marissa', 'Meyer','978-1-25-000721-6', 'Square Fish', 2013, 2, 9.89, 6, 4.84),
('The Thousand Autumns of Jacob de Zoet', 'David', 'Mitchell', '978-0-34-092157-9', 'Random House', 2010, 5, 12.90, 4, 5.33),
('Throne of Glass', 'Sarah', 'Mass', '978-1-40-883233-2', 'Bloomsbury Publishing PLC', 2012, 1, 9.96, 5, 2.19);


INSERT INTO Orders (idCustomer, orderDate, orderTotal) 
VALUE
(2, '2022-03-18', 68.93),
(5, '2022-01-02', 40.15),
(3, '2022-02-16', 9.36),
(4, '2022-04-20', 5.90),
(2, '2022-04-20', 10.62),
(1, '2022-04-25', 4.84);


INSERT INTO Reviews (idCustomer, idBook, postTitle, postBody, stars)
VALUE 
(3, 2, 'Great book', NULL, 5),
(2, 3, 'Mediocre', "This book was predictable and not very exciting", 3),
(4, 4, NULL, "The character development was not bad but could use work", 4),
(1, 2, 'Not good', "Terrible book, do not recommend", 1),
(1, 1, 'Pretty good', "Good for a quick relaxing read", 4);

INSERT INTO Coupons (expirationDate, discountCode, discountPercent)
VALUE
('2023-04-25', '10_OFF_MITCHELL', 0.10),
('2023-02-08', '15_OFF_BLOOMSBURG', 0.15),
('2023-01-13', '20_OFF_NEW2014BOOKS', 0.20);

INSERT INTO OrderDetails (idOrder, idBook, orderQty, orderType, orderPrice, idCoupon, discountedPrice)
VALUE
(1, 2, 3, "purchase", 29.37, NULL, 29.37),
(1, 3, 4, "purchase", 39.56, NULL, 39.56),
(2, 4, 2, "purchase", 25.80, 1, 23.22),
(2, 5, 2, "purchase", 19.92, 2, 16.93),
(3, 1, 2, "purchase", 11.70, 3, 9.36),
(4, 2, 1, "sale", 5.90, NULL, 5.90),
(5, 1, 2, "sale", 10.62, NULL, 10.62),
(6, 3, 1, "sale", 4.84, NULL, 4.84);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;
