import tkinter as tk
from tkinter import ttk, messagebox
from main import connect_db, fetch_students, fetch_courses, fetch_enrollments, search_students, search_courses, search_enrollments



# Manage connections globally
connections = {}

def manage_connection(pc, ip, is_checked, var):
    """Establish or close connections based on the checkbox state."""
    global connections
    if is_checked:
        try:
            connections[pc] = connect_db(ip)
            messagebox.showinfo("Connection Status", f"Connected to {pc}.")
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect to {pc}: {e}")
            var.set(False)  # Automatically uncheck the checkbox
            if pc in connections:  # Ensure no partial connections remain
                del connections[pc]
    else:
        if pc in connections:
            connections[pc].close()
            del connections[pc]
            messagebox.showinfo("Connection Status", f"Disconnected from {pc}.")



def close_all_connections():
    """Close all active connections when the application exits."""
    global connections
    for pc, conn in list(connections.items()):
        conn.close()
        del connections[pc]

def show_data(option, filter_option="none", search_value=""):
    """Display data in the table based on the selected option and filter."""
    try:
        for row in tree.get_children():
            tree.delete(row)  # Clear existing rows in the table

        # Check active connections
        active_connections = {}
        for pc, conn in list(connections.items()):
            try:
                conn.ping(reconnect=True)  # Check if the connection is active
                active_connections[pc] = conn
            except Exception:
                # Uncheck the checkbox and remove the connection
                if pc == "PC 1":
                    pc1_var.set(False)
                elif pc == "PC 2":
                    pc2_var.set(False)
                elif pc == "PC 3":
                    pc3_var.set(False)
                del connections[pc]
                messagebox.showwarning("Connection Lost", f"Connection to {pc} lost. Unchecking the box.")

        if not active_connections:
            messagebox.showwarning("No Connection", "No active connections. Please check at least one PC.")
            return

        # Fetch data from all active connections
        data = []
        columns = ()
        for conn in active_connections.values():
            if filter_option == "none":
                if option == "students":
                    data += fetch_students(conn)
                    columns = ("Admission Number", "First Name", "Last Name", "Address", "Contact Number")
                elif option == "courses":
                    data += fetch_courses(conn)
                    columns = ("Course ID", "Name", "Description")
                elif option == "enrollments":
                    data += fetch_enrollments(conn)
                    columns = ("Enrollment ID", "Student Name", "Course Name", "Enrollment Date", "Completion Date")
            else:
                if option == "students":
                    if filter_option == "name":
                        data += search_students(conn, "CONCAT(FirstName, ' ', LastName)", search_value)
                    elif filter_option == "address":
                        data += search_students(conn, "Address", search_value)
                    elif filter_option == "contact":
                        data += search_students(conn, "ContactNo", search_value)
                    columns = ("Admission Number", "First Name", "Last Name", "Address", "Contact Number")
                elif option == "courses":
                    if filter_option == "name":
                        data += search_courses(conn, "Name", search_value)
                    elif filter_option == "description":
                        data += search_courses(conn, "Description", search_value)
                    columns = ("Course ID", "Name", "Description")
                elif option == "enrollments":
                    if filter_option == "enrollment_date":
                        data += search_enrollments(conn, "EnrollmentDate", search_value)
                    elif filter_option == "completion_date":
                        data += search_enrollments(conn, "CompletionDate", search_value)
                    columns = ("Enrollment ID", "Student Name", "Course Name", "Enrollment Date", "Completion Date")

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

# Checkboxes for PCs
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=10)

pc1_var = tk.BooleanVar(value=False)
pc2_var = tk.BooleanVar(value=False)
pc3_var = tk.BooleanVar(value=False)

pc1_checkbox = tk.Checkbutton(checkbox_frame, text="PC 1", variable=pc1_var,
                               command=lambda: manage_connection("PC 1", "172.16.15.202", pc1_var.get(), pc1_var))
pc1_checkbox.grid(row=0, column=0, padx=10)

pc2_checkbox = tk.Checkbutton(checkbox_frame, text="PC 2", variable=pc2_var,
                               command=lambda: manage_connection("PC 2", "172.16.15.102", pc2_var.get(), pc2_var))
pc2_checkbox.grid(row=0, column=1, padx=10)

pc3_checkbox = tk.Checkbutton(checkbox_frame, text="PC 3", variable=pc3_var,
                               command=lambda: manage_connection("PC 3", "172.16.16.0", pc3_var.get(), pc3_var))
pc3_checkbox.grid(row=0, column=2, padx=10)


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

# Close all connections on exit
root.protocol("WM_DELETE_WINDOW", lambda: (close_all_connections(), root.destroy()))

# Start the application
root.mainloop()
