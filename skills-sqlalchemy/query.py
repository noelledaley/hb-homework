"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.discontinued.is_(None), Brand.founded == 1903).all()

# Get all brands with that are either discontinued or founded before 1950.

Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    l = db.session.query(Brand.name, Brand.headquarters, Model.name).join(Model).filter(Model.year == year).all()

    for brand, hq, name in l:
        print name, brand, hq

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    l = db.session.query(Brand.name, Model.name).join(Model).order_by(Brand.name).all()

    brands = {}

    for brand, model in l:
        if not brands.get(brand):
            brands[brand] = [model]
        else:
            brands[brand].append(model)

    brands = {}

    print brands

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Design a function in python that takes in any string as parameter, and returns a list of objects that are brands whose name contains or is equal to the input string."""

    q = Brand.query.filter(db.or_(Brand.name == mystr, Brand.name.like('%\%s%' % mystr))).all()

    # TODO: figure out proper string substitution

    return q


def get_models_between(start_year, end_year):
    """Design a function that takes in a start year and end year (two integers), and returns a list of objects that are models with years that fall between the start year and end year."""

    q = Model.query.filter(Model.year > start_year, Model.year < end_year).all()

    return q

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# A Flask-SQLAlchemy query object.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table joins tables with a many to many relationship.
