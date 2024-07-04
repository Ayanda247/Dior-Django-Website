# Dior Store Project

The project is a Django-powered website for a fictitious Dior store. Here's a summary of the current status of the project:

## Current Features

- **Home Page**: The website's landing page that displays prominent items and promotions.
- **Women's Section**: Dedicated to women's items, such as beauty products, purses, and shoes. The products and prices listed here are retrieved from the database.
- **Men's Section**: Features items such as cologne and shoes. Products and prices are retrieved from the database, similar to the women's section.
- **Cologne & Beauty Section**: A specialized area providing information on cologne and beauty goods sourced from the database.
- **Contact Page**: Includes a contact form that allows users to submit questions, which are stored in the database and followed by a confirmation email. This page also contains a FAQ section.
- **Search Functionality**: A search bar allows users to search for goods. The search results contain product names and photos, dynamically retrieved based on the user's input.
- **Django Debug Toolbar**: Provides precise performance measurements and SQL query analysis, making it easy to optimize and debug the application.
- **Media File Handling**: Allows users to upload and manage photos and other media formats. Media files are stored in a specific directory and served by the Django development server.

## Future Development

Currently, the project is in development, with the following anticipated improvements:

- **User Authentication**: Enabling login and registration features.
- **User Profiles**: Users may manage their profiles and examine order history.
- **Order Management**: Allow users to place orders and check their status.
- **Enhanced Search and Filter Options**: Improving search capabilities to deliver more accurate results and more filters.
- **Responsive Design**: Ensure that the website is completely responsive and appears fantastic on all devices.

## Requirements

- Python 3.10.x
- Django 4.0.3
- Django REST Framework 3.13.1
- Pillow 9.0.1
- django-crispy-forms 1.13.0
- django-debug-toolbar 3.2.4
- django-allauth 0.50.0
- whitenoise 5.3.0
- django-cors-headers 3.10.1
- gunicorn 20.1.0
- psycopg2-binary 2.9.3
- mysqlclient 2.1.0
- django-environ 0.8.1
- django-oscar 2.2
- django-payments 0.14.0
- django-mptt 0.13.4
- django-taggit 1.5.1
- django-model-utils 4.2.0
- django-redis 5.2.0
- django-storages 1.13.2
- boto3 1.26.7
- stripe 2.62.0
- django-secure 1.0.1
- django-axes 5.27.1
- django-compressor 4.3
- pytest 7.2.0
- pytest-django 4.5.2
- factory-boy 3.2.1
- sphinx 5.3.0
- sphinx-rtd-theme 1.0.0
- # django-media 1.0.1 (commented out for now)

## Installation and Setup

### Using `venv`

1. **Clone the Repository**:
  ```
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
```
   

2. **Create and Activate a Virtual Environment**:
```
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`t
```

3. **Install Dependencies**:
```
  pip install -r requirements.txt
```

4. **Set Up Environment Variables**:
  Create a .env file in the project root and add your environment variables (e.g., database configuration, secret key).

5. **Apply Migrations**:
```
  python manage.py migrate
```

6. **Create a Superuser**:
```
  python manage.py createsuperuser
```

7. **Run the Development Server**:
```
  python manage.py runserver
```


### Using Docker:

1. **Clone the Repository**:
```
  git clone https://github.com/yourusername/yourproject.git
  cd yourproject
```

2.**Create a Dockerfile in the project root**:
```
  FROM python:3.10-slim

  WORKDIR /app

  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt

  COPY . .

  ENV PYTHONUNBUFFERED=1

  CMD ["gunicorn", "--bind", "0.0.0.0:8000", "yourproject.wsgi:application"]
```

3. **Create a docker-compose.yml file in the project root**:
```
  version: '3'

  services:
    web:
      build: .
      command: gunicorn yourproject.wsgi:application --bind 0.0.0.0:8000
      volumes:
        - .:/app
      ports:
        - "8000:8000"
      env_file:
        - .env
      depends_on:
        - db

    db:
      image: postgres:13
      volumes:
        - postgres_data:/var/lib/postgresql/data
      environment:
        POSTGRES_DB: yourdbname
        POSTGRES_USER: yourdbuser
        POSTGRES_PASSWORD: yourdbpassword

  volumes:
    postgres_data:
```

4. **Set Up Environment Variables**:
   Create a .env file in the project root and add your environment variables:
```
  SECRET_KEY=your-secret-key
  DEBUG=True
  DB_NAME=yourdbname
  DB_USER=yourdbuser
  DB_PASSWORD=yourdbpassword
  DB_HOST=db
  DB_PORT=5432
```

5. **Build and Run the Docker Containers**:
```
  docker-compose up --build
```

6. **Apply Migrations**:
   Open a new terminal and run:
```
  docker-compose exec web python manage.py migrate
```

7. **Create a Superuser**:
```
  docker-compose exec web python manage.py createsuperuser
```

Your application should now be up and running. You can access it at
        ```http://localhost:8000```
  
   





   

