# Database Printer

##  Overview

**Multiway** is a desktop-based Python application built with **Tkinter** that provides a simple graphical interface for managing users, students, and expense records. The system integrates with a **MySQL database** to retrieve stored data and can **export expense records to Excel files** for reporting and printing.

The project is suitable for **learning GUI development**, **database integration**, and **file handling** in Python.

---

##  Project Structure

```
Latest/
│── main.py              # Login window (application entry point)
│── data_save.py         # Main system dashboard & navigation
│── sudent_names.py      # Database access & Excel export logic
│── main.png             # Application icon
```

---

##  Features

* 🔐 **Login Interface** using Tkinter
* 🧑‍🎓 **Student data handling** from MySQL database
* 💰 **Expense management**
* 📊 **Export all expenses to Excel (.xlsx)**
* 🖨️ Option to print/view saved expense files
* 🖼️ Custom window icon and styled GUI

---

##  Technologies Used

* **Python 3.x**
* **Tkinter** – GUI development
* **Pillow (PIL)** – Image handling
* **MySQL** – Database storage
* **mysql-connector-python** – Database connection
* **openpyxl** – Excel file creation and formatting

---

##  Requirements

Make sure you have the following installed:

* Python **3.7 or higher**
* MySQL Server
* Required Python packages:

```bash
pip install pillow mysql-connector-python openpyxl
```

---

##  Database Configuration

The system expects a **MySQL database** with the following default configuration:

* **Host:** localhost
* **User:** root
* **Password:** (empty)
* **Database name:** `register`

⚠️ Make sure the required tables and data already exist in the database, as this project reads from them.

You can modify the database credentials inside:

```python
sudent_names.py
```

---

##  How to Run the Project

1. Clone or download the repository
2. Ensure MySQL server is running
3. Place all files in the same directory
4. Run the application:

```bash
python main.py
```

---

##  Output Files

* Exported Excel files are saved automatically in the:

```
Saved/
```

Folder naming format:

```
All Expenses YYYY-MM-DDHHMMSS.xlsx
```

---

##  Learning Objectives

This project helps practice:

* Python GUI development with Tkinter
* Modular programming in Python
* MySQL database connectivity
* Reading data from databases
* Writing and formatting Excel files
* File and folder management

---

##  Possible Improvements

* Add user authentication validation
* Improve database error handling
* Add CRUD operations for students and expenses
* Convert to a cross-platform executable
* Improve UI responsiveness

---

##  License

This project is intended for **educational purposes**. You are free to modify and improve it.

---

##  Author

Developed by **Milkias Amanuel (XMIAN)**

If you find this project useful, feel free to ⭐ the repository!
