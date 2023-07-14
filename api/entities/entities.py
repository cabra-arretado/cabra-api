""" Entities for the application """
from datetime import Date
from pydantic import BaseModel, EmailStr, SecretStr
from uuid import UUID


class BaseEntity(BaseModel):
	""" The entity to rule them all  """
	uuid: UUID


class UserBase(BaseEntity):
	""" Base user entity """
	email: EmailStr
	# TODO: encrypt password
	password: SecretStr


class ProductBase(BaseEntity):
	""" Base product entity """
	name: str
	description: str
	price: float


class OrderBase(BaseEntity):
	""" Base order entity """
	user: UserBase
	date_created: Date
