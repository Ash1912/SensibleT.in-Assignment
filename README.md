# SensibleT.in-Assignment

# Transaction Management API

This project provides a RESTful API for managing financial transactions. It allows users to create, update, and fetch transactions based on user ID. The project is built using Django and Django REST Framework.

## Requirements

- Python 3.x
- Django
- Django REST Framework

## Installation

### 1. Clone the Repository
   
```bash
git clone https://github.com/<your-username>/SensibleT.in-Assignment.git
```

### 2. Install Python and Django

Ensure Python is installed on your system. You can check if Python is installed by running:

```bash
python --version
```

To install Django and Django REST Framework, run the following command:

```bash
pip install django djangorestframework
```

### 3. Set Up the Project

Create a new Django project and an app for transactions:

```bash
django-admin startproject transaction_management
cd transaction_management
python manage.py startapp transactions
```

### 4. Install Required Libraries

```bash
pip install django djangorestframework
```

### 5. Configure the App

Add rest_framework and transactions to the INSTALLED_APPS list in transaction_management/settings.py:

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'transactions',  # Add this
]
```

### 6. Create the Transaction Model

Edit transactions/models.py to define the Transaction model.

### 7. Create the Serializer

Create a serializers.py file in the transactions app.

### 8. Create the Views

Edit transactions/views.py to create the viewset for Transaction.

### 9. Define URLs

Create transactions/urls.py

### 10. Migrate the Database

Run the following commands to apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 11. Test the API

Start the development server:

```bash
python manage.py runserver
```

This project will run on
```bash
http://127.0.0.1:8000
```
## Project Structure

```bash
transaction_management/
    ├── manage.py
    ├── transaction_management/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── transactions/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
```

Use a tool like Postman or CURL to test the endpoints.

### Example API Endpoints:

**1. Create a Transaction (POST /api/transactions/)**:

**Request**:

```json
{
    "amount": 100.00,
    "transaction_type": "DEPOSIT",
    "user": 1
}
```

**Response**:

```json
{
    "id": 1,
    "amount": "100.00",
    "transaction_type": "DEPOSIT",
    "status": "PENDING",
    "timestamp": "2024-11-16T10:30:00Z"
}
```

**2. Get All Transactions for a User (GET /api/transactions/?user_id=1)**:

**Response**:

```json
[
    {
        "id": 1,
        "amount": "100.00",
        "transaction_type": "DEPOSIT",
        "status": "PENDING",
        "timestamp": "2024-11-16T10:30:00Z"
    }
]
```

**3. Get All Transactions for a User (GET http://127.0.0.1:8000/api/transactions/by_user/?user_id=1)**: 

**Response **:

```json
{
    "transactions": [
        {
            "id": 1,
            "amount": "100.00",
            "transaction_type": "DEPOSIT",
            "status": "PENDING",
            "timestamp": "2024-11-16T10:30:00Z"
        }
    ]
}
```

**Update Transaction Status (PATCH /api/transactions/1/):

**Request**:

```json
{
    "status": "COMPLETED"
}
```

**Response**:

```json
{
    "id": 1,
    "amount": "100.00",
    "transaction_type": "DEPOSIT",
    "status": "COMPLETED",
    "timestamp": "2024-11-16T10:30:00Z"
}
```

### Additional Notes:

- **Transaction Types**: DEPOSIT, WITHDRAWAL

- **Transaction Statuses**: PENDING, COMPLETED, FAILED

- Ensure that you have a User model in your Django application as transactions are linked to users.

## License

### MIT License


### Key Points:
1. **Endpoints**:
   - **POST**: Create a transaction.
   - **GET**: Get transactions for a user.
   - **PATCH**: Update transaction status.
   
2. **Database**: The database stores transaction information, including the amount, type, user, status, and timestamp.
   
3. **Requirements**: Make sure to install the necessary dependencies and migrate the database.

