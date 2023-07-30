from .utils import get_env

import sqlalchemy

test_env = {
"DB_HOST": "localhost",
"DB_PORT": 3306,
"DB_USERNAME": "root",
"DB_PASSWORD": "123456",
"DB_DATABASE": "cabra-platform",
}
env = get_env(test_env)

# Create a connection to the database
engine = sqlalchemy.create_engine(f"mysql+pymysql://{env.get('DB_USERNAME')}:{env.get('DB_PASSWORD')}@{env.get('DB_HOST')}:{env.get('DB_PORT')}/{env.get('DB_DATABASE')}")

# Create a user and insert it on the table
def insert_user(email, password):
	with engine.connect() as conn:
		insert_stm = sqlalchemy.text(f"INSERT INTO users (email, password) VALUES ('{email}', '{password}')")
		conn.execute(insert_stm)
		conn.commit()
	# return get_user(email)

# Get a user from the database
def get_user(email: str):
	get_stm = sqlalchemy.text(f"SELECT * FROM users WHERE email = '{email}'")
	with engine.connect() as conn:
		user = conn.execute(get_stm).fetchone()
	return user
