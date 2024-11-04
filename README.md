# ContactListApp_API

### Project Overview
This project automates API testing for the Contact List App .

### Project Structure
- **api/**: Contains files for each page of the web application, with methods representing user actions (e.g., filling forms, clicking buttons, verifying elements).
- **tests/**: Contains test files for each page, validating the logic and interactions defined in the corresponding page files.

### Tech Stack
- **Python**
- **Selenium WebDriver**
- **pytest** for running tests and generating reports


### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AlesiaLu/ContactListApp_API.git
    ```

2. **Install dependencies**:
    Ensure you have Python and pip installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the tests**:
    Execute all tests using **pytest**:
    ```bash
    pytest
    ```

4. **Generate a test report**:
 To create HTML-report с pytest-html, run:
    ```bash
    pytest ./tests --html=report.html
    ```

### Example Usage
To run a specific test, specify the test file path:
```bash
pytest tests/test_login.py
```
This runs the test suite for the login, ensuring that functionalities like successful login and error messaging work as expected.
