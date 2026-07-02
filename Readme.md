# Automation Testing

## Tool Used

- Selenium WebDriver
- Python
- Pytest
- Chrome Browser

---

## Automated Test Scenarios

### Scenario 1: Successful User Registration

**Objective:**
Verify that a new user can register successfully using valid details.

**Steps:**
1. Open the Registration page.
2. Enter a valid Name, Email, Password, and Confirm Password.
3. Click **Register**.

**Expected Result:**
- Registration is successful.
- API returns **201 Created**.
- Success message is displayed.

---

### Scenario 2: Registration with Duplicate Email

**Objective:**
Verify that the application prevents duplicate email registration.

**Steps:**
1. Open the Registration page.
2. Enter an email that already exists.
3. Fill the remaining fields.
4. Click **Register**.

**Expected Result:**
- Registration fails.
- API returns **409 Conflict**.
- "Email already exists" message is displayed.

---

### Scenario 3: Successful User Login

**Objective:**
Verify that a registered user can log in successfully.

**Steps:**
1. Open the Login page.
2. Enter a valid Email and Password.
3. Click **Login**.

**Expected Result:**
- Login is successful.
- JWT token is generated.
- User is redirected to the Dashboard.

---

### Scenario 4: Login with Invalid Password

**Objective:**
Verify that login fails when an incorrect password is entered.

**Steps:**
1. Open the Login page.
2. Enter a valid Email.
3. Enter an invalid Password.
4. Click **Login**.

**Expected Result:**
- Login fails.
- API returns **401 Unauthorized**.
- Error message is displayed.

---

### Scenario 5: Access Dashboard Without Login

**Objective:**
Verify that the Dashboard is protected and cannot be accessed without authentication.

**Steps:**
1. Open the Dashboard URL directly without logging in.

**Expected Result:**
- User is redirected to the Login page.
- Dashboard is not accessible without a valid JWT token.

---

## Notes

- The Selenium scripts are written in Python.
- URLs and element locators are assumed because the actual application was not provided.
- The scripts can be updated once the real application is available.