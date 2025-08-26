from sqlalchemy import (
    DateTime,
    Numeric,
    Text,
    Column,
    String,
    Integer,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# Tabela Usuários
class User:
    __tablename__ = "users"

    # Keys
    id = Column("id", Integer, primary_key=True, autoincrement=True)

    # Campos
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    cpf = Column("cpf", String, nullable=False)
    phone = Column("phone", String)
    active = Column("active", Boolean, default=true)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, id, name, email, password, cpf, phone, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.phone = phone
        self.active = active
        self.admin = admin


# Tabela de Espaço Esportivo
class sport_center(Base):
    __tablename__ = "facilities"

    # Keys
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column("user_id" Integer, ForeignKey("users.id"), nullable=False)

    # Campos
    name = Column("name", String, nullable=False)
    cnpj = Column("cnpj", String, nullable=False)
    latitude = Column("latitude", Numeric(9, 6), nullable=False)
    longitude = Column("longitude", Numeric(9, 6), nullable=False)
    photo_path = Column("photo_path", String)
    description = Column("description", String)


# Tabela de avaliações
class Review(Base):
    __tablename_ = "reviews"

    # Keys
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    field_id = Column("field_id", String, ForeignKey("fields.id"), nullable=False)
    user_id = Column("user_id", String, ForeignKey("users.id"), nullable=False)

    #Campos
    rating = Column("rating", nullable=False)
    comment = Column("comment",)
    created_at = Column("created_at", DateTime) 


# Tabela de campos
class Field(Base):
    __tablename_ = "fields"

    # Keys
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    facility_id = Column("facility_id", Integer, ForeignKey("facilities.id"), nullable=False)

    # Campos
    name = Column("name", String, nullable=False)
    field_type = Column("type", String, nullable=False)
    price_per_hour = Column("price_per_hour", Numeric, nullable=False)
    photo_path = Column("photo_path", String)
    description = Column("description", Text)
 

# Tabela de Disponibilidades
class Availability(Base):
    __tablename_ = "availabilities"

    # Keys
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    field_id = Column("field_id", String, ForeignKey("fields.id"), nullable=False)

    # Campos
    day_of_week = Column("day_of_week", Integer, nullable=False)
    start_time = Column("start_time", DateTime, nullable=False)
    end_time = Column("end_time", DateTime, nullable=False)


# Tabela de Reservas de campo
class Booking(Base):
    __tablename_ = "bookings"

    # Keys
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column("user_id" Integer, ForeignKey("users.id"), nullable=False)
    field_id = Column("field_id", String, ForeignKey("fields.id"), nullable=False)
    
    # Campos
    day_of_week = Column("day_of_week", Integer, nullable=False)
    start_time = Column("start_time", DateTime, nullable=False)
    status = Column("status", String, default="pending")