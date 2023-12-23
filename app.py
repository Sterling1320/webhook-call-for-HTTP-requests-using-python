from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database connection configuration
db = mysql.connector.connect(
    host="localhost",    # MySQL server hostname
    user="root",         # MySQL username
    password="iambt1013",  # MySQL password
    database="chatbot"   # MySQL database name
)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    print(data)
    userInput = data['queryResult']['queryText']
    segments = userInput.split()
    for segments in segments:
      if segments.isdigit() and len(segments) == 10:
        student_id = segments
        break
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student_info WHERE prn = %s", (student_id,))
    student = cursor.fetchone()

    if student is None:
        response = {'fulfillmentText': 'No student found with the provided ID.'}
    else:
        response = {
            'fulfillmentText': f"PRN: {student['prn']}\nFirst Name: {student['fname']}\nLast Name: {student['lname']}"
        }

    cursor.close()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
