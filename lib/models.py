from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from seed import session


# SQLAlchemy database engine
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

    @classmethod
    def fanciest(cls):
        # Find the restaurant with the highest price
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        # Returns a list of formatted review strings for the restaurant
        return [review.full_review() for review in self.reviews]

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

    def full_name(self):
        # Returns the full name of the customer, with the first name and last name joined.
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Finds the restaurant with the highest star rating from this customer
        highest_rating = 0
        favorite_restaurant = None

        for review in self.reviews:
            if review.rating > highest_rating:
                highest_rating = review.rating
                favorite_restaurant = review.restaurant

        return favorite_restaurant

    def add_review(self, restaurant, rating):
        # Creates a new review for the provided restaurant with the given rating
        review = Review(restaurant=restaurant, customer=self, rating=rating)
        session.add(review)

    def delete_reviews(self, restaurant):
        # Removes all reviews for a specific restaurant
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)

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

    def full_review(self):

        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.rating} stars"
