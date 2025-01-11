import mysql.connector

def connect_db():
    """Connect to the locally installed database."""
    return mysql.connector.connect(
        host="localhost",        # Replace with your database host (e.g., "127.0.0.1")
        user="root",             # Replace with your database username
        password="Usman12Ahmad",  # Replace with your database password
        database="StudentManagement"  # Replace with your database name
    )

def fetch_students():
    """Fetch all students."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student;")
    data = cursor.fetchall()
    conn.close()
    return data

def fetch_courses():
    """Fetch all courses."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Course;")
    data = cursor.fetchall()
    conn.close()
    return data

def fetch_enrollments():
    """Fetch all enrollments with student names and course names."""
    conn = connect_db()
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
    conn.close()
    return data

def search_students(field, search_value):
    """Search students based on a specific field and value."""
    conn = connect_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM Student WHERE {field} LIKE %s;"
    cursor.execute(query, (f"%{search_value}%",))
    data = cursor.fetchall()
    conn.close()
    return data

def search_courses(field, search_value):
    """Search courses based on a specific field and value."""
    conn = connect_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM Course WHERE {field} LIKE %s;"
    cursor.execute(query, (f"%{search_value}%",))
    data = cursor.fetchall()
    conn.close()
    return data

def search_enrollments(field, search_value):
    """Search enrollments based on a specific field and value."""
    conn = connect_db()
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
    conn.close()
    return data
