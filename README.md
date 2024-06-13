# Restful Booker API Automation Suite (Python)

This project is an API automation suite created in Python for the Restful Booker API. It includes automated tests using the Pytest framework to ensure the functionality of the Restful Booker API endpoints.

## Installation

1. Ensure you have Python installed on your system (version 3.12 or higher).
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Install [Poetry](https://python-poetry.org/docs/#installation) if you haven't already:
5. Install project dependencies using Poetry:

```
poetry install
```

## To run the automated tests and generate an HTML report:

```
poetry run pytest --html=report.html
```

This will generate the html report in current directory with name of report (or whatever you passed as parameter in the above command).
