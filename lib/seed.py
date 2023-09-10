from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# SQLAlchemy database engine (adjust the database URL as needed)
DATABASE_URL = "sqlite:///restaurant_reviews.db"
engine = create_engine(DATABASE_URL)

# session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# data for restaurants
restaurants_data = [
    {"name": "Fish & Grill", "price": 330},
    {"name": "Burgers Mania", "price": 240},
    {"name": "Snacks Kings", "price": 450},
    {"name": "Diners Inn", "price": 380},
    {"name": "Junkers", "price": 550},
]

# data for customers
customers_data = [
    {"first_name": "John", "last_name": "Doe"},
    {"first_name": "Jane", "last_name": "Smith"},
    {"first_name": "Michael", "last_name": "Johnson"},
    {"first_name": "Emily", "last_name": "Brown"},
    {"first_name": "David", "last_name": "Lee"},
]

# data for reviews
reviews_data = [
    {"content": "Great food and service!", "rating": 5, "restaurant_id": 1, "customer_id": 1},
    {"content": "Nice ambiance, but food could be better.", "rating": 3, "restaurant_id": 2, "customer_id": 2},
    {"content": "Excellent experience overall.", "rating": 4, "restaurant_id": 1, "customer_id": 3},
    {"content": "Not impressed with the menu.", "rating": 2, "restaurant_id": 3, "customer_id": 4},
    {"content": "Outstanding in every way!", "rating": 5, "restaurant_id": 4, "customer_id": 5},
]

# Populate the database with the data
for restaurant_data in restaurants_data:
    restaurant = Restaurant(**restaurant_data)
    session.add(restaurant)

for customer_data in customers_data:
    customer = Customer(**customer_data)
    session.add(customer)

for review_data in reviews_data:
    review = Review(**review_data)
    session.add(review)

# Commit the changes to the database
session.commit()

# Close the session
session.close()
