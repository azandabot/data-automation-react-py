# Time-Series Data Visualization Web Application

## Overview

This project is a simple web application designed to visualize time-series data from various sensors in a factory setting. The application comprises a React frontend, a Flask backend, and a PostgreSQL database. The purpose of this application is to allow users to view numeric and text parameter data from different devices over time.

## Tech Stack

- **Frontend**: React.js, Bootstrap 5.3, TanStack React Query, Vite
- **Backend**: Flask, Marshmallow, SQLAlchemy, Pipenv
- **Database**: PostgreSQL

## Setup Instructions

Follow these instructions to set up the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- Node.js (v14 or later)
- Python (v3.8 or later)
- PostgreSQL (v12 or later)
- Pipenv

### Backend Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/azandabot/data-automation-react-py.git
    cd data-automation-react-py/backend
    ```

2. **Set up a virtual environment and install dependencies**:
    ```sh
    pipenv install
    pipenv shell
    ```

3. **Set up environment variables**:
    - Create a `.env` file in the `backend` directory:
      ```sh
      touch .env
      ```
    - Add the following variables to the `.env` file:
      ```ini
      DATABASE_HOST=localhost
      DATABASE_PORT=5432
      DATABASE_USER=username
      DATABASE_PASSWORD=password
      DATABASE_NAME=timeseries_db
      SECRET_KEY=your_secret_key
      ```

4. **Configure Flask to use environment variables**:
    In `app.py`, load the variables from the `.env` file:
    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()

    DATABASE_URL = f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
    SECRET_KEY = os.getenv('SECRET_KEY')
    ```

5. **Database Setup**:
    - The database will be created and migrations will be applied when the app is run.

6. **Run database migrations and seed data**:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    flask seed run
    ```

7. **Start the backend server**:
    ```sh
    flask run
    ```

### Frontend Setup

1. **Navigate to the frontend directory**:
    ```sh
    cd ../frontend
    ```

2. **Set up environment variables**:
    - Create a `.env` file in the `frontend` directory:
      ```sh
      touch .env
      ```
    - Add the following variables to the `.env` file:
      ```ini
      VITE_API_URL=http://localhost:5000
      VITE_API_SECRET=your_api_secret
      ```

3. **Install dependencies**:
    ```sh
    npm install
    ```

4. **Start the frontend development server**:
    ```sh
    npm run dev
    ```

### Running the Application

1. Ensure both the backend and frontend servers are running.
2. Open your browser and navigate to `http://localhost:3000`.

## Project Structure

time-series-visualization/
├── backend/
│ ├── db/
│ │ ├── init.py
│ │ ├── db.py
│ ├── models/
│ │ ├── init.py
│ ├── controllers/
│ │ ├── init.py
│ ├── utils/
│ │ ├── init.py
│ ├── routes/
│ │ ├── init.py
│ ├── app.py
│ ├── config.py
│ ├── migrations/
│ ├── Pipfile
│ ├── Pipfile.lock
│ └── .env
└── frontend/
├── public/
├── src/
│ ├── components/
│ ├── main.js
├── index.html
├── package.json
├── package-lock.json
└── .env


## Explanation and Decisions

This application was developed to provide a simple yet effective interface for visualizing time-series data. Flask was chosen for the backend due to its simplicity and flexibility, while React.js was chosen for the frontend for its powerful component-based architecture. The application uses Bootstrap 5.3 for styling and TanStack React Query for performing CRUD operations.

**Backend**:
- **Flask** serves the API endpoints.
- **SQLAlchemy** manages database interactions.
- **Marshmallow** handles serialization/deserialization.
- **Pipenv** simplifies dependency management.
- **dotenv** is used for environment variables.
- **Auth**: A simple token-based authentication is implemented, where each user gets a token upon accessing the API.
- **Database Migrations and Seeding**: SQLAlchemy is used to manage database migrations and seeding.

**Frontend**:
- **React** allows for dynamic, responsive UI components.
- **Bootstrap 5.3** provides a modern CSS framework for styling.
- **TanStack React Query** simplifies data fetching and state management.
- **Vite** is used for fast and efficient development server setup.

Given more time, additional features such as more sophisticated error handling, enhanced data visualization, and comprehensive testing could be implemented.

## Authentication

A simple token-based authentication mechanism is implemented. Each user receives a token from the backend, which must be included in subsequent API requests for authentication.

### Generating a Token

1. **API Endpoint**: `/api/token`
2. **Method**: `POST`
3. **Response**: `{ "token": "your_generated_token" }`

### Using the Token

Include the token in the `Authorization` header of your API requests:

```sh
Authorization: Bearer your_generated_token
