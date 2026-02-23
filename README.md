# Job Board – Django Web App

Simple job board web application built with Django where users can browse jobs and view job details.  
You can use it as a learning project for Django basics (models, views, templates, URLs).

## Features

- List all job posts with title, company, and location.
- View detailed page for each job (description, created date, etc.).
- Django admin panel to manage jobs.
- Responsive basic UI using Django templates (HTML & CSS).

## Tech Stack

- Python 3.x
- Django 5.0 (or your version)
- SQLite (development database)
- HTML, CSS (Django Templates)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mhmedgalal/job-board.git
cd job-board
2. Create virtual environment
bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Apply migrations
bash
python manage.py migrate
5. Create superuser
bash
python manage.py createsuperuser
6. Run development server
bash
python manage.py runserver
Then open in your browser:

Site: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

Project Structure
text
job-board/
├── jobboard/          # Project settings & URLs
├── jobs/              # Job app (models, views, urls, templates)
├── templates/         # HTML templates
├── static/            # Static files (CSS, images) if any
├── manage.py
└── README.md
How it works
Job model contains main fields: title, description, company, location, created_at.

Views to display job list and detail page for each job.

Django admin to add, edit, and delete jobs easily.

Future Improvements
Add user accounts and job applications.

Add forms to create/edit jobs from the site, not only admin.

Add filtering/search for jobs (by title, company, location).

Add pagination for job list.

License
This project is for learning purposes.
Feel free to fork and modify it for your own use.

text
undefined
