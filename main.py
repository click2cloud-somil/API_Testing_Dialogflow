from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "How Are You"

@app.route('/blog')
def blog():
    return ("open your blog")

@app.route('/doctors')
def get_doctors():
    doctors = [
        {'id':1, 'Name':'Somil Mehta', 'Contact Number': 7829359892, 'Address': 'Behind Jaiswal Chitramandir'},
        {'id':2, 'Name':'Shreya Dubey','Contact Number': 9713259882,'Address': 'Near Mahila Bank'},
        {'id':3, 'Name':'Abhijit Meshram','Contact Number': 8055071497,'Address':'Kamptee Road'},
        {'id':4, 'Name':'Nishant Kohale','Contact Number':9834988102,'Address':'Near Nursing Home'}
        ]
    return jsonify(doctors)


#app.run(port=5000,debug=True)
if __name__ == '__main__':
    app.run(debug=True)
