from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy database engine (adjust the database URL as needed)
DATABASE_URL = "sqlite:///restaurant_reviews.db"
engine = create_engine(DATABASE_URL)

# SQLAlchemy base class for declarative models
Base = declarative_base()

# Restaurant model
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # one-to-many relationship with Review
    reviews = relationship('Review', back_populates='restaurant')

    def customers(self):
        # List comprehension to extract customers from reviews
        return [review.customer for review in self.reviews]

    def reviews(self):
        # Returns a collection of all the reviews for the restaurant
        return self.reviews

# Customer model
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # one-to-many relationship with Review
    reviews = relationship('Review', back_populates='customer')

    def restaurants(self):
        # List comprehension to extract restaurants from reviews
        return [review.restaurant for review in self.reviews]

    def reviews(self):
        # Returns a collection of all the reviews that the customer has left
        return self.reviews

# Review model
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    rating = Column(Integer)

    # many-to-one relationship with Restaurant
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')

    # many-to-one relationship with Customer
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='reviews')

    def customer(self):
        return self.customer 

    def restaurant(self):
        return self.restaurant  

# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
