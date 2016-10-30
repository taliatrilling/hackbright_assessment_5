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
# Part 2: Write queries


# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like ("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    year_models = db.session.query(Model.name, Model.brand_name, Brand.headquarters).distinct(Model.id).filter(Model.year == year).outerjoin(Brand).all()

    for name, brand_name, headquarters in year_models:
    	if headquarters is not None:
    		print name, brand_name, headquarters + "\n"
    	else:
			print name, brand_name, "-" + "\n"


def get_brands_summary():
	'''Prints out each brand name, and each model name for that brand
	using only ONE database query.'''
	brand_summary = db.session.query(Brand.name, Model.name).distinct(Model.name).filter(Model.brand_name == Brand.name).all()

	brands = {}
	for item in brand_summary:
		if item[0] in brands.keys():
			existing_models = brands[item[0]]
			existing_models.append(item[1])
			brands[item[0]] = existing_models
		else:
			brands[item[0]] = [item[1]]

	for key, value in brands.items():
		print "\nBrand name:" + key
		for item in value:
			print item

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# The above query will return a BaseQuery object of the brand with the name Ford. However, because our query 
# doesn't have something on it to specify which records to fetch (like . all()), what we can do with the 
# object is somewhat limited.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# An association table is the table that connects the two tables of interest in a "many to many" data model. Unlike a 
# middle table, the fields in an association table don't represent anything the user is actually interested in, and 
# instead act to enable the relationship between the other tables. 

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
	"""Takes in an string, returns a list of objects that are the brands whose names contain or are equal to the string"""
	objects = []
	names = db.session.query(Brand.name).distinct(Brand.name).filter((Brand.name == mystr) | (Brand.name.like("%" + mystr + "%"))).all()

	for name in names:
		objects.append(name[0])

	return objects

def get_models_between(start_year, end_year):
    """Takes in two integers of years and returns a list of the models with years that fall between them"""
    objects = []
    names = db.session.query(Model.name).distinct(Model.name).filter(Model.year >= start_year, Model.year < end_year).all()

    for name in names:
    	objects.append(name[0])

    return objects
 






