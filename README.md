# Data Visio

[![Data Visio](https://res.cloudinary.com/marcomontalbano/image/upload/v1716861937/video_to_markdown/images/google-drive--1AY5NL0kRRAJQJfpJpu0wH9DfjBOIQ5qu-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1AY5NL0kRRAJQJfpJpu0wH9DfjBOIQ5qu/preview "Data Visio")


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
pipenv install
pipenv shell
```
3. Set up environment variables:
Create a `.env` file in the `backend` directory with the following content:
```plaintext
DB_NAME=timeseries_db
DB_USER=postgres
```
5. Create the database:
Make sure your database is set up and running. Update the credentials in the `.env` file accordingly.

6. Run application:
```bash
python app.py
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
│   ├── tests
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

![Screenshot 2024-05-28 033328](https://github.com/azandabot/data-automation-react-py/assets/147757437/9fa312b8-aef6-4df6-a171-dff5be86900f)
![Screenshot 2024-05-28 033305](https://github.com/azandabot/data-automation-react-py/assets/147757437/a3001250-37ce-4242-8e8d-3befc8339a8f)
![Screenshot 2024-05-28 033140](https://github.com/azandabot/data-automation-react-py/assets/147757437/147f2efb-d44e-4d3e-8867-2e04d963e915)
![Screenshot 2024-05-28 033058](https://github.com/azandabot/data-automation-react-py/assets/147757437/a62aac09-ffd3-4bf1-92e5-fbc5379e20c7)
![Screenshot 2024-05-28 033036](https://github.com/azandabot/data-automation-react-py/assets/147757437/65a601e2-eb88-4b22-912f-314eadac01db)
![Screenshot 2024-05-28 033012](https://github.com/azandabot/data-automation-react-py/assets/147757437/eaa5f350-c233-456c-ba2b-fc03c03fe141)
![Screenshot 2024-05-28 032933](https://github.com/azandabot/data-automation-react-py/assets/147757437/46c01299-55a3-4c34-a655-36999f77e091)
![Screenshot 2024-05-28 032919](https://github.com/azandabot/data-automation-react-py/assets/147757437/11008569-de53-4ed9-9661-5db92bcfde0c)
![Screenshot 2024-05-28 032901](https://github.com/azandabot/data-automation-react-py/assets/147757437/40190cd9-32aa-47ed-9754-51526f8fd4c9)
![Screenshot 2024-05-28 033602](https://github.com/azandabot/data-automation-react-py/assets/147757437/63aef653-5141-4162-9a0b-f75e8a9accaa)
![Screenshot 2024-05-28 033522](https://github.com/azandabot/data-automation-react-py/assets/147757437/428e7b20-319c-40df-b574-abd8e7dabcde)
![Screenshot 2024-05-28 033425](https://github.com/azandabot/data-automation-react-py/assets/147757437/bdb12735-1a4c-474b-9298-7bc6190c43bf)
![Screenshot 2024-05-28 033404](https://github.com/azandabot/data-automation-react-py/assets/147757437/d1946891-517d-46d6-b545-87ef75bd5ada)
