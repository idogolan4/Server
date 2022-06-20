from flask import Flask, redirect, url_for, request
from flask import render_template
from datetime import timedelta
from flask import session, jsonify

app = Flask(__name__)

app.secret_key = '1234'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=20)


@app.route('/')
@app.route('/FirstPage')
def FirstPage():
    return render_template('FirstPage-1.HTML')


@app.route('/ContactPage')
def ContactPage():
    return render_template('ContactPage-1.html')


@app.route('/FAQ')
def FAQ():  # put application's code here
    return render_template('FAQ-1.html')


@app.route('/assignment3_1')
def assignment3_1():
    curr_user = {'firstname': "Ido", 'lastname': "Golan"}
    # curr_user='' #will write Guest
    return render_template('assignment3_1.html',
                           curr_user=curr_user,
                           hobbies=['football', 'netflix', 'beach', 'traveling', 'friends', 'PS'])


Users_dict = {'ido': {'lastname': "golan", 'email': "idogolan@gmail.com"},
              'omer': {'lastname': "azulay", 'email': "omerazulay@gmail.com"},
              'maor': {'lastname': "minay", 'email': "maorminay@gmail.com"},
              'shahaf': {'lastname': "yamin", 'email': "shahafyamin@gmail.com"},
              'dor': {'lastname': "nudelman", 'email': "dornudelman@gmail.com"}}

registration_dict = {'idogolan': {'password': "1111"},
                     'omerazulay': {'password': "2222"},
                     'maorminay': {'password': "3333"}}


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2():
    if 'name' in request.args:
        name = request.args['name']
        lastname = request.args['lastname']
        email = request.args['email']
        if name in Users_dict:
            return render_template('‘assignment3_2.html',
                                   name=name,
                                   lastname=lastname,
                                   email=email)

        else:
            return render_template('‘assignment3_2.html',
                                   message='User not found.',
                                   Users_dict=Users_dict)

    if 'username' in request.form:
        user_name = request.form['username']
        password = request.form['password']
        if user_name in registration_dict:
            return render_template('‘assignment3_2.html',
                                   message2='Username is already taken, please try again')
        else:
            registration_dict[user_name] = password
            print(registration_dict.keys())
            session['username'] = user_name
            print(password)
            return render_template('‘assignment3_2.html',
                                   user_name=user_name,
                                   password=password,
                                   registration_dict=registration_dict)
    else:
        return render_template('‘assignment3_2.html')


@app.route('/Logout')
def Logout_func():
    session.clear()
    return redirect(url_for('assignment3_2'))


if __name__ == '__main__':
    app.run(debug=True)
