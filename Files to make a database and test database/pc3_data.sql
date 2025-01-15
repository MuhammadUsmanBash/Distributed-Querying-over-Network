-- Students for PC3
INSERT INTO Student (AdmissionNumber, FirstName, LastName, Address, ContactNo)
VALUES
(11, 'Jack', 'Harris', '892 Poplar Dr, Northport', '123-456-7891'),
(12, 'Karen', 'Martin', '103 Hickory Pl, Southgate', '234-567-8902'),
(13, 'Leo', 'King', '214 Willow Cir, Hillside', '345-678-9013'),
(14, 'Mia', 'Scott', '325 Sycamore Ter, Greenfield', '456-789-0124'),
(15, 'Noah', 'Young', '436 Spruce Ave, Brookfield', '567-890-1235');

-- Courses for PC3
INSERT INTO Course (CourseID, Name, Description)
VALUES
(7, 'Psychology 101', 'Basics of psychology, focusing on human behavior and cognition.'),
(8, 'Economics 101', 'Principles of microeconomics and macroeconomics.'),
(9, 'English Literature 101', 'Study of classic and modern literature.'),
(10, 'Philosophy 101', 'Introduction to philosophical thinking and reasoning.');

-- Enrollments for PC3
INSERT INTO Enrolled (EnrollmentID, AdmissionNumber, CourseID, EnrollmentDate, CompletionDate)
VALUES
(11, 11, 7, '2024-01-01', '2024-05-01'),
(12, 12, 8, '2024-01-15', '2024-06-15'),
(13, 13, 9, '2024-02-01', '2024-07-01'),
(14, 14, 10, '2024-03-01', '2024-08-01'),
(15, 15, 7, '2024-04-01', '2024-09-01');
