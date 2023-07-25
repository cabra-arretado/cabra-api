""" Entities for the application """
from datetime import datetime
from pydantic import BaseModel, EmailStr,SecretStr


class BaseEntity(BaseModel):
	""" The entity to rule them all  """
	class Config:
		""" Pydantic configuration """
		arbitrary_types_allowed = True

class UserPreCreated(BaseEntity):
	""" Base user entity """
	email: EmailStr
	# TODO: encrypt password
	password: SecretStr

class User(UserPreCreated):
	""" User entity with id """
	id: int

class ProductBase(BaseEntity):
	""" Base product entity """
	name: str
	description: str
	price: float


class OrderBase(BaseEntity):
	""" Base order entity """
	user: UserPreCreated
	date_created: datetime
