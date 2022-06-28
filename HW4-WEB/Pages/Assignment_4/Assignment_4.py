from flask import Blueprint, render_template
import mysql.connector
from flask import request, redirect
from flask import jsonify
import requests

assignment_4 = Blueprint('assignment_4', __name__,
                         static_folder='static',
                         template_folder='template')


@assignment_4.route('/Assignment_4')
def assignment4_func():
    query = 'select * from users'
    user_list = interact_db(query, query_type='fetch')
    return render_template('Assignment_4.html', users=user_list)


@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    query = 'select * from users'
    user_list = interact_db(query, query_type='fetch')
    for user in user_list:
        if name == user.name:
            query_1 = 'select * from users'
            user_list1 = interact_db(query=query_1, query_type='fetch')
            return render_template('Assignment_4.html',
                                   message2='This user already exist!',
                                   users=user_list1)
        else:
            if (len(name) == 0):
                query_1 = 'select * from users'
                user_list1 = interact_db(query=query_1, query_type='fetch')
                return render_template('Assignment_4.html', users=user_list1, message2='Please fill the fields!')
            else:
                query = "INSERT INTO users(name,lastname,email) VALUES ('%s','%s','%s')" % (name, lastname, email)
                interact_db(query=query, query_type='commit')
                query_1 = 'select * from users'
                user_list1 = interact_db(query=query_1, query_type='fetch')
                return render_template('Assignment_4.html',
                                       message2='User added successfully!',
                                       users=user_list1)


# update
@assignment_4.route('/update_user', methods=['POST'])
def update_user():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    if lastname != "" and email != "":
        query = "UPDATE users SET lastname='%s',email='%s' WHERE name='%s' " % (lastname, email, name)
        interact_db(query=query, query_type='commit')
        query_1 = 'select * from users'
        user_list = interact_db(query=query_1, query_type='fetch')
        return render_template('Assignment_4.html',
                               message1='lastname and Email is updated!',
                               users=user_list)
    elif (lastname != "" and email == ""):
        query = "UPDATE users SET lastname='%s' WHERE name='%s' " % (lastname, name)
        interact_db(query=query, query_type='commit')
        query_1 = 'select * from users'
        user_list = interact_db(query=query_1, query_type='fetch')
        return render_template('Assignment_4.html',
                               message1='lastname is updated!',
                               users=user_list)
    elif (lastname == "" and email != ""):
        query = "UPDATE users SET email='%s' WHERE name='%s' " % (email, name)
        interact_db(query=query, query_type='commit')
        query_1 = 'select * from users'
        user_list = interact_db(query=query_1, query_type='fetch')
        return render_template('Assignment_4.html',
                               message1='Email is updated!',
                               users=user_list)
    else:
        query_1 = 'select * from users'
        user_list = interact_db(query=query_1, query_type='fetch')
        return render_template('Assignment_4.html',
                               message1='please fill the fields!',
                               users=user_list)


@assignment_4.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    query_1 = 'select * from users'
    user_list = interact_db(query=query_1, query_type='fetch')
    return render_template('Assignment_4.html',
                           message='User Deleted!',
                           users=user_list)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    # CREATE, UPDATE, DELETE
    if query_type == 'commit':
        connection.commit()
        return_value = True

        # READ
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment_4.route('/assignment_4/users')
def users_response():
    query = 'select * from users'
    query_list = interact_db(query, query_type='fetch')
    return jsonify(query_list)


@assignment_4.route('/assignment_4/outer_source')
def outer_source():
    return render_template('outer_source.html')


@assignment_4.route('/assignment_4/outer_source/fetch_backend')
def outer_source_fetch():
    user_id = request.args['user_id']
    res = requests.get(f"https://reqres.in/api/users/{user_id}")
    return render_template('outer_source.html', request_data=res.json()['data'])


@assignment_4.route('/assignment_4/restapi_users', defaults={'user_id': 1})
@assignment_4.route('/assignment_4/restapi_users/<int:user_id>')
def restapi_users(user_id):
    query = "select * from users WHERE id='%s';" % user_id
    query_list = interact_db(query, query_type='fetch')
    if len(query_list) != 0:
        message = ''
        response = {'user_id': user_id}
        usersDetails = query_list
    else:
        message = {'The user_id is not exist': user_id}
        response = {}
        usersDetails = query_list

    response = jsonify(message, response, usersDetails)
    return response
