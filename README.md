# REST-API-to-manage-employees-in-a-company_CRUD-operations
# REST API to Manage Employees in a Company (CRUD Operations)

This project is a RESTful API designed to manage employee records in a company. It provides full CRUD (Create, Read, Update, Delete) functionality, allowing users to efficiently handle employee data.

## Features

- **Add a New Employee:** Create a new employee record with details such as name, designation, department, and salary.
- **View Employees:** Retrieve employee data by ID or view all employees in the company.
- **Update Employee Data:** Modify existing employee details.
- **Delete an Employee:** Remove an employee's record from the database.
- **Error Handling:** Includes error messages and response codes for invalid or unsuccessful operations.

## Technologies Used

- **Programming Language:** Python
- **Framework:** Flask (for API routing and request handling)
- **Database:** SQLite / MySQL / PostgreSQL (customizable based on project requirements)
- **Tools:** Postman (for testing API endpoints)

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/karthikkarthi-Ghost/REST-API-to-manage-employees-in-a-company_CRUD-operations.git
   cd REST-API-to-manage-employees-in-a-company_CRUD-operations
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   Update the database configuration in `config.py` according to your preferred database.

5. **Run the application:**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000`.

## API Endpoints

- **GET /employees**: Fetch all employee records.
- **GET /employees/{id}**: Fetch a specific employee by ID.
- **POST /employees**: Add a new employee. Requires a JSON body with employee details.
- **PUT /employees/{id}**: Update an existing employee's details.
- **DELETE /employees/{id}**: Delete an employee by ID.

### Example Request (POST)

```http
POST /employees
Content-Type: application/json

{
  "name": "John Doe",
  "designation": "Software Engineer",
  "department": "IT",
  "salary": 60000
}
```

### Example Response (JSON)

```json
{
  "message": "Employee created successfully",
  "employee": {
    "id": 1,
    "name": "John Doe",
    "designation": "Software Engineer",
    "department": "IT",
    "salary": 60000
  }
}
```

## Error Handling

The API provides meaningful error messages and appropriate HTTP status codes for scenarios such as:
- 404 Not Found: When an employee with the specified ID doesn't exist.
- 400 Bad Request: When required fields are missing or invalid data is provided.

## Testing

You can use Postman or any other API testing tool to validate the functionality of the endpoints. Unit tests are also provided in the `tests/` folder to ensure code quality.

## Contributing

Contributions are welcome! Please create a fork of the repository, make changes, and submit a pull request for review.

## License

This project is licensed under the MIT License.
