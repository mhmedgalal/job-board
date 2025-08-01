# Job Board - Django Project

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.1.7-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> A comprehensive job board website built with Django that allows users to post jobs, apply for positions, and manage their profiles.

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/7ee92732-b255-48c6-a730-f089334934a3" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/b373e154-52d4-4d6b-8268-ab64b466b56e" />



---

## 🚀 Features

- ✅ **User Authentication**: Register, login, and manage user profiles
- ✅ **Job Posting**: Employers can post and manage job offers
- ✅ **Job Search**: Filter and browse available jobs
- ✅ **Job Applications**: Users can upload CVs and apply directly
- ✅ **Blog System**: Admins can post articles and news
- ✅ **Contact Page**: With working email form
- ✅ **Responsive Design**: Fully responsive across all devices

---

## 🛠️ Technologies Used

- **Backend**: Django 5.1.7
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite (development)
- **Others**: django-bootstrap5, django-filter, Pillow

---

## 📦 Requirements

Ensure you have Python 3.12+ installed.

Django==5.1.7
django-bootstrap5
django-filter
Pillow

yaml
Copy
Edit

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mhmedgalal/job-board.git
   cd jobs
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On macOS/Linux: source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations

bash
Copy
Edit
python manage.py migrate
Create a superuser (optional)

bash
Copy
Edit
python manage.py createsuperuser
Run the development server

bash
Copy
Edit
python manage.py runserver
Open the site
Visit http://127.0.0.1:8000 in your browser.

🗂️ Project Structure
bash
Copy
Edit
jobs/
├── accounts/       # Authentication & profiles
├── Blog/           # Blog system
├── contact/        # Contact form
├── home/           # Homepage views
├── job/            # Job models and views
├── pages/          # Static pages
├── project/        # Main settings & URLs
├── static/         # Static assets
├── templates/      # HTML templates
├── media/          # Uploaded files
└── manage.py       # Django CLI
👤 Usage
Job Seekers
Register/login

Browse jobs

Apply with CV

Manage profile

Employers
Register/login

Post jobs

View applications

Edit or delete job listings

🤝 Contributing
Fork the repo

Create a new branch

Commit your changes

Push and open a pull request

📝 License
This project is licensed under the MIT License.

👨‍💻 Author
Mohmed Galal
GitHub


Mohmed Galal 
