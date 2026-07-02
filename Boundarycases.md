# Boundary Test Cases

# QA Intern Assignment - User Authentication & Authorization (JWT)

---

## BC_001 - Name Length: 4 Characters (Fail)

**Field**
Name

**Boundary Value**
4 characters

**Test Data**
John

**Expected Result**
- Validation error is displayed.
- Registration is not allowed.
- Backend returns **400 Bad Request** if the request is submitted.

**Priority**
High

---

## BC_002 - Name Length: 5 Characters (Pass)

**Field**
Name

**Boundary Value**
5 characters

**Test Data**
James

**Expected Result**
- Name is accepted.
- User can continue with registration.

**Priority**
High

---

## BC_003 - Name Length: 24 Characters (Pass)

**Field**
Name

**Boundary Value**
24 characters

**Test Data**
ABCDEFGHIJKLMNOPQRSTUVWX

**Expected Result**
- Name is accepted.
- Registration proceeds successfully.

**Priority**
High

---

## BC_004 - Name Length: 25 Characters (Fail)

**Field**
Name

**Boundary Value**
25 characters

**Test Data**
ABCDEFGHIJKLMNOPQRSTUVWXY

**Expected Result**
- Validation error is displayed.
- Registration is blocked.
- Backend returns **400 Bad Request** if submitted.

**Priority**
High

---

## BC_005 - Password Length: 11 Characters (Fail)

**Field**
Password

**Boundary Value**
11 characters

**Test Data**
Pass1234567

**Expected Result**
- Validation error indicating password must be at least 12 characters.
- Registration is not allowed.

**Priority**
High

---

## BC_006 - Password Length: 12 Characters (Pass)

**Field**
Password

**Boundary Value**
12 characters

**Test Data**
Pass12345678

**Expected Result**
- Password is accepted.
- User can continue registration.

**Priority**
High

---

## BC_007 - Email in Uppercase

**Field**
Email

**Boundary Case**
Uppercase characters

**Test Data**
JOHN@EXAMPLE.COM

**Expected Result**
- Email is accepted.
- Email is converted to lowercase before storage.
- Registration succeeds if email is unique.

**Priority**
Medium

---

## BC_008 - Email with Leading and Trailing Spaces

**Field**
Email

**Boundary Case**
Whitespace before and after email

**Test Data**
"  john@example.com  "

**Expected Result**
- Leading and trailing spaces are trimmed.
- Email is validated correctly.
- Registration succeeds if email is unique.

**Priority**
Medium

---

## BC_009 - Very Long Email Address

**Field**
Email

**Boundary Case**
Maximum practical email length

**Test Data**
verylongemailaddresswithmanycharacters123456789@exampledomainwithaverylongname.com

**Expected Result**
- Email is validated according to application rules.
- If within the supported length, registration succeeds.
- Otherwise, appropriate validation error is shown.

**Priority**
Medium

---

## BC_010 - Rate Limiting: 10 Registration Attempts

**Feature**
Rate Limiting

**Boundary Value**
10 registration attempts within one hour from the same IP

**Test Data**
10 valid registration requests

**Expected Result**
- All 10 requests are processed normally.
- No rate-limit error is returned.

**Priority**
High

---

## BC_011 - Rate Limiting: 11th Registration Attempt

**Feature**
Rate Limiting

**Boundary Value**
11th registration attempt within one hour from the same IP

**Test Data**
11 valid registration requests

**Expected Result**
- API returns **429 Too Many Requests**.
- Registration is blocked.
- Appropriate error message is displayed.

**Priority**
High

---