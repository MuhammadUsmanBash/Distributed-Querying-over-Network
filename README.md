# Distributed Querying over Network

This project implements a **Client-Server Model**, where the client sends queries to the servers, and the servers respond with data from their respective databases.

## Installation Instructions for Server Database

### Setting up the Database on Server Device A:
1. Run the file located at `Files/make_database_and_test_database/database_schema.sql` to create the database schema.
2. Populate the database with dummy data by running one of the following files:
   - `pc1_data.sql`
   - `pc2_data.sql`
   - `pc3_data.sql`
3. Verify the database creation by executing the respective `test.sql` file for the server (e.g., `pc1_test.sql`).

---

## Hosting MySQL Server on Device A and Accessing it from Device B

### Steps to Configure Device A (MySQL Server):

1. **Install MySQL Server**
   - Download and install MySQL Community Server from the [official MySQL website](https://dev.mysql.com/downloads/).
   - During installation, note down the root username and password.
   - Ensure the MySQL Server service (`mysqld`) is running.

2. **Configure MySQL for Remote Connections**
   - Open the MySQL configuration file:
     - Default location: `C:\ProgramData\MySQL\MySQL Server X.X\my.ini` (Ensure you open it as an administrator. The `ProgramData` folder is hidden by default.)
   - Locate the line: 
     ```
     bind-address = 127.0.0.1
     ```
     (This is usually under the `[mysqld]` section and might not always be present.)
   - Replace it with:
     ```
     bind-address = 0.0.0.0
     ```
     This change allows MySQL to accept connections from any IP address.

3. **Restart the MySQL Service**
   - Open the Command Prompt as an administrator.
   - Execute the following commands:
     ```bash
     net stop MySQL83 # Adjust version accordingly
     net start MySQL83 # Adjust version accordingly
     ```

4. **Create a User for Remote Access**
   - Log in to MySQL:
     ```bash
     mysql -u root -p
     ```
     (Run this command from the `MySQL Server <version>/bin` folder in the Command Prompt.)
   - Create a new user and grant remote access:
     ```sql
     CREATE USER 'remote_user'@'%' IDENTIFIED BY 'password';
     GRANT ALL PRIVILEGES ON *.* TO 'remote_user'@'%' WITH GRANT OPTION;
     FLUSH PRIVILEGES;
     ```
     Replace `remote_user` and `password` with your desired username and password.

5. **Allow MySQL Port in Windows Firewall**
   - Open **Control Panel** > **System and Security** > **Windows Defender Firewall** > **Advanced Settings**.
   - Navigate to **Inbound Rules** > **New Rule**.
   - Select **Port**, enter `3306` (default MySQL port), and choose **Allow the connection**.
   - Click **Next**, and give the rule a name.

6. **Get Device A's IP Address**
   - Run the following command to find the IP address:
     ```bash
     ipconfig
     ```
   - Note the **IPv4 Address** of the network adapter (e.g., `192.168.1.2`).

7. **Repeat Steps for Additional Servers**
   - Configure additional devices as servers if needed.

---

### Steps to Configure Device B (Client Application):

1. **Install MySQL Client or Connector**
   - If using Python, ensure the MySQL connector library is installed:
     ```bash
     pip install mysql-connector-python
     ```

2. **Connect to Device A's MySQL Server**
   - Use the IP address of Device A and the credentials created earlier.

3. **Test the Connection**
   - Run the client application to ensure successful connectivity and data retrieval.

---

## Final Setup

After completing the initial setup:
1. Update the IP addresses in `GUI.py` as per your server configuration.
2. Run the application to execute queries seamlessly.

---
