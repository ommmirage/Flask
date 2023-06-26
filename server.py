from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<string:page_name>")
def page_name(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            email = request.form['email']
            subject = request.form['subject']
            message = request.form['message']
            write_to_csv(email, subject, message)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'Something went wrong.'

def write_to_file(email, subject, message):
    # Mode a means append
    with open('database.txt', mode='a') as database:
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(email, subject, message):
    with open('database.csv', mode='a') as database:
        csv_writer = csv.writer(database, delimiter = ',', quotechar = '\'',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
