-- Students for PC1
INSERT INTO Student (AdmissionNumber, FirstName, LastName, Address, ContactNo)
VALUES
(1, 'John', 'Doe', '123 Main St, Cityville', '123-456-7890'),
(2, 'Jane', 'Smith', '456 Elm St, Townsville', '234-567-8901'),
(3, 'Alice', 'Johnson', '789 Oak St, Villagetown', '345-678-9012'),
(4, 'Bob', 'Brown', '135 Maple Ave, Springfield', '456-789-0123'),
(5, 'Charlie', 'Davis', '246 Pine Rd, Lakeside', '567-890-1234');

-- Courses for PC1
INSERT INTO Course (CourseID, Name, Description)
VALUES
(1, 'Mathematics 101', 'Basic mathematics course covering algebra, geometry, and calculus.'),
(2, 'Physics 101', 'Introduction to physics including mechanics and thermodynamics.'),
(3, 'Chemistry 101', 'Basic principles of chemistry, including atomic structure and bonding.');

-- Enrollments for PC1
INSERT INTO Enrolled (EnrollmentID, AdmissionNumber, CourseID, EnrollmentDate, CompletionDate)
VALUES
(1, 1, 1, '2024-01-15', '2024-05-15'),
(2, 2, 2, '2024-02-01', '2024-06-01'),
(3, 3, 3, '2024-01-10', '2024-05-10'),
(4, 4, 1, '2024-01-12', '2024-05-12'),
(5, 5, 2, '2024-01-15', '2024-05-15');

