# Job Board - Django Project

A comprehensive job board website built with Django that allows users to post jobs, apply for positions, and manage their profiles.

## Features

- **User Authentication**: Register, login, and profile management
- **Job Posting**: Employers can post new job opportunities
- **Job Search**: Browse and filter available jobs
- **Job Applications**: Users can apply for jobs with CV upload
- **Blog System**: News and articles section
- **Contact Form**: Contact page with email functionality
- **Responsive Design**: Modern UI that works on all devices

## Technologies Used

- **Backend**: Django 5.1.7
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (development)
- **Additional**: django-bootstrap5, django-filter, Pillow

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd jobs
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the website**
   Open your browser and go to `http://127.0.0.1:8000`

## Project Structure

```
jobs/
├── accounts/          # User authentication and profiles
├── Blog/             # Blog system
├── contact/          # Contact form
├── home/             # Home page
├── job/              # Job posting and management
├── pages/            # Additional pages
├── project/          # Django project settings
├── static/           # Static files (CSS, JS, images)
├── templates/        # Base templates
├── media/            # User uploaded files
└── manage.py         # Django management script
```

## Usage

### For Job Seekers
1. Register an account
2. Browse available jobs
3. Apply for positions by uploading your CV
4. Manage your profile and applications

### For Employers
1. Register an account
2. Post new job opportunities
3. Review applications
4. Manage your job postings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Author

Mohmed Galal 