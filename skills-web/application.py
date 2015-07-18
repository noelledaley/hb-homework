from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start_application():
    return render_template('application-form.html')

if __name__ == '__main__':
    app.run(debug=True)
