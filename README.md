# Library Management System

A Flask-based Library Management System built with Python and Object-Oriented Programming (OOP).

## Features

* Member registration and login
* Member dashboard
* Browse available books
* Borrow and return books
* Admin login
* Add books
* Delete books
* JSON-based data persistence
* Flask sessions for authentication

## Technologies Used

* Python
* Flask
* Object-Oriented Programming (OOP)
* HTML
* CSS
* JavaScript
* JSON

## Project Structure

```text
lms/
├── app.py
├── admin.py
├── book.py
├── library.py
├── member.py
├── library_data.json
├── requirements.txt
├── .env
├── .gitignore
├── templates/
├── static/
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/SammyCruz19/lms.git
cd lms-oop
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

The application uses a Flask secret key for session management.

Create a `.env` file in the same directory as `app.py`:

```env
SECRET_KEY=your-own-secret-key
```

You can use your own random secret key. Do not share or commit your `.env` file.

The `.env` file is excluded from Git using `.gitignore`.

## Running the Application

Start the Flask development server:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Admin Login

The default admin credentials used by the application are:

```text
Username: admin
Password: 1234
```

After logging in as an administrator, you can add and delete books and view registered members.

> **Note:** These credentials are hard-coded for demonstration purposes. They should be replaced with a more secure authentication system in a production application.

## Data Storage

The application stores books and member information in:

```text
library_data.json
```

The JSON file is automatically loaded when the application starts and updated when changes are made.

## Disclaimer

This project is intended for learning and demonstration purposes. It is not designed for production use and does not implement production-level authentication, authorization, or database security.
