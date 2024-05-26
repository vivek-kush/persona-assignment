
# Persona Assignment

A brief description of what this project does and who it's for

# Newsletter App

This repository contains a Newsletter Scheduler web application that allows you to create, schedule, and send newsletters via a RESTful API. The application ensures reliable and automated delivery of newsletters at specified times.

## Setup Instructions

1. **Clone the Repository:**

```bash
git clone https://github.com/vivek-kush/persona-assignment.git
cd persona_assignment/newsletter_service

```
2. **Create Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  
```

3. **Install Dependencies:**


```bash
pip install -r requirements.txt
```

4. **Create .env File:**

Create a file named .env in the project root directory and add the following content:
```bash
touch .env

EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password

```


5. **Run Database Migrations:**

```bash
python manage.py migrate
```

6. **Start Celery Worker:**

```bash
celery -A newsletter_service worker --loglevel=info
```
7. **Start Django Development Server:**

```bash
python manage.py runserver
```

## Test with cURL

1. **Add Topics:**
Sample request
```bash
curl --location 'http://127.0.0.1:8000/api/topics/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Sports"
}'
```
Sample response:
```bash
{
    "id": 1,
    "name": "Sports"
}
```

2. **Add Subscribers:**
Sample request
```bash
curl --location 'http://127.0.0.1:8000/api/subscribers/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "vivek.test1@gmail.com",
    "topics": [3, 2]
}'
```
Sample response:
```bash
{
    "id": 1,
    "email": "vivek.test1@gmail.com",
    "topics": [
        2,
        3
    ]
}
```

3. **Add Content:**

*Note: The send_time parameter must be in UTC time.*

Sample request
```bash
curl --location 'http://127.0.0.1:8000/api/contents/' \
--header 'Content-Type: application/json' \
--data '{
  "topic": 1,
  "text": "This is a test newsletter for xyz topic",
  "send_time": "2024-05-26T09:16:25Z"
}'
```
Sample response:
```bash
{
    "id": 1,
    "topic": 1,
    "text": "This is a test newsletter for xyz topic",
    "send_time": "2024-05-26T09:16:25Z"
}
```

