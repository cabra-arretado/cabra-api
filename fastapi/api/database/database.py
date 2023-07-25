from utils import get_env

import sqlalchemy

test_env = {
"DB_HOST": "localhost",
"DB_PORT": 3306,
"DB_USERNAME": "root",
"DB_PASSWORD": "password",
"DB_DATABASE": "customers",
}
env = get_env(test_env)

# Create a connection to the database
engine = sqlalchemy.create_engine(f"mysql+pymysql://{env.get('DB_USERNAME')}:{env.get('DB_PASSWORD')}@{env.get('DB_HOST')}:{env.get('DB_PORT')}/{env.get('DB_DATABASE')}")

# Create a user and insert it on the table
def create_user(email, password):
	with engine.connect() as conn:
		conn.execute(f"INSERT INTO users (email, password) VALUES ('{email}', '{password}')")


