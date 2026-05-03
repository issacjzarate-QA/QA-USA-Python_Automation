                                        🚕 Urban Routes – Automated UI Testing with Selenium (Project 8)

    This project represents the moment where everything I learned in the QA program finally came together
    Page Object Model, Selenium, locators, waits, assertions, user flows, debugging, and real‑world test design.

Urban Routes is a web application that allows users to enter an address, choose a taxi plan, add extras (like blankets or ice cream), verify their phone number, and order a ride.

My goal in this project was to automate the entire end‑to‑end flow using clean, maintainable POM structure and realistic user behavior.

🎯 Project Objectives
Build a full POM automation framework

Use Selenium WebDriver with explicit waits

Automate the complete taxi‑ordering flow

Validate UI behavior with meaningful assertions

Handle dynamic elements (modals, toggles, counters)

Retrieve SMS verification codes through browser logs

Demonstrate clean test design and modular code

This project is the continuation of Project 7 — but now with full Selenium implementation and POM structure.

🧠 What I Learned (My Thought Process)
This project wasn’t just “write tests.”
It was about learning how a QA engineer thinks:

Breaking down a complex flow into reusable page methods

Choosing the right locators (ID when possible, XPath when necessary)

Using WebDriverWait instead of sleeps

Designing tests that mimic real user behavior

Debugging modal windows and focus issues

Understanding how UI state changes (active classes, checked properties)

Keeping tests readable and maintainable

Using helper utilities like retrieve_phone_code() to handle dynamic data

Every test in this suite reflects a real decision I had to make as I learned how to automate like a professional.

🏗 Tech Stack
Python 3

Selenium 4

Pytest

Page Object Model (POM)

ChromeDriver

Explicit Waits (WebDriverWait + EC)

Helper utilities for SMS code retrieval

📁 Project Structure
Code
QA-USA-Python_Automation/
│── main.py               # Test suite (pytest)
│── pages.py              # Page Object Model class
│── data.py               # Test data & constants
│── helpers.py            # Utility functions (SMS code, URL check)
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
🧩 Key Features Automated
✔ Setting Pickup & Destination Addresses
Inputs values

Retrieves them

Asserts correctness

✔ Selecting the “Supportive” Tariff
Opens tariff menu

Clicks Supportive

Verifies active state via class attribute

✔ Phone Number + SMS Verification
Enters phone number

Retrieves SMS code from browser logs

Enters code

Confirms login

✔ Adding a Credit Card
Opens payment modal

Enters card number + code

Handles focus issues (TAB/click outside)

Verifies card is linked

✔ Writing a Comment for the Driver
Inputs message

Asserts stored value

✔ Ordering Blanket & Handkerchiefs
Toggles slider

Verifies checkbox state

✔ Ordering 2 Ice Creams
Clicks “+” twice

Asserts counter value

✔ Ordering a Taxi
Completes full flow

Verifies “Car search” modal appears

🧪 How to Run the Tests
Install dependencies:

Code
pip install -r requirements.txt
Run the test suite:

Code
pytest main.py -v
Make sure the Urban Routes server is running — the test suite checks this automatically using helpers.is_url_reachable().

🧱 Page Object Model (POM) Design
All UI interactions live inside pages.py, including:

Locators

Input methods

Click actions

Assertions helpers

Modal handling

Counter logic

Toggle logic

This keeps tests in main.py clean, readable, and focused on behavior — not Selenium details.

🔍 Example Test Flow (Readable & Realistic)
python
def test_fill_phone_number(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    page = UrbanRoutesPage(self.driver)

    page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
    page.click_call_taxi()
    page.click_supportive()

    page.click_phone_field()
    page.enter_phone_number(data.PHONE_NUMBER)

    code = helpers.retrieve_phone_code(self.driver)
    page.enter_sms_code(code)

    assert page.get_phone_value() == data.PHONE_NUMBER
This is the style I aimed for:
clear, modular, and easy to understand.

🚀 Why This Project Matters
This project shows that I can:

Build a real automation framework

Use POM correctly

Handle dynamic UI behavior

Think like a QA engineer

Write clean, maintainable tests

Debug issues with locators, waits, and modals

Automate a full end‑to‑end user journey

It represents a major milestone in my QA engineering journey — the moment where everything clicked.

🙌 Author
Issac J. Zarate  
QA Engineer — Manual & Automation
Focused on clean test design, real‑world workflows, and continuous learning.
