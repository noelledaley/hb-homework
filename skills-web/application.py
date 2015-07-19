from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def start_application():
    return render_template('application-form.html')

@app.route('/application', methods=["POST"])
def confirm_application():
    first_nm = request.form.get("first_name")
    salary = request.form.get("salary_requirement")
    job_app = request.form.get("job")

    return render_template('confirmation.html', first_name = first_nm, salary_requirement = salary, job = job_app)

if __name__ == '__main__':
    app.run(debug=True)
