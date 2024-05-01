INSERT INTO Users (Name, Email, Password, JobTitle, RegistrationDate)
VALUES 
    ('Kavish Singh', 'kavish.singh@gmail.com', 'password123', 'Software Engineer', '2024-04-30');
INSERT INTO Documents (Title, Abstract, Content, ViewCount, UpvoteCount, DownvoteCount, OwnerID)
VALUES 
    ('Pointers', 'This is a sample document abstract for pointers', 'Pointers are used to store and manage the addresses of dynamically allocated blocks of memory. Such blocks are used to store data objects or arrays of objects. Most structured and object-oriented languages provide an area of memory, called the heap or free store, from which objects are dynamically allocated', 0, 0, 0, (SELECT UserID FROM Users WHERE Name = 'Kavish Singh'));

SELECT * FROM users;

SELECT * FROM documents;