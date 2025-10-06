# Expense Management System

The Expense Tracking System is a web-based application built using Streamlit, Python, and MySQL that allows users to easily record and analyze their daily expenses.
It provides an intuitive interface to add new expenses, view existing records, and analyze historical spending patterns through a clear visual dashboard.

### 🚀 **Features**

💰 **Add and View Expenses**:
Record daily expenses with details like date, amount, category, and notes.

📅 **Date-based Filtering**:
Select specific date ranges to review your past expenses.

📊 **Visual Insights**:
View category-wise expense breakdown using interactive bar charts for selected dates.

⚠️ **Validation and Notifications**:
Displays alerts when data is unavailable for a selected date range.

🗃️ **Database Integration**:
Stores all expense records securely in a MySQL database.
## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Dikshawelekar8/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py