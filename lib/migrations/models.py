from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define the base model
Base = declarative_base()

# Define the Restaurant model
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Establish the one-to-many relationship between Restaurant and Review
    reviews = relationship('Review', back_populates='restaurant')

# Define the Customer model
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Establish the one-to-many relationship between Customer and Review
    reviews = relationship('Review', back_populates='customer')

# Define the Review model
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    comment = Column(String)

    # Establish the many-to-one relationship with Restaurant and Customer
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    # Define back references to access Restaurant and Customer objects
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

# Create the database tables
Base.metadata.create_all(engine)