# Restaurant Management System

This is a simple Restaurant Management System project that demonstrates the use of SQLAlchemy in a Python application. It includes models for restaurants, customers, and reviews, along with various methods to interact with the database.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10 (or a compatible version)
- Pipenv (for managing project dependencies)
- SQLite (or any other relational database you prefer)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>

2. Navigate to the project directory:

   cd restaurant-management-system

3. Install project dependencies using Pipenv:

   pipenv install

The project dependencies are defined in the Pipfile.

4. Create the database tables and populate them     
   with mock data by running the following command:

   pipenv run python3 seed.py


## Database Migrations

This project uses Alembic for database migrations. The configuration for Alembic is stored in the alembic.ini file. To create and manage database migrations, you can use the following Alembic commands:

1. Initialize Alembic (run this once to set up     
   migrations):

   pipenv run alembic init alembic

2. Generate a new migration script after making 
   changes to your models:

   pipenv run alembic revision -m "Your migration message"

3. Apply migrations to the database:

   pipenv run alembic upgrade head

4. Rollback the last migration (useful for testing):

   pipenv run alembic downgrade -1


## Author
   
   John Jackson Winter.


## Lisence
   
   This project is licensed under the MIT License - see the LICENSE file for details.







