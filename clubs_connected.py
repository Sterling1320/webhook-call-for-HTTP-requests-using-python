from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database connection configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iambt1013",
    database="chatbot"
)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    print(data)

    userInput = data['queryResult']['queryText']
    
    # Check if user input is about club information
    if "club" in userInput.lower():
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT Cname, Chead, club_room, contact_number FROM clubs")
        clubs = cursor.fetchall()
        cursor.close()

        if not clubs:
            response = {'fulfillmentText': 'No club information found.'}
        else:
            club_info = "\n".join([f"Club: {club['Cname']}, Head: {club['Chead']}, Room: {club['club_room']}, Contact: {club['contact_number']}" for club in clubs])

            # Adding a small paragraph to the response
            response = {
                'fulfillmentText': f"Deogiri College offers a variety of clubs where interested students can join and meet with like-minded people for interesting extracurricular activities. Here is the list of all available Clubs in the college and their respective club heads:\n\n\n\n{club_info}"
            }
    else:
        # If the user input is not about club information, you can add more conditions or handle other cases here
        response = {'fulfillmentText': 'Sorry, I can only provide information about clubs at the moment.'}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
