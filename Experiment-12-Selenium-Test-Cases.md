# Experiment 12: Develop Test Cases for a Containerized Application Using Selenium

## Aim
To develop and execute automated test cases for a containerized web application using Selenium WebDriver.

## Objectives
1. To understand automated testing using Selenium.
2. To test the accessibility of a containerized application.
3. To verify page titles and web elements.
4. To automate browser interactions.
5. To identify application errors through automated tests.

## Software Requirements
- Docker
- Selenium WebDriver
- Python 3
- Google Chrome or another supported browser
- A containerized web application
- Code editor

## Introduction
Selenium is an open-source automation framework used to test web applications through a browser. Docker packages an application and its dependencies into a container. Combining Selenium with a containerized application allows testers to verify application availability, page content, navigation, and basic functionality in a repeatable environment.

## Procedure
1. Create or use the containerized web application developed in Experiment 7.
2. Start the application container and map its port to the host machine.
3. Verify that the application is accessible through a browser.
4. Install Python and Selenium.
5. Create a Python test file.
6. Write test cases to verify the page title, page content, and application availability.
7. Run the tests using Selenium WebDriver.
8. Observe the test results and correct any failures.

## Sample Test Program

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ContainerAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:8080")

    def test_page_title(self):
        self.assertEqual(
            self.driver.title,
            "Docker Application"
        )

    def test_heading(self):
        heading = self.driver.find_element(
            By.TAG_NAME, "h1"
        )
        self.assertEqual(
            heading.text,
            "Hello from Docker!"
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

## Test Cases

| Test Case | Description | Expected Result |
|---|---|---|
| TC01 | Open the application URL | Application loads successfully |
| TC02 | Verify the page title | Title is Docker Application |
| TC03 | Verify the main heading | Heading displays Hello from Docker! |
| TC04 | Check page availability | The application responds correctly |
| TC05 | Verify page content | Expected text is displayed |

## Execution Commands

- `docker ps` – Checks whether the application container is running.
- `pip install selenium` – Installs the Selenium Python library.
- `python test_selenium.py` – Executes the automated test program.

## Expected Output
The browser opens the containerized application. The test program checks the page title and main heading. If both match the expected values, the test cases pass.

## Result
Developed sample Selenium test cases for a containerized web application and studied how automated browser testing verifies application functionality.

## Applications
- Automated functional testing
- Regression testing
- Containerized application validation
- Continuous Integration pipelines
- Software quality assurance
