# 🏭 Sugar Factory Booking System

A web-based Sugar Factory Booking System built using **Python, Django, and MySQL**. The application allows users to register, manage their profiles, and book cane delivery slots through an interactive calendar.

## 🚀 Features

- **User Authentication:** User registration, login, and logout.
- **User Profile:** View and update farmer profile details.
- **Booking Calendar:** Interactive calendar for cane delivery bookings.
- **Slot Management:** Maximum 3 bookings per day.
- **Booking Dashboard:** View and manage personal bookings.
- **Booking Cancellation:** Cancel existing bookings.
- **Manufacturing Information:** Explore the six manufacturing stages.
- **Admin Panel:** Manage users, bookings, and website content.
- **AJAX Integration:** Book slots without reloading the page.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| MySQL | Database |
| HTML5 | Page structure |
| CSS3 | Styling |
| JavaScript | Frontend interactions |
| Bootstrap | Responsive UI |
| AJAX | Asynchronous requests |
| SweetAlert2 | Interactive alerts |

## 📁 Project Structure

```text
sugar_factory_django/
│
├── apps/
│   ├── core/
│   ├── accounts/
│   ├── booking/
│   └── manufacturing/
│
├── sugar_factory/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   ├── layouts/
│   ├── core/
│   ├── accounts/
│   ├── booking/
│   └── manufacturing/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/
├── database_setup.sql
├── manage.py
└── requirements.txt
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd sugar_factory_django
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create MySQL Database

Create the database using MySQL:

```sql
CREATE DATABASE sfbs
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Alternatively, run the provided SQL setup file:

```bash
mysql -u root -p < database_setup.sql
```

### 5. Configure Database

Update the `DATABASES` configuration in `sugar_factory/settings.py` with your MySQL credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sfbs',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

If migrations have not been created for your models, generate them first:

```bash
python manage.py makemigrations
```

### 7. Create Admin Account

```bash
python manage.py createsuperuser
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Open the application:

```text
http://127.0.0.1:8000/
```

## 📅 Booking Rules

- Maximum 3 bookings are allowed per day.
- A user can make only one booking per day.
- Past dates cannot be booked.
- Users can view and cancel their bookings from the dashboard.

## 🔗 Important URLs

| URL | Description |
|---|---|
| `/` | Home Page |
| `/about/` | About Us |
| `/contact/` | Contact |
| `/products/` | Products |
| `/manufacturing/` | Manufacturing Overview |
| `/accounts/register/` | User Registration |
| `/accounts/login/` | User Login |
| `/booking/calendar/` | Booking Calendar |
| `/booking/dashboard/` | User Dashboard |
| `/admin/` | Admin Panel |

## 🧪 Run Tests

```bash
python manage.py test
```

## 🔒 Security

- Django authentication system.
- Password hashing using Django's password management.
- CSRF protection.
- Django ORM for database operations.
- Form validation and session-based authentication.

## 👩‍💻 Author

**Kumkum Gadhwal**

GitHub: [Your GitHub Profile](YOUR_GITHUB_PROFILE_URL)

---

⭐ If you find this project useful, consider giving it a star!