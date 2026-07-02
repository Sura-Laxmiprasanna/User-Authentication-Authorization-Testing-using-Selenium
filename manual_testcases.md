# Manual Test Cases

# QA Intern Assignment - User Authentication & Authorization (JWT)

---

 ## TC_001 - Verify Successful User Registration

**Title**
Verify Successful User Registration

**Preconditions**
- Registration page is accessible.

**Steps**
1. Open the Registration page.
2. Enter a valid Name.
3. Enter a valid Email.
4. Enter a valid Password.
5. Enter the same Confirm Password.
6. Click **Register**.

**Test Data**
- Name: Sura
- Email: sura@gmail.com
- Password: Password1234
- Confirm Password: Password1234

**Expected Result**
- Registration succeeds.
- API returns **201 Created**.
- Success message is displayed.

**Priority**
High

---

## TC_002 - Verify Registration with Blank Name

**Preconditions**
- Registration page is open.

**Steps**
1. Leave Name blank.
2. Fill remaining fields.
3. Click Register.

**Test Data**
- Name: (Blank)
- Email: sura@example.com
- Password: Password1234

**Expected Result**
- "Name is required" validation appears.
- Backend returns **400 Bad Request** if submitted.

**Priority**
High

---

## TC_003 - Verify Name Length Less Than 5 Characters

**Preconditions**
- Registration page is open.

**Steps**
1. Enter Name with 4 characters.
2. Fill other fields.
3. Submit.

**Test Data**
- Name: Sura

**Expected Result**
- Validation error displayed.

**Priority**
High

---

## TC_004 - Verify Name Length Greater Than 24 Characters

**Preconditions**
- Registration page is open.

**Steps**
1. Enter a Name containing 25 characters.
2. Submit the form.

**Test Data**
- Name: SURALAXMIPRASANNASURALAXMIPRASANNA

**Expected Result**
- Validation error displayed.

**Priority**
High

---

## TC_005 - Verify Registration with Invalid Email Format

**Preconditions**
- Registration page is open.

**Steps**
1. Enter invalid email.
2. Complete remaining fields.
3. Submit.

**Test Data**
- Email: Ssuragmail.com

**Expected Result**
- Invalid email validation displayed.
- Backend returns **400 Bad Request**.

**Priority**
High

---

## TC_006 - Verify Registration with Duplicate Email

**Preconditions**
- User already exists with the email.

**Steps**
1. Enter an already registered email.
2. Fill remaining fields.
3. Submit.

**Test Data**
- Email: sura@example.com

**Expected Result**
- API returns **409 Conflict**.
- "Email already exists" message displayed.

**Priority**
High

---

## TC_007 - Verify Password Less Than 12 Characters

**Preconditions**
- Registration page is open.

**Steps**
1. Enter an 11-character password.
2. Submit.

**Test Data**
- Password: Pass1234567

**Expected Result**
- Password validation displayed.

**Priority**
High

---

## TC_008 - Verify Password Without Numbers

**Preconditions**
- Registration page is open.

**Steps**
1. Enter alphabet-only password.
2. Submit.

**Test Data**
- Password: PasswordOnly

**Expected Result**
- Password must contain letters and numbers.

**Priority**
Medium

---

## TC_009 - Verify Password Without Letters

**Preconditions**
- Registration page is open.

**Steps**
1. Enter numeric password only.
2. Submit.

**Test Data**
- Password: 123456789123

**Expected Result**
- Validation error displayed.
- Password must contain letters and numbers
**Priority**
Medium

---

## TC_010 - Verify Password and Confirm Password Mismatch

**Preconditions**
- Registration page is open.

**Steps**
1. Enter Password.
2. Enter different Confirm Password.
3. Submit.

**Test Data**
- Password: Password1234
- Confirm Password: Password5678

**Expected Result**
- "Passwords do not match" validation displayed.

**Priority**
High

---

## TC_011 - Verify Registration with Blank Email

**Preconditions**
- Registration page is open.

**Steps**
1. Leave Email blank.
2. Submit.

**Test Data**
- Email: Blank

**Expected Result**
- Email required validation displayed.

**Priority**
High

---

## TC_012 - Verify Registration with Blank Password

**Preconditions**
- Registration page is open.

**Steps**
1. Leave Password blank.
2. Submit.

**Test Data**
- Password: Blank

**Expected Result**
- Password required validation displayed.

**Priority**
High

---

## TC_013 - Verify Email is Converted to Lowercase

**Preconditions**
- Registration page is open.

**Steps**
1. Enter uppercase email.
2. Submit.

**Test Data**
- Email: SURA@EXAMPLE.COM

**Expected Result**
- Email stored as john@example.com.

**Priority**
Medium

---

## TC_014 - Verify Email with Leading and Trailing Spaces

**Preconditions**
- Registration page is open.

**Steps**
1. Enter email with spaces.
2. Submit.

**Test Data**
- Email: " sura@example.com "

**Expected Result**
- Spaces trimmed.
- Registration succeeds.

**Priority**
Medium

---

## TC_015 - Verify Registration with Special Characters in Name

**Preconditions**
- Registration page is open.

**Steps**
1. Enter special characters in Name.
2. Submit.

**Test Data**
- Name: John@#$

**Expected Result**
- Invalid input handled correctly.
- API returns **400 Bad Request** if input is not allowed.

**Priority**
Medium

---

## TC_016 - Verify Registration with XSS Input

**Preconditions**
- Registration page is open.

**Steps**
1. Enter `<script>alert('XSS')</script>` in Name.
2. Submit.

**Test Data**
- Name: `<script>alert('XSS')</script>`

**Expected Result**
- Script is not executed.
- Input is sanitized or rejected.

**Priority**
High

---

## TC_017 - Verify Successful Login

**Preconditions**
- User account exists.

**Steps**
1. Open Login page.
2. Enter valid Email.
3. Enter valid Password.
4. Click Login.

**Test Data**
- Email: sura@example.com
- Password: Password1234

**Expected Result**
- Login successful.
- JWT token returned.
- User redirected to Dashboard.

**Priority**
High

---

## TC_018 - Verify Login with Invalid Password

**Preconditions**
- User account exists.

**Steps**
1. Enter valid Email.
2. Enter incorrect Password.
3. Click Login.

**Test Data**
- Password: WrongPassword123

**Expected Result**
- API returns **401 Unauthorized**.
- Login fails.

**Priority**
High

---

## TC_019 - Verify Dashboard Access Without JWT

**Preconditions**
- User is not logged in.

**Steps**
1. Open Dashboard URL directly.

**Test Data**
- No JWT Token

**Expected Result**
- User is redirected to Login page.

**Priority**
High

---

## TC_020 - Verify Registration Rate Limiting

**Preconditions**
- Registration page is open.

**Steps**
1. Submit registration requests 11 times within one hour from the same IP.

**Test Data**
- Different valid emails

**Expected Result**
- First 10 attempts are accepted.
- 11th attempt returns **429 Too Many Requests**.

**Priority**
High

---

## TC_021 - Verify Concurrent Registration with Same Email (Conceptual)

**Preconditions**
- Two users attempt registration simultaneously.

**Steps**
1. User A submits registration.
2. User B submits registration using the same email at the same time.

**Test Data**
- Email: sura@example.com

**Expected Result**
- One registration succeeds (**201 Created**).
- Second request returns **409 Conflict**.

**Priority**
High
