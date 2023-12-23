from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('medicine.db')
c = conn.cursor()

# Create Medicines table
c.execute("""
   CREATE TABLE IF NOT EXISTS Medicines (
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       dosage TEXT
   )
""")

# Create Schedule table
c.execute("""
   CREATE TABLE IF NOT EXISTS Schedule (
       id INTEGER PRIMARY KEY,
       time TEXT NOT NULL,
       medicine_id INTEGER,
       FOREIGN KEY(medicine_id) REFERENCES Medicines(id)
   )
""")

# Insert data into Medicines table
c.executemany("""
   INSERT INTO Medicines (name, dosage) VALUES (?, ?)
""", [
   ('Syndopa', '110'),
   ('Ropark', '1 mg'),
   ('Ropark', '0.5 mg'),
   ('Parkitidin', '1 mg'),
   ('Xafinact', '50 mg'),
   ('Aten', '25 mg'),
   ('Glucomet GP', '2'),
   ('Gluxit S', '10/100'),
   ('Duzela M', '30'),
   ('Parkitidin', '1 mg'),
   ('Ropark', '1 mg'),
   ('Ropark', '0.5 mg'),
   ('Syndopa', '110'),
   ('Ropark', '1 mg'),
   ('Ropark', '0.5 mg'),
   ('Syndopa', '110'),
   ('Catchnil', None),
   ('Duzela M', '30'),
   ('Ecospirin AV', '75'),
   ('Glycomet GP', '2'),
   ('Zolcalm', '5 mg'),
   ('Syndopa CR', '125'),
   ('Rivotril', None)
])

# Insert data into Schedule table
c.executemany("""
   INSERT INTO Schedule (time, medicine_id) VALUES (?, ?)
""", [
   ('08:00 AM', 1),
   ('08:00 AM', 2),
   ('08:00 AM', 3),
   ('08:00 AM', 4),
   ('08:00 AM', 5),
   ('09:30 AM', 6),
   ('09:30 AM', 7),
   ('09:30 AM', 8),
   ('01:00 PM', 9),
   ('01:00 PM', 4),
   ('01:00 PM', 2),
   ('01:00 PM', 3),
   ('01:00 PM', 1),
   ('06:00 PM', 2),
   ('06:00 PM', 3),
   ('06:00 PM', 1),
   ('06:00 PM', 10),
   ('09:30 PM', 9),
   ('09:30 PM', 11),
   ('09:30 PM', 7),
   ('10:30 PM', 12),
   ('10:30 PM', 1),
   ('10:30 PM', 13)
])

# Commit changes and close connection
conn.commit()
conn.close()

@app.route('/medicine', methods=['POST'])
def create_medicine():
  # Code to add a new medicine

@app.route('/medicine/<int:id>', methods=['GET'])
def read_medicine(id):
  # Code to read a medicine

@app.route('/medicine/<int:id>', methods=['PUT'])
def update_medicine(id):
  # Code to update a medicine

@app.route('/medicine/<int:id>', methods=['DELETE'])
def delete_medicine(id):
  # Code to delete a medicine

if __name__ == '__main__':
  app.run(debug=True)
