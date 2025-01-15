-- Students for PC2
INSERT INTO Student (AdmissionNumber, FirstName, LastName, Address, ContactNo)
VALUES
(6, 'Eve', 'Wilson', '357 Cedar Ln, Riverdale', '678-901-2345'),
(7, 'Frank', 'Moore', '468 Birch Blvd, Mountainview', '789-012-3456'),
(8, 'Grace', 'Taylor', '579 Walnut Way, Plainfield', '890-123-4567'),
(9, 'Henry', 'Anderson', '680 Cherry St, Westfield', '901-234-5678'),
(10, 'Ivy', 'Thomas', '791 Ash Ct, Eastville', '012-345-6789');

-- Courses for PC2
INSERT INTO Course (CourseID, Name, Description)
VALUES
(4, 'Biology 101', 'Fundamentals of biology, focusing on cellular biology and genetics.'),
(5, 'History 101', 'Overview of world history from ancient to modern times.'),
(6, 'Computer Science 101', 'Introduction to programming and computational thinking.');

-- Enrollments for PC2
INSERT INTO Enrolled (EnrollmentID, AdmissionNumber, CourseID, EnrollmentDate, CompletionDate)
VALUES
(6, 6, 4, '2024-03-01', '2024-07-01'),
(7, 7, 5, '2024-03-05', '2024-07-05'),
(8, 8, 6, '2024-03-10', '2024-07-10'),
(9, 9, 4, '2024-03-15', '2024-07-15'),
(10, 10, 5, '2024-04-01', '2024-08-01');


