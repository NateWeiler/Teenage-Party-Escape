from flask import render_template, flash, redirect
from app import app
from .forms import InputField, LoginForm

@app.route('/login')
def login():
    form = InputField()
    return render_template('login.html', title='Login')

@app.route('/intro')
def intro():
    return render_template('intro.html', title='Introduction')


@app.route('/basement', methods=['GET','POST'])
def basement():
    form = InputField()
    return render_template('basement.html', title='Basement')

@app.route('/screwed')
def screwed():
    return render_template('screwed.html', title='You have died.')

@app.route('/find_parents')
def find_parents():
    return render_template('find_parents.html', title='Find Parents')

@app.route('/bedroom')
def bedroom():
    return render_template('bedroom.html', title='Bedroom')

@app.route('/window')
def window():
    return render_template('window.html', title='Window')

@app.route('/garage')
def garage():
    return render_template('garage.html', title='Garage')

@app.route('/passcode')
def passcode():
    return render_template('passcode.html',title="Passcode")

@app.route('/meet_friend')
def meet_friend():
    return render_template('meet_friend.html',title="Meet Friend")

@app.route('/arrive_to_party')
def arrive_to_party():
    return render_template('arrive_to_party.html',title="Arrive to Party")

@app.route('/party')
def party():
    return render_template('party.html',title="Party")

@app.route('/talk_to_girl')
def talk_to_girl():
    return render_template('talk_to_girl.html',title="Talk to Girl")

@app.route('/phone_number')
def phone_number():
    return render_template('party.html',title="Phone_number")

@app.route('/party_over')
def party_over():
    return render_template('party_over.html',title="Phone_number")

@app.route('/success')
def success():
    return render_template('success.html',title=" Congrats")
