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

# Create a table
engine.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255)")

