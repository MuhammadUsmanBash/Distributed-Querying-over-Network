import mysql.connector

def connect_db(ip):
    """Connect to the locally installed database with a timeout."""
    try:
        return mysql.connector.connect(
            host=ip,  # PC 2
            user="usman",
            password="usman123",
            database="StudentManagement",
            connect_timeout=5  # Timeout in seconds
        )
    except mysql.connector.Error as e:
        raise Exception(f"Failed to connect to {ip}: {e}")


def fetch_students(conn):
    """Fetch all students."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student;")
    data = cursor.fetchall()
    return data

def fetch_courses(conn):
    """Fetch all courses."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Course;")
    data = cursor.fetchall()
    return data

def fetch_enrollments(conn):
    """Fetch all enrollments with student names and course names."""
    cursor = conn.cursor()
    query = """
    SELECT 
        e.EnrollmentID, 
        CONCAT(s.FirstName, ' ', s.LastName) AS StudentName, 
        c.Name AS CourseName, 
        e.EnrollmentDate, 
        e.CompletionDate
    FROM Enrolled e
    JOIN Student s ON e.AdmissionNumber = s.AdmissionNumber
    JOIN Course c ON e.CourseID = c.CourseID;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def search_students(conn,field, search_value):
    """Search students based on a specific field and value."""
    cursor = conn.cursor()
    query = f"SELECT * FROM Student WHERE {field} LIKE %s;"
    cursor.execute(query, (f"%{search_value}%",))
    data = cursor.fetchall()
    return data

def search_courses(conn,field, search_value):
    """Search courses based on a specific field and value."""
    cursor = conn.cursor()
    query = f"SELECT * FROM Course WHERE {field} LIKE %s;"
    cursor.execute(query, (f"%{search_value}%",))
    data = cursor.fetchall()
    return data

def search_enrollments(conn,field, search_value):
    """Search enrollments based on a specific field and value."""
    cursor = conn.cursor()
    query = f"""
    SELECT 
        e.EnrollmentID, 
        CONCAT(s.FirstName, ' ', s.LastName) AS StudentName, 
        c.Name AS CourseName, 
        e.EnrollmentDate, 
        e.CompletionDate
    FROM Enrolled e
    JOIN Student s ON e.AdmissionNumber = s.AdmissionNumber
    JOIN Course c ON e.CourseID = c.CourseID
    WHERE {field} LIKE %s;
    """
    cursor.execute(query, (f"%{search_value}%",))
    data = cursor.fetchall()
    return data
