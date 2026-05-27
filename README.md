# 🎄 Secret Santa Web Application - Setup Guide

A complete web application for creating Secret Santa assignments and managing wishlists using Flask and MySQL.

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation & Setup](#installation--setup)
5. [Database Configuration](#database-configuration)
6. [Running the Application](#running-the-application)
7. [Project Structure](#project-structure)
8. [Usage Guide](#usage-guide)
9. [Troubleshooting](#troubleshooting)

---

## 🎯 Project Overview

The Secret Santa Application is a web-based tool that helps organize Secret Santa exchanges. It provides functionality to:
- Randomly assign Secret Santa pairs
- Manage and view assignments
- Create and share wishlists

**Tech Stack:**
- **Backend:** Flask (Python)
- **Database:** MySQL
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Icons:** Font Awesome

---

## ✨ Features

### 1. **Create Secret Santa Assignments**
   - Enter participant names (comma or newline separated)
   - Automatic random assignment algorithm
   - Ensures no person gets themselves
   - Stores date and time of creation

### 2. **View Assignments**
   - See all created assignments
   - Grouped by creation date/time
   - Delete individual or all assignments
   - Clean, organized display

### 3. **Wishlist Management**
   - Add personalized wishlists
   - View all wishlists
   - Delete wishlist entries
   - Date/time tracking

### 4. **User-Friendly Interface**
   - Responsive design (Mobile, Tablet, Desktop)
   - Beautiful gradient colors
   - Smooth animations
   - Easy navigation

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.7+**
   - Download from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **MySQL Server**
   - Download from: https://dev.mysql.com/downloads/mysql/
   - Or use MySQL Community Edition

3. **MySQL Workbench** (Optional, for easier database management)
   - Download from: https://dev.mysql.com/downloads/workbench/

4. **Text Editor or IDE**
   - VS Code (Recommended): https://code.visualstudio.com/
   - PyCharm: https://www.jetbrains.com/pycharm/

---

## 🚀 Installation & Setup

### Step 1: Clone/Download the Project

Download all project files and create the following folder structure:

```
secret_santa_app/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── database.sql             # Database creation script
│
├── templates/               # HTML templates folder
│   ├── base.html
│   ├── index.html
│   ├── create_secret_santa.html
│   ├── view_secret_santa.html
│   ├── add_wishlist.html
│   ├── view_wishlists.html
│   ├── 404.html
│   └── 500.html
│
└── README.md               # This file
```

### Step 2: Install Python Dependencies

Open Command Prompt/Terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

**Alternative (if above doesn't work):**

```bash
pip install Flask==2.3.3
pip install Flask-MySQLdb==1.0.1
pip install MySQLdb-python==1.2.5b1
```

---

## 🗄️ Database Configuration

### Step 1: Open MySQL Command Line or MySQL Workbench

**Using MySQL Command Line:**
```bash
mysql -u root -p
```

**Or use MySQL Workbench GUI**

### Step 2: Create Database and Tables

Run the following SQL commands from `database.sql`:

```sql
CREATE DATABASE IF NOT EXISTS secret_santa_db;
USE secret_santa_db;

CREATE TABLE IF NOT EXISTS secret_santa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    participant_name VARCHAR(100) NOT NULL,
    assigned_to VARCHAR(100) NOT NULL,
    created_date DATE NOT NULL,
    created_time TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS wishlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    wishlist TEXT NOT NULL,
    created_date DATE NOT NULL,
    created_time TIME NOT NULL
);
```

### Step 3: Configure Database Connection in Flask

Edit `app.py` and update the MySQL configuration:

```python
app.config['MYSQL_HOST'] = 'localhost'      # Keep as localhost
app.config['MYSQL_USER'] = 'root'           # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'your_password'  # Your MySQL password
app.config['MYSQL_DB'] = 'secret_santa_db' # Database name
```

**Example:**
```python
app.config['MYSQL_PASSWORD'] = 'MyPassword123'  # If your password is 'MyPassword123'
app.config['MYSQL_PASSWORD'] = ''               # If no password (default for local)
```

---

## ▶️ Running the Application

### Step 1: Navigate to Project Directory

```bash
cd path/to/secret_santa_app
```

### Step 2: Start Flask Application

```bash
python app.py
```

Or:

```bash
flask run
```

### Step 3: Open in Browser

Open your web browser and go to:

```
http://localhost:5000
```

You should see the Secret Santa homepage! 🎉

---

## 📁 Project Structure

```
secret_santa_app/
│
├── app.py
│   ├── Database Configuration
│   ├── Helper Functions (assign_secret_santa, validate_participants)
│   ├── Routes:
│   │   ├── / (index)
│   │   ├── /create_secret_santa
│   │   ├── /view_secret_santa
│   │   ├── /add_wishlist
│   │   ├── /view_wishlists
│   │   ├── /delete_assignment/<id>
│   │   ├── /delete_wishlist/<id>
│   │   └── /clear_all_assignments
│   └── Error Handlers (404, 500)
│
├── templates/
│   ├── base.html              # Base template with navbar
│   ├── index.html             # Homepage
│   ├── create_secret_santa.html
│   ├── view_secret_santa.html
│   ├── add_wishlist.html
│   ├── view_wishlists.html
│   ├── 404.html               # Error page
│   └── 500.html               # Error page
│
└── Database:
    ├── secret_santa table
    └── wishlist table
```

---

## 📖 Usage Guide

### 1. **Creating Secret Santa Assignments**

1. Click "Create Secret Santa" button on homepage
2. Enter participant names:
   - Separated by commas: `Alice, Bob, Charlie`
   - Or one per line:
     ```
     Alice
     Bob
     Charlie
     ```
3. Click "Create Assignments"
4. Assignments are randomly created and saved

**Example Assignment:**
```
Alice → Charlie (gives gift to Charlie)
Bob → Alice (gives gift to Alice)
Charlie → Bob (gives gift to Bob)
```

### 2. **Viewing Assignments**

1. Click "View Assignments" in navbar or homepage
2. See all assignments grouped by creation date/time
3. Delete individual assignments or clear all
4. View assignment dates and times

### 3. **Adding Wishlists**

1. Click "Add Wishlist" button
2. Enter your name
3. Enter detailed wishlist items:
   ```
   - Sony WH-1000XM4 Headphones (Black)
   - Coffee Machine (Stainless Steel)
   - Book: "Atomic Habits"
   - Cozy Sweater (Size M, Dark Blue)
   ```
4. Click "Submit Wishlist"

### 4. **Viewing Wishlists**

1. Click "View Wishlists" in navbar
2. See all wishlists grouped by person
3. Use wishlists to find gift ideas
4. Delete wishlists if needed

---

## 🔧 Database Schema

### secret_santa Table

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Primary Key, Auto-increment |
| participant_name | VARCHAR(100) | Name of person being assigned |
| assigned_to | VARCHAR(100) | Name of person they give to |
| created_date | DATE | Date assignment was created |
| created_time | TIME | Time assignment was created |

### wishlist Table

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Primary Key, Auto-increment |
| name | VARCHAR(100) | Name of person with wishlist |
| wishlist | TEXT | Wishlist content (items/preferences) |
| created_date | DATE | Date wishlist was created |
| created_time | TIME | Time wishlist was created |

---

## 🔍 Key Functions

### assign_secret_santa(participants)
Randomly assigns Secret Santa pairs ensuring no one gets themselves.

```python
# Input: ['Alice', 'Bob', 'Charlie']
# Output: {'Alice': 'Charlie', 'Bob': 'Alice', 'Charlie': 'Bob'}
```

### validate_participants(participants_list)
Validates participant names for duplicates and minimum count.

```python
# Checks:
# - At least 2 participants
# - No duplicate names
# - Valid input format
```

---

## 🐛 Troubleshooting

### Issue 1: MySQL Connection Error
**Error:** "Can't connect to MySQL server on 'localhost'"

**Solution:**
1. Check MySQL is running:
   - Windows: Open Services and look for "MySQL80" (or your version)
   - Mac: System Preferences > MySQL > Start MySQL Server
   - Linux: `sudo service mysql start`

2. Verify credentials in `app.py`:
   ```python
   app.config['MYSQL_USER'] = 'root'
   app.config['MYSQL_PASSWORD'] = 'your_actual_password'
   ```

### Issue 2: ModuleNotFoundError: No module named 'flask'

**Solution:**
```bash
pip install -r requirements.txt
# or
pip install Flask Flask-MySQLdb
```

### Issue 3: Database Not Found

**Solution:**
1. Create database by running SQL commands:
   ```bash
   mysql -u root -p < database.sql
   ```

2. Or manually run in MySQL:
   ```sql
   CREATE DATABASE secret_santa_db;
   ```

### Issue 4: Port 5000 Already in Use

**Solution:**
```bash
# Change port in app.py:
app.run(debug=True, host='localhost', port=5001)  # Use 5001 instead

# Then access: http://localhost:5001
```

### Issue 5: Templates Not Found

**Solution:**
- Ensure `templates/` folder is in the same directory as `app.py`
- Folder structure must be exactly:
  ```
  secret_santa_app/
  ├── app.py
  └── templates/
      ├── base.html
      ├── index.html
      └── ... (other templates)
  ```

---

## 🎨 Customization

### Change Colors

Edit `templates/base.html` and modify the gradient colors:

```css
/* Current purple gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change to different colors */
background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);  /* Red-Teal */
background: linear-gradient(135deg, #FFB347 0%, #FF6B35 100%);  /* Orange */
background: linear-gradient(135deg, #0093E9 0%, #80D0C0 100%);  /* Blue-Green */
```

### Change Secret Key

For production, change the secret key in `app.py`:

```python
app.secret_key = 'your_secret_key_here'
# Change to something random:
app.secret_key = 'aB3!xY9@kL2#mN5$pQ8'
```

### Change Port

In `app.py`, modify the port number:

```python
app.run(debug=True, host='localhost', port=8000)  # Use 8000
# Then access: http://localhost:8000
```

---

## 📝 Additional Notes

### Security Notes
- Change `secret_key` for production
- Never commit passwords to version control
- Use environment variables for sensitive data
- Set `debug=False` for production

### Performance Tips
- Add database indexes (already included)
- Use pagination for large datasets
- Cache frequently accessed data
- Optimize images and assets

### Future Enhancements
- User authentication system
- Email notifications
- PDF export of assignments
- Budget tracking
- Gift tracking
- Email integration

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review Flask documentation: https://flask.palletsprojects.com/
3. Check MySQL documentation: https://dev.mysql.com/doc/

---

## 📄 License

This project is open source and available for personal and educational use.

---

## 🎉 Enjoy!

Happy Secret Santa exchanges! This app was created to make organizing gift exchanges fun and easy.

**Created with ❤️ for spreading holiday cheer!**

---

## Version Info
- **Flask:** 2.3.3
- **Python:** 3.7+
- **MySQL:** 5.7+
- **Last Updated:** 2024