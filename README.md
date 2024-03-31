# Quizify Web Application

Quizify is a web application designed to empower interactive learning and engagement through quizzes. It allows users to register, log in, create quizzes, and take quizzes created by other users.

## Table of Contents
* `Installation`
* `Usage`
* `Features`
* `File Structure`
* `Technologies Used`
* `Contributing`
* `License`

## Installation
To run Quizify locally on your machine, follow these steps:

1. Clone the repository
```bash
git clone <repository_url >
```

2. Navigate to the project directory
```bash
cd Quizify
```

3. Create a virtual environment:
```bash
python3 -m venv venv
```

4. Activate the virtual environment:
>> On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```

>> On Windows:
  ```bash
  venv\Scripts\activate
  ```

5. Install the required dependencies:
```bash
pip install -r requirements.txt
```

6. Set up the environment variables:
* Create a .env file in the project root directory.
*  Add the following environment variables to the .env file:

    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url

7. Set up database using sql queries using the .sql file which contains the db with required privileges:
```bash
cat set_db_dev.sql | sudo mysql -hlocalhost -uroot -p
```

## Usage
To run the Quizify web application, follow these steps:
1. Ensure your virtual environment is activated and navigate to Quizify directory.
2. Run the Flask application:
```bash
python3 api/app.py
```
3. Access the web application in your browser at `http://localhost:5000/home`

## Features
- User Registration: Users can create a new account by providing their email and password.
- User Authentication: Registered users can log in to their accounts securely.
- Dashboard: Users are presented with a dashboard where they can view available quizzes.
- Quiz Creation: Users can create quizzes by providing quiz titles, questions, and options.
- nQuiz Taking: Users can take quizzes created by other users and receive scores upon completion.
- API Integration: The application can fetch quiz data from an external API and create quizzes based on the fetched data.

## File Structure
```bash
Quizify/
│──api/
    ├── __init__.py             #Initializes flask as package
    ├── app.py                  # Main Flask application file
    ├── models.py               # Defines database models
    ├── templates/              # HTML templates
    │   ├── index.html          # Home page template
    │   ├── login.html          # Login page template
    │   ├── register.html       # User registration page template
    │   ├── dashboard.html      # Dashboard template
    │   ├── quiz.html           # Quiz page template
    ├── static/                 # Static files (CSS, JS, images, fonts)
    │   ├── css/                # CSS files
    │   ├── js/                 # JavaScript files
    │   ├── images/             # Image files
    │   ├── fonts/              # Font files
    │   └── forms/              # Form templates
    ├── .env                    # Environment variables configuration file
    ├── README.md               # Project README file
    ├── AUTHORS                 # Authors file
    ├── requirements.txt        # Python dependencies
    └── set_db_dev.sql          # SQL queries that sets the quizify database
  ```

## Technologies Used
- Flask: Micro web framework for Python
- Flask-SQLAlchemy: SQLAlchemy extension for Flask
- Flask-Login: User session management for Flask
- Flask-Migrate: Database migration tool for Flask
- Flask-Bcrypt: Flask extension for password hashing
- Python 3: Programming language
- HTML5/CSS3: Frontend markup and styling
- JavaScript: Frontend scripting language

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request on the GitHub repository. Thanks you!