"""Sample file demonstrating SQLAlchemy joins & relationships."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions


class Employee(db.Model):
    """Employee."""

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    state = db.Column(db.String(2), nullable=False, default='CA')
    fav_color = db.Column(db.String(20), nullable=True, default='Unknown')
    dept_code = db.Column(db.Integer, db.ForeignKey('departments.dept_code'))

    dept = db.relationship('Department',
                           backref=db.backref('employees', order_by=id)
                           )

    def __repr__(self):
        return "<Employee id=%d name=%s>" % (self.id, self.name)


class Department(db.Model):
    """Department. A department has many employees."""

    __tablename__ = "departments"

    dept_code = db.Column(db.String(5), primary_key=True)
    dept = db.Column(db.String(20), nullable=True, unique=True)
    phone = db.Column(db.String(20))

    def __repr__(self):
        return "<Department id=%s name=%s>" % (self.dept_code, self.dept)


def example_data():
    """Create some sample data."""

    ded = Department(dept_code='ed', dept='Education', phone='555-1000')
    dad = Department(dept_code='admin', dept='Administration', phone='555-2222')
    dpt = Department(dept_code='pt', dept='Part-Time', phone='555-9999')
    dot = Department(dept_code='oth', dept='Other', phone='555-3333')

    joel = Employee(name='Joel Burton', dept=ded, fav_color='orange')
    cynthia = Employee(name='Cynthia Dueltgen', dept=ded, fav_color='purple')
    rachelt = Employee(name='Rachel Thomas', dept=ded)
    katie = Employee(name='Katie Lefevre', dept=ded, fav_color='all of them')
    meggie = Employee(name='Meggie Mahnken', dept=ded, fav_color='black')
    heather = Employee(name='Heather Bryant', dept=ded, fav_color='purple')
    kristen = Employee(name='Kristen McClure', dept=ded, fav_color='orange')
    lavinia = Employee(name='Lavinia Karl', dept=ded)
    denise = Employee(name='Denise Wiedl', dept=ded)
    david = Employee(name='David Phillips', dept=dad)
    angie = Employee(name='Angie Chang', dept=dad)
    stefan = Employee(name='Stefan Gomez', dept=dad)
    laura = Employee(name='Laura Gillen', dept=dad)
    paria = Employee(name='Paria Rajai', dept=dad)
    wendy = Employee(name='Wendy Saccuzzo', dept=dot)
    dori = Employee(name='Dori Grant', dept=dot)
    kari = Employee(name='Kari Burge', dept=dot, fav_color='orange')
    rachelw = Employee(name='Rachel Walker', dept=dpt)
    anna = Employee(name='Anna Akullian', dept=dpt)
    jumal = Employee(name='Jumal Qazi', dept=dpt, fav_color='orange')
    lindsay = Employee(name='Lindsay Cade', fav_color='purple')
    balloonicorn = Employee(name='Balloonicorn', fav_color='pink')


    db.session.add_all([ded, dad, dpt, dot, joel, cynthia, rachelt, katie, meggie,
                        heather, kristen, lavinia, denise, david, angie, stefan,
                        laura, paria, wendy, dori, kari, rachelw, anna, jumal, lindsay])
    db.session.commit()


def all_employees_nav():
    """Show all employees."""

    # This is inefficient, as it makes a query for each department!

    emps = db.session.query(Employee)
    emps_with_dept = emps.filter(Employee.dept_code.isnot(None))

    for emp in emps_with_dept.all():
        print emp.name, emp.dept.dept, emp.dept.phone


def all_employees_join():
    """Show employees with a join."""

    emps = db.session.query(Employee.name,
                            Department.dept,
                            Department.phone).join(Department)

    for name, dept, phone in emps.all():
        print name, dept, phone


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."

    db.create_all()
    example_data()
