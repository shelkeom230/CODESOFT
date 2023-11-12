from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="task5_codesoft"
)

cursor = db.cursor()

# Create a table for contacts
create_table_query = """
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL
)
"""

# run the query
cursor.execute(create_table_query)
db.commit()

# create end points


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_contact', methods=['POST'])
def add_contact():
    contact_data = request.get_json()
    contact_name = contact_data.get('name')
    contact_number = contact_data.get('contactnumber')
    address = contact_data.get('address')

# insert into database
    insert_query = "INSERT INTO contacts (name, contact_number, address) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (contact_name, contact_number, address))
    db.commit()

    return jsonify({'message': 'Contact added successfully'})


@app.route('/get_contacts', methods=['GET'])
def get_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    return jsonify([{'id': id, 'name': name, 'contact_number': contact_number, 'address': address} for id, name, contact_number, address in contacts])


@app.route('/edit_contact/<int:contact_id>', methods=['PUT'])
def edit_contact(contact_id):
    new_name = request.get_json().get('name')

    update_query = "UPDATE contacts SET name = %s WHERE id = %s"
    cursor.execute(update_query, (new_name, contact_id))
    db.commit()

    return jsonify({'message': 'Contact updated successfully'})


@app.route('/delete_contact/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    delete_query = "DELETE FROM contacts WHERE id = %s"
    cursor.execute(delete_query, (contact_id,))
    db.commit()

    return jsonify({'message': 'Contact deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
