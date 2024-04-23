CREATE DATABASE CORP_CONNECT;

USE CORP_CONNECT

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Password VARCHAR(255),
    JobTitle VARCHAR(255),
    RegistrationDate DATE
);


CREATE TABLE UserCredentials (
    UserID INT,
    Username VARCHAR(255),
    PasswordHash VARCHAR(255),
    PasswordSalt VARCHAR(255),
    LastChanged DATETIME,
    SecurityQuestions VARCHAR(255),
    SecurityAnswersHash VARCHAR(255),
    TwoFactorEnabled BOOLEAN,
    TwoFactorSecret VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);



CREATE TABLE EmployeeProfiles (
    UserID INT,
    JobTitle VARCHAR(255),
    ProfessionalDetails TEXT,
    DocumentsCreated INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);


CREATE TABLE Documents (
    DocumentID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255),
    Abstract TEXT,
    Content TEXT,
    ViewCount INT,
    UpvoteCount INT,
    DownvoteCount INT,
    OwnerID INT,
    FOREIGN KEY (OwnerID) REFERENCES Users(UserID)
);
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    DocumentID INT,
    FeedbackText TEXT,
    DateSubmitted DATETIME,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (DocumentID) REFERENCES Documents(DocumentID)
);


CREATE TABLE Comments (
    CommentID INT AUTO_INCREMENT PRIMARY KEY,
    DocumentID INT,
    UserID INT,
    CommentText TEXT,
    Timestamp DATETIME,
    IsEdited BOOLEAN,
    FOREIGN KEY (DocumentID) REFERENCES Documents(DocumentID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);



CREATE TABLE PerformanceReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeID INT,
    ReviewerID INT,
    Date DATE,
    Strengths TEXT,
    Weaknesses TEXT,
    Goals TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES Users(UserID),
    FOREIGN KEY (ReviewerID) REFERENCES Users(UserID)
);

CREATE TABLE Notifications (
    NotificationID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    MessageType VARCHAR(255),
    MessageContent TEXT,
    DateCreated DATETIME,
    IsRead BOOLEAN,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);



CREATE TABLE UserGroups (
    GroupID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Description TEXT,
    CreatedBy INT,
    CreationDate DATE,
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID)
);


CREATE TABLE GroupMembers (
    GroupID INT,
    UserID INT,
    FOREIGN KEY (GroupID) REFERENCES UserGroups(GroupID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    PRIMARY KEY (GroupID, UserID)
);


CREATE TABLE Posts (
    PostID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255),
    Likes INT,
    Dislikes INT,
    Views INT,
    UserID INT,
    DocumentID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (DocumentID) REFERENCES Documents(DocumentID)
);	
