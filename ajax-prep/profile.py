import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    return render_template("index.html")



@app.route('/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    user_name = request.form['name']
    user_age = request.form.get('age')
    user_occupation = request.form.get('occupation')
    user_salary = request.form.get('salary')
    user_edu = request.form.get('education')
    user_state = request.form.get('state')
    user_city = request.form.getlist('city')
    user_garden = request.form.get('garden')
    user_tv = request.form.get('tv')

    # TODO: get the values from the rest of the form
    # Add them to jsonify

    return jsonify({'user_name': user_name, 'user_age': age, 'user_occupation': user_occupation, 'user_salary': user_salary, 'user_edu': user_edu, 'user_state': user_state, 'user_city': user_city, 'user_garden': user_garden, 'user_tv': user_tv})


if __name__ == "__main__":
    app.run(debug=True)
