""" Entities for the application """
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, SecretStr
from uuid import UUID, uuid4


class BaseEntity(BaseModel):
	""" The entity to rule them all  """
	uuid: UUID = Field(default_factory=uuid4, alias="id", index=True, primary_key=True)

	class Config:
		""" Pydantic configuration """
		arbitrary_types_allowed = True

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
	date_created: datetime
