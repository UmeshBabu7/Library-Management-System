# Library Management System

This project is a microservices-based library management system built using Python Django. It includes services for managing books, members, borrowing, notifications, and search functionality. The system is designed to be scalable and user-friendly for both librarians and members.

 Features

 Librarian Dashboard
- Overview Section: Displays total books, total members, books borrowed, and overdue books.
- Book Management: Add, remove, update, and search for books.
- Member Management: Add, remove, update, and search for members.
- Borrowing Management: Issue and return books, track borrowing history.
- Notifications: Manage overdue notifications and reservation alerts.
- Reports and Analytics: View borrowing trends, popular books, and member activity.

 Member Dashboard
- Personal Overview: View borrowed books, borrowing history, and overdue books.
- Book Search and Reservation: Search for books and reserve unavailable ones.
- Notifications: Receive due date reminders, overdue alerts, and reservation updates.
- Profile Management: Update personal information and view membership status.
- Recommendations: Get personalized book recommendations and see new arrivals.

 Microservices

# Book Service
Manages book information (CRUD operations).

# Member Service
Manages member information (CRUD operations).

# Borrowing Service
Manages borrowing and returning of books.

# Notification Service
Handles notifications for overdue books using Celery for periodic tasks.

# Search Service
Provides search functionality for books and members.

 Setup Instructions

 Prerequisites
- Python 
- Django
- Django REST Framework
- Celery
- Redis (for Celery)
- Docker (for containerization)

# Installation

1. Clone the repository:
    ```
    git clone https://github.com/UmeshBabu7/Library-Management-System.git
    cd Library-Management-System
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Start Redis server:
    ```
    redis-server
    ```

5. Start Celery worker and beat:
    ```
    celery -A your_project_name worker --loglevel=info
    celery -A your_project_name beat --loglevel=info
    ```

6. Run the Django development server:
    ```
    python manage.py runserver
    ```

# Docker Setup

1. Build and run each service:
    ```
    docker build -t book_service -f Dockerfile.book_service .
    docker run -d -p 8000:8000 book_service

    docker build -t member_service -f Dockerfile.member_service .
    docker run -d -p 8001:8001 member_service

    docker build -t borrowing_service -f Dockerfile.borrowing_service .
    docker run -d -p 8002:8002 borrowing_service

    docker build -t notification_service -f Dockerfile.notification_service .
    docker run -d -p 8003:8003 notification_service

    docker build -t search_service -f Dockerfile.search_service .
    docker run -d -p 8004:8004 search_service
    ```

# Usage

 Librarian Dashboard
Access the librarian dashboard at `http://localhost:8000/dashboard/` to manage books, members, borrowing, and view reports.

 Member Dashboard
Members can access their dashboard at `http://localhost:8001/dashboard/` to view borrowed books, search for books, and manage their profile.
