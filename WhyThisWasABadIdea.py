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
        response = get_club_info()
    # Check if user input is about library information
    elif "library" in userInput.lower() or "book" in userInput.lower():
        response = get_library_info(data)
    else:
        # If the user input is not about clubs or library, you can add more conditions or handle other cases here
        response = {'fulfillmentText': 'Sorry, I can only provide information about clubs and library at the moment.'}

    return jsonify(response)

def get_club_info():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT Cname, Chead, club_room, contact_number FROM clubs")
    clubs = cursor.fetchall()
    cursor.close()

    if not clubs:
        return {'fulfillmentText': 'No club information found.'}
    else:
        club_info = "\n".join([f"Club: {club['Cname']}, Head: {club['Chead']}, Room: {club['club_room']}, Contact: {club['contact_number']}" for club in clubs])

        # Adding a small paragraph to the response
        return {
            'fulfillmentText': f"Deogiri College offers a variety of clubs where interested students can join and meet with like-minded people for interesting extracurricular activities. Here is the list of all available Clubs in the college and their respective club heads:\n\n\n\n{club_info}"
        }

def get_library_info(data):
    # Extract parameters from the user's input
    parameters = data['queryResult']['parameters']
    prn_number = parameters.get('prnNumber')

    if not prn_number:
        return {'fulfillmentText': 'Please provide your PRN for book information.'}

    # Query the library table for issued books under the specified PRN
    cursor = db.cursor(dictionary=True)
    query = f"SELECT prn, issued_book_id, bookname, author, branch, issued_date, due_date FROM library WHERE prn = {prn_number}"
    cursor.execute(query)
    books = cursor.fetchall()
    cursor.close()

    if not books:
        return {'fulfillmentText': 'No books found under the provided PRN.'}
    else:
        book_info = "\n".join([f"Book ID: {book['issued_book_id']}, Book Name: {book['bookname']}, Author: {book['author']}, Branch: {book['branch']}, Issued Date: {book['issued_date']}, Due Date: {book['due_date']}" for book in books])

        # Adding a small paragraph to the response
        return {
            'fulfillmentText': f"Here are the details of the books issued under PRN {prn_number}:\n\n\n\n{book_info}"
        }

if __name__ == '__main__':
    app.run(debug=True)
