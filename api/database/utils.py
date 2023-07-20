import os
from dotenv import load_dotenv

load_dotenv()

def get_env(test_env: dict = None):
	"""
	Get environment variables, if dict test_env provided use that instead
	"""
	if test_env:
		return test_env
	return os.environ
