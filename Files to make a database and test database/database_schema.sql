-- Create the database
CREATE DATABASE StudentManagement;
USE StudentManagement;

-- Create the Student table
CREATE TABLE Student (
    AdmissionNumber INT AUTO_INCREMENT PRIMARY KEY, -- Unique, auto-generated admission number
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Address TEXT NOT NULL,
    ContactNo VARCHAR(15) NOT NULL
);

-- Create the Course table
CREATE TABLE Course (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique, auto-generated course ID/number
    Name VARCHAR(100) NOT NULL,
    Description TEXT
);

-- Create the Enrolled table
CREATE TABLE Enrolled (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique, auto-generated enrollment ID
    AdmissionNumber INT NOT NULL, -- Foreign key referencing Student
    CourseID INT NOT NULL, -- Foreign key referencing Course
    EnrollmentDate DATE NOT NULL,
    CompletionDate DATE,
    FOREIGN KEY (AdmissionNumber) REFERENCES Student(AdmissionNumber)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
        ON DELETE CASCADE ON UPDATE CASCADE
);
