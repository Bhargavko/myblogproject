# Django Blog Project

This is a simple blog application built using Django and the Django REST Framework. The application allows users to create, read, update, and delete blog posts.

## Features

- User authentication using token-based authentication
- Create, read, update, and delete blog posts
- A simple REST API for accessing blog posts

## Technologies Used

- Django 5.1.2
- Django REST Framework
- SQLite (for the database)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/myblogproject.git
   cd myblogproject
2. Create and activate a virtual environment:
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install the required packages:
   pip install -r requirements.txt

4. Running the Application
   Apply database migrations:

    python manage.py migrate
    Create a superuser to access the admin interface:


    python manage.py createsuperuser
    Run the development server:


    python manage.py runserver
    Open your browser and navigate to http://127.0.0.1:8000/.

    API Endpoints
    GET /api/posts/ - List all blog posts
    POST /api/posts/ - Create a new blog post (requires authentication)
    GET /api/posts/<id>/ - Retrieve a specific blog post
    PUT /api/posts/<id>/ - Update a specific blog post (requires authentication)
    DELETE /api/posts/<id>/ - Delete a specific blog post (requires authentication)

   Generate the Token: You can generate a token using the Django shell:

5. python manage.py shell
   
   Run the following commands in the shell:
   from django.contrib.auth.models import User
   from rest_framework.authtoken.models import Token

   # Replace 'username' with the actual username
   user = User.objects.get(username='your_username')  
   token, created = Token.objects.get_or_create(user=user)
   print(token.key)  # This will display the token
   Use the Token: Use the token in your API requests by including it in the header:


   curl -H "Authorization: Token your_token_here" http://127.0.0.1:8000/api/posts/

6. Authentication
    This application uses token-based authentication. To obtain a token, you can register a new user or use the       existing users through the Django admin interface. Include the token in your request headers as follows:


    Authorization: Token <your_token>
    Curl Commands for API Interaction
    List all blog posts

    curl -H "Authorization: Token <your_token>" http://127.0.0.1:8000/api/posts/
    Create a new blog post

    curl -X POST -H "Authorization: Token <your_token>" -H "Content-Type: application/json" -d '{"title": "My New       Blog Post", "content": "This is the content of my new blog post."}' http://127.0.0.1:8000/api/posts/
    Update a blog post

    curl -X PUT -H "Authorization: Token <your_token>" -H "Content-Type: application/json" -d '{"title": "My Updated Blog Post", "content": "This is the updated content of my new blog post."}' http://127.0.0.1:8000/api/posts/<id>/
    Delete a blog post
    
    curl -X DELETE -H "Authorization: Token <your_token>" http://127.0.0.1:8000/api/posts/<id>/


