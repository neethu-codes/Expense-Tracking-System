# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.
This is a simple **Expense Management System** that allows users to record, categorize, and analyze their expenses. It is built with:

- **Frontend:** [Streamlit](https://streamlit.io/) for an interactive and user-friendly UI.
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) for handling API requests and managing data.
- **Database:** MySQL for storing expense records.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
1. **Create and activate virtual environment:**:   
   ```bash
    python -m venv venv  # Create virtual environment
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate  # For Windows
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```

## API Endpoints (FastAPI)

| Method | Endpoint         | Description                              | Request Body Parameters                                                                                    |
| :----- | :--------------- | :--------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| **GET**  | `/expenses/{date}` | Retrieve all expenses on a specific date | *None*                                                                                                 |
| **POST** | `/expenses/{date}` | Add a new expense on a specific date    | An array of objects, each with: `category`: String, `amount`: Float, `notes`: String                  |
| **POST** | `/analytics`      | Fetch expenses between two dates         | `start_date`: Date (YYYY-MM-DD), `end_date`: Date (YYYY-MM-DD)                                          |
| **GET**  | `/analytics`      | Get all the expenses grouped by month   | *None*                                                                                                 |

**Note:** For POST requests, the request body should be sent as a JSON object.
