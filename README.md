# Time-Series Data Visualization Web Application

## Overview
This project is a simple web application designed to visualize time-series data from various sensors in a factory setting. The application comprises a React frontend, a Flask backend, and a PostgreSQL database. The purpose of this application is to allow users to view numeric and text parameter data from different devices over time.

🛠 **Tech Stack**
-------------
- Frontend: React
- Backend: Flask
- Database: Your choice (PostgreSQL recommended)
- Styling: Bootstrap, Styled-Components
- Charting Libraries: @ant-design/plots, react-chartjs-2

🚀 **Getting Started**
------------------
### Prerequisites
Before you begin, ensure you have the following software installed:
- Node.js (>= 14.x)
- npm (>= 6.x) or yarn (>= 1.x)
- Python (>= 3.12)
- PostgreSQL (or any other database of your choice)

### Setup Instructions
#### 1. Clone the Repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/azandabot/data-automation-react-py.git
cd data-automation-react-py
```
#### 2. Set Up the Backend
1. Navigate to the `backend` directory:
```bash
cd backend
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Set up environment variables:
Create a `.env` file in the `backend` directory with the following content:
```plaintext
FLASK_APP=app.py
DATABASE_URL=your-database-url
```
5. Create the database:
Make sure your database is set up and running. Update the `DATABASE_URL` in the `.env` file accordingly.
6. Run database migrations:
```bash
flask db upgrade
```
7. Start the backend server:
```bash
flask run
```
#### 3. Set Up the Frontend
1. Navigate to the `frontend` directory:
```bash
cd frontend
```
2. Install the required dependencies:
```bash
npm install  # or yarn install
```
3. Start the frontend development server:
```bash
npm start  # or yarn dev
```

📊 **Application Overview**
-----------------------
This application captures time-series data from several sensors and visualizes it. The backend is built with Flask and serves a REST API, while the frontend is built with React and provides a user-friendly interface to view the data.

### Features
- View sensor data in real-time
- Visualize numeric and text data with charts and tables
- Simple and intuitive UI

### Project Structure
```plaintext
data-automation-react-py/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── .env
│   ├── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── ...
│   ├── public/
│   ├── ...
│
├── README.md
├── ...
```

📸 **Screenshots / Recordings**
---------------------------
Feel free to add screenshots or recordings of your project in the `screenshots` directory. Here are a few examples:
