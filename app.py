import gspread
from flask import Flask, render_template, request

gc = gspread.service_account(filename='flask-profile.json')
sh= gc.open('flask-profile')

shProfile = sh.get_worksheet(0)
shContact = sh.get_worksheet(1)
shContact.append_row(['Bob', 'bob@gmail.com', ' hi'])



app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        shContact.append_row([request.form['name'], request.form['email'], request.form['message']])


    profile = {
        'about':shProfile.acell('B1').value,
        'interests':shProfile.acell('B2').value,
        'experience':shProfile.acell('B3').value,
        'education':shProfile.acell('B4').value,
    }
    return render_template('index.html', profile=profile)

@app.route('/contact')
def contact():
    return render_template('contact.html')

