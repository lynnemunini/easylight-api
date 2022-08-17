# EasyLight API

Flask application that serves as an API for the [EasyLight](https://github.com/lynnemunini/EasyLight) app.

The API fetches details from the Android app during registration and updates the database.
When the user wants to login to the app, the API fetches the user's details from the database and checks if they match the details provided by the user.
If successful, the user will be redirected to the app.

The API is hosted on Heroku and can be accessed from any device connected to the internet.

## Admin Dashboard

The admin dashboard is a web application that allows the admin to manage the app. To access the admin dashboard for the app use the following link [Admin Dashboard](http://easylight.herokuapp.com/admin)

## Installation

Clone the repository and install dependencies:

```bash
git clone 
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the application

Run the application:

```bash
python3 main.py
```
