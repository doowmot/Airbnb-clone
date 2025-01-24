import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# GET /spaces/index
@app.route('/spaces', methods=['GET'])
def get_list_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('spaces/index.html', spaces=spaces)


# GET /spaces/new
@app.route('/spaces/new', methods=['GET'])
def get_a_new_space():
    return render_template('spaces/new.html')


# GET /spaces/<id>  --- geet a single space
@app.route('/spaces/<int:id>', methods=['GET'])
def get_a_single_space(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('spaces/show_single.html', space=space)


# POST /spaces/new  --- submit a new space
@app.route('/spaces', methods=['POST'])
def post_submit_a_new_space():
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    date_repository = DateRepository(connection)


    space = Space(
        None,
        request.form['name'],
        request.form['description'],
        int(request.form['price']),
        1
    )
    space_repository.create(space)

    available_from = request.form['available_from']
    available_to = request.form['available_to']
    
    date_repository.create_availability_range(available_from, available_to, space_id)

    spaces = space_repository.all()
    return render_template('spaces/index.html', spaces=spaces)

# GET /login
@app.route('/login', methods=['GET'])
def get_login():
    return render_template('authentication/login.html')

# GET /signup
@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('authentication/signup.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
