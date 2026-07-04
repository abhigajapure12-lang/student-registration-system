# Student Registration Form

A Django-based student registration system with a modern UI. This project allows you to register students, view registered students, and manage student data through Django admin.

## Project Structure

```
myproject/
├── manage.py
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── register.html       # Registration form page
│   │   ├── success.html        # Success confirmation page
│   │   └── student_list.html   # View all registered students
│   ├── admin.py                # Django admin configuration
│   ├── forms.py                # Registration form definition
│   ├── models.py               # Database models (Student, Department, Course)
│   ├── urls.py                 # App URL routes
│   ├── views.py                # View functions (register, success, student_list)
│   └── ...
├── myproject/
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main project URL configuration
│   └── ...
└── manage.py
```

## Features

- **Student Registration Form**: Register new students with their personal and academic information
- **Form Validation**: Automatically validates email, phone number, and other fields
- **Student List View**: View all registered students in a beautiful table format
- **Admin Panel**: Manage students, departments, and courses through Django admin
- **Responsive Design**: Modern UI with Bootstrap 5
- **Success Notifications**: User-friendly success messages and confirmations

## Installation & Setup

### 1. Navigate to project directory
```bash
cd myproject
```

### 2. Install required packages (if not already installed)
```bash
pip install django psycopg2-binary
```

### 3. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser (for admin panel)
```bash
python manage.py createsuperuser
```

### 5. Add sample data (Departments and Courses)
```bash
python manage.py shell
```

Then in the Django shell, run:
```python
from myapp.models import Department, Course

# Create departments
dept1 = Department.objects.create(department_name='Computer Science')
dept2 = Department.objects.create(department_name='Information Technology')

# Create courses
course1 = Course.objects.create(course_name='B.Tech in CSE', duration='4 years')
course2 = Course.objects.create(course_name='B.Tech in IT', duration='4 years')

exit()
```

### 6. Run the development server
```bash
python manage.py runserver
```

## URLs

- **Registration Page**: `http://localhost:8000/` - Register a new student
- **Success Page**: `http://localhost:8000/success/` - Confirmation after registration
- **Student List**: `http://localhost:8000/students/` - View all registered students
- **Admin Panel**: `http://localhost:8000/admin/` - Manage all data

## Database Models

### Student
- First Name
- Last Name
- Age
- Email
- Phone
- Department (Foreign Key)
- Course (Foreign Key)

### Department
- Department Name

### Course
- Course Name
- Duration

## Form Fields

The registration form includes:
- First Name (Text input)
- Last Name (Text input)
- Age (Number input)
- Email (Email input with validation)
- Phone (Text input, max 10 characters)
- Department (Dropdown selection)
- Course (Dropdown selection)

## Styling

The project uses:
- **Bootstrap 5** for responsive layout
- **Custom CSS** for gradient backgrounds and modern UI components
- **Form Bootstrap Classes** for consistent styling

## Admin Panel Features

- Search students by name, email, or phone
- Filter students by department, course, or age
- Sort by any column
- Add, edit, or delete student records
- Bulk operations support

## Next Steps

You can extend this project by:
1. Adding user authentication for students
2. Implementing email notifications for registration
3. Adding payment gateway integration
4. Creating student login portal
5. Adding download/export functionality for student records
6. Implementing file uploads for student documents
7. Adding search and advanced filtering
