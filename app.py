import pyrebase

config = {
	"apiKey": "YOUR_API_KEY_WILL_COME_HERE",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": ""
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()	#initialize the database.


from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':

			name = request.form['name']
			db.child("todo").push(name)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('index.html', t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		return render_template('index.html')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
