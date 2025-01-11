import tkinter as tk
from tkinter import ttk, messagebox
from main import fetch_students, fetch_courses, fetch_enrollments, search_students, search_courses, search_enrollments

def show_data(option, filter_option="none", search_value=""):
    """Display data in the table based on the selected option and filter."""
    try:
        for row in tree.get_children():
            tree.delete(row)  # Clear existing rows in the table

        # Fetch data based on filters
        if filter_option == "none":
            if option == "students":
                data = fetch_students()
                columns = ("Admission Number", "First Name", "Last Name", "Address", "Contact Number")
            elif option == "courses":
                data = fetch_courses()
                columns = ("Course ID", "Name", "Description")
            elif option == "enrollments":
                data = fetch_enrollments()
                columns = ("Enrollment ID", "Student Name", "Course Name", "Enrollment Date", "Completion Date")
            else:
                return
        else:
            if option == "students":
                if filter_option == "name":
                    data = search_students("CONCAT(FirstName, ' ', LastName)", search_value)
                elif filter_option == "address":
                    data = search_students("Address", search_value)
                elif filter_option == "contact":
                    data = search_students("ContactNo", search_value)
                columns = ("Admission Number", "First Name", "Last Name", "Address", "Contact Number")
            elif option == "courses":
                if filter_option == "name":
                    data = search_courses("Name", search_value)
                elif filter_option == "description":
                    data = search_courses("Description", search_value)
                columns = ("Course ID", "Name", "Description")
            elif option == "enrollments":
                if filter_option == "enrollment_date":
                    data = search_enrollments("EnrollmentDate", search_value)
                elif filter_option == "completion_date":
                    data = search_enrollments("CompletionDate", search_value)
                columns = ("Enrollment ID", "Student Name", "Course Name", "Enrollment Date", "Completion Date")
            else:
                return

        # Update table headings
        tree["columns"] = columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        # Insert data into the table
        for row in data:
            tree.insert("", "end", values=row)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")

# Callback for combo box change
def update_filter_options(option):
    """Update filter combo box based on the selected main option."""
    if option == "students":
        filter_combo["values"] = ["none", "name", "address", "contact"]
    elif option == "courses":
        filter_combo["values"] = ["none", "name", "description"]
    elif option == "enrollments":
        filter_combo["values"] = ["none", "enrollment_date", "completion_date"]
    else:
        filter_combo["values"] = ["none"]
    filter_combo.set("none")

# Create the main window
root = tk.Tk()
root.title("Student Management Portal")
root.geometry("800x600")

# Title Label
title_label = tk.Label(root, text="Student Management Portal", font=("Arial", 20))
title_label.pack(pady=10)

# Combo Box, Filter, and Search
frame = tk.Frame(root)
frame.pack(pady=10)

options = ["students", "courses", "enrollments"]
selected_option = tk.StringVar(value=options[0])
combo_box = ttk.Combobox(frame, textvariable=selected_option, values=options, state="readonly")
combo_box.grid(row=0, column=0, padx=10)

filter_label = tk.Label(frame, text="Filter:")
filter_label.grid(row=0, column=1, padx=5)

filter_option = tk.StringVar(value="none")
filter_combo = ttk.Combobox(frame, textvariable=filter_option, state="readonly", values=["none"])
filter_combo.grid(row=0, column=2, padx=10)

search_entry = tk.Entry(frame, width=30)
search_entry.grid(row=0, column=3, padx=10)

search_button = tk.Button(frame, text="Search", command=lambda: show_data(selected_option.get(), filter_option.get(), search_entry.get()))
search_button.grid(row=0, column=4, padx=10)

# Update filter options when the main combo box changes
combo_box.bind("<<ComboboxSelected>>", lambda e: update_filter_options(selected_option.get()))

# Table
tree = ttk.Treeview(root, show="headings")
tree.pack(expand=True, fill="both", padx=20, pady=20)



# Start the application
root.mainloop()
