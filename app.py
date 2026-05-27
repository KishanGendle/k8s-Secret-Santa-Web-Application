from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import random
from datetime import datetime
import re
import os
from dotenv import load_dotenv

# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()

# =========================
# FLASK APP
# =========================

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "secret-key")

# =========================
# DATABASE CONFIG
# =========================

db_config = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DB", "secret_santa_db")
}


# =========================
# DATABASE CONNECTION
# =========================

def get_db_connection():

    return mysql.connector.connect(**db_config)


# =========================
# CREATE TABLES
# =========================

def init_database():

    try:
        connection = get_db_connection()

        cursor = connection.cursor()

        # Secret Santa Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS secret_santa (
                id INT AUTO_INCREMENT PRIMARY KEY,
                participant_name VARCHAR(100),
                assigned_to VARCHAR(100),
                created_date DATE,
                created_time TIME
            )
        """)

        # Wishlist Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS wishlist (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                wishlist TEXT,
                created_date DATE,
                created_time TIME
            )
        """)

        connection.commit()

        cursor.close()
        connection.close()

        print("Database tables created successfully!")

    except Exception as e:

        print("Database Error:", str(e))


# =========================
# FAVICON FIX
# =========================

@app.route('/favicon.ico')
def favicon():
    return '', 204


# =========================
# HOME PAGE
# =========================

@app.route('/')
def index():

    return render_template('index.html')


# =========================
# VALIDATE PARTICIPANTS
# =========================

def validate_participants(participants_list):

    participants = []

    for participant in participants_list:

        cleaned_name = participant.strip()

        if cleaned_name != "":
            participants.append(cleaned_name)

    # Duplicate check
    if len(participants) != len(set(participants)):
        return False, "Duplicate names are not allowed!"

    # Minimum 2 participants required
    if len(participants) < 2:
        return False, "Minimum 2 participants required!"

    return True, participants


# =========================
# SECRET SANTA ASSIGNMENT
# =========================

def assign_secret_santa(participants):

    shuffled = participants.copy()

    valid = False

    while not valid:

        random.shuffle(shuffled)

        valid = True

        for i in range(len(participants)):

            if participants[i] == shuffled[i]:
                valid = False
                break

    assignments = {}

    for i in range(len(participants)):

        assignments[participants[i]] = shuffled[i]

    return assignments


# =========================
# CREATE SECRET SANTA
# =========================

@app.route('/create_secret_santa', methods=['GET', 'POST'])
def create_secret_santa():

    if request.method == 'POST':

        participants_input = request.form.get('participants')

        participants_list = re.split(r'[,\n]+', participants_input)

        is_valid, result = validate_participants(participants_list)

        if not is_valid:

            flash(result, 'danger')

            return redirect(url_for('create_secret_santa'))

        participants = result

        assignments = assign_secret_santa(participants)

        current_datetime = datetime.now()

        current_date = current_datetime.date()

        current_time = current_datetime.time()

        try:

            connection = get_db_connection()

            cursor = connection.cursor()

            # Save data into DB
            for participant, assigned_to in assignments.items():

                query = """
                    INSERT INTO secret_santa
                    (participant_name, assigned_to, created_date, created_time)
                    VALUES (%s, %s, %s, %s)
                """

                values = (
                    participant,
                    assigned_to,
                    current_date,
                    current_time
                )

                cursor.execute(query, values)

            connection.commit()

            cursor.close()

            connection.close()

            flash('Secret Santa Created Successfully!', 'success')

            return redirect(url_for('view_secret_santa'))

        except Exception as e:

            flash(str(e), 'danger')

            return redirect(url_for('create_secret_santa'))

    return render_template('create_secret_santa.html')


# =========================
# VIEW SECRET SANTA DATA
# =========================

@app.route('/view_secret_santa')
def view_secret_santa():

    try:

        connection = get_db_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT * FROM secret_santa
            ORDER BY id DESC
        """

        cursor.execute(query)

        assignments = cursor.fetchall()

        cursor.close()

        connection.close()

        return render_template(
            'view_secret_santa.html',
            assignments=assignments
        )

    except Exception as e:

        flash(str(e), 'danger')

        return redirect(url_for('index'))


# =========================
# ADD WISHLIST
# =========================

@app.route('/add_wishlist', methods=['GET', 'POST'])
def add_wishlist():

    if request.method == 'POST':

        name = request.form.get('name')

        wishlist_text = request.form.get('wishlist')

        if name.strip() == "":

            flash("Name is required!", 'danger')

            return redirect(url_for('add_wishlist'))

        if wishlist_text.strip() == "":

            flash("Wishlist is required!", 'danger')

            return redirect(url_for('add_wishlist'))

        current_datetime = datetime.now()

        current_date = current_datetime.date()

        current_time = current_datetime.time()

        try:

            connection = get_db_connection()

            cursor = connection.cursor()

            query = """
                INSERT INTO wishlist
                (name, wishlist, created_date, created_time)
                VALUES (%s, %s, %s, %s)
            """

            values = (
                name,
                wishlist_text,
                current_date,
                current_time
            )

            cursor.execute(query, values)

            connection.commit()

            cursor.close()

            connection.close()

            flash("Wishlist Added Successfully!", 'success')

            return redirect(url_for('view_wishlists'))

        except Exception as e:

            flash(str(e), 'danger')

            return redirect(url_for('add_wishlist'))

    return render_template('add_wishlist.html')


# =========================
# VIEW WISHLISTS
# =========================

@app.route('/view_wishlists')
def view_wishlists():

    try:

        connection = get_db_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT * FROM wishlist
            ORDER BY id DESC
        """

        cursor.execute(query)

        wishlists = cursor.fetchall()

        cursor.close()

        connection.close()

        return render_template(
            'view_wishlists.html',
            wishlists=wishlists
        )

    except Exception as e:

        flash(str(e), 'danger')

        return redirect(url_for('index'))


# =========================
# DELETE SECRET SANTA
# =========================

@app.route('/delete_assignment/<int:id>', methods=['POST'])
def delete_assignment(id):

    try:

        connection = get_db_connection()

        cursor = connection.cursor()

        query = "DELETE FROM secret_santa WHERE id = %s"

        cursor.execute(query, (id,))

        connection.commit()

        cursor.close()

        connection.close()

        flash("Assignment Deleted Successfully!", 'success')

    except Exception as e:

        flash(str(e), 'danger')

    return redirect(url_for('view_secret_santa'))


# =========================
# DELETE WISHLIST
# =========================

@app.route('/delete_wishlist/<int:id>', methods=['POST'])
def delete_wishlist(id):

    try:

        connection = get_db_connection()

        cursor = connection.cursor()

        query = "DELETE FROM wishlist WHERE id = %s"

        cursor.execute(query, (id,))

        connection.commit()

        cursor.close()

        connection.close()

        flash("Wishlist Deleted Successfully!", 'success')

    except Exception as e:

        flash(str(e), 'danger')

    return redirect(url_for('view_wishlists'))


# =========================
# CLEAR ALL ASSIGNMENTS
# =========================

@app.route('/clear_all_assignments', methods=['POST'])
def clear_all_assignments():

    try:

        connection = get_db_connection()

        cursor = connection.cursor()

        query = "DELETE FROM secret_santa"

        cursor.execute(query)

        connection.commit()

        cursor.close()

        connection.close()

        flash("All Assignments Cleared!", 'success')

    except Exception as e:

        flash(str(e), 'danger')

    return redirect(url_for('view_secret_santa'))


# =========================
# MAIN
# =========================

if __name__ == '__main__':

    init_database()

    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
