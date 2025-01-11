-- Count rows in Student table
SELECT COUNT(*) AS TotalStudents FROM Student;

-- Count rows in Course table
SELECT COUNT(*) AS TotalCourses FROM Course;

-- Count rows in Enrolled table
SELECT COUNT(*) AS TotalEnrollments FROM Enrolled;




-- Check if all Enrollment records reference valid Students and Courses
SELECT e.EnrollmentID
FROM Enrolled e
LEFT JOIN Student s ON e.AdmissionNumber = s.AdmissionNumber
LEFT JOIN Course c ON e.CourseID = c.CourseID
WHERE s.AdmissionNumber IS NULL OR c.CourseID IS NULL;



-- Check number of Students, Courses, and Enrollments for each PC

-- PC2
SELECT COUNT(*) AS Students_PC2 FROM Student WHERE AdmissionNumber BETWEEN 6 AND 10;
SELECT COUNT(*) AS Courses_PC2 FROM Course WHERE CourseID BETWEEN 4 AND 6;
SELECT COUNT(*) AS Enrollments_PC2 FROM Enrolled WHERE AdmissionNumber BETWEEN 6 AND 10;





