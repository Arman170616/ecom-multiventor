#!/bin/bash

# Multi Vendor E commerce API

# A brief and descriptive title for your project.

## Setup

### 1. Virtual Environment

# Create a virtual environment to isolate your project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

```
### 2. Install the required dependencies.
```
    pip install -r requirements.txt

```

###3. Database Migration
Apply migrations to set up the database.
```
python manage.py migrate
```
API Endpoints 
```
     {
        "users": "http://127.0.0.1:8000/users/",
        "products": "http://127.0.0.1:8000/products/",
        "cartitems": "http://127.0.0.1:8000/cartitems/",
        "carts": "http://127.0.0.1:8000/carts/",
        "orders": "http://127.0.0.1:8000/orders/",
        "dailydata": "http://127.0.0.1:8000/dailydata/"
    }

```
 
