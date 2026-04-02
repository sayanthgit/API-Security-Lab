API Security Testing Lab – IDOR Vulnerability
-Introduction
--------------

This project demonstrates an API security vulnerability known as IDOR (Insecure Direct Object Reference).
The goal of this lab is to understand how improper authorization can lead to unauthorized access to sensitive data and how to fix it.

What is IDOR?

IDOR occurs when an application exposes internal object references (like user IDs) without verifying whether the user is authorized to access that resource.

Project Structure
api-security-lab/

-vulnerable_app.py   # Vulnerable API (IDOR present)
-secure_app.py       # Fixed API (IDOR mitigated)
-README.md           # Project documentation

Vulnerability Description
--------------------------

In the vulnerable version:

The API allows users to access data using endpoints like:
/user/1
/user/2
There is no authorization check
Any user can access any other user's data by simply changing the ID

Exploitation (Attack)
--------------------

Using Burp Suite:

Intercept request:
GET /user/1
Modify request:
GET /user/2
Server response:
{
  "id": 2,
  "name": "Rahul"
}

 This shows unauthorized access to another user's data.

 Impact
 -------
-Unauthorized data exposure
-Privacy violation
-Potential data breach.

Fix Implemented

The vulnerability was fixed by implementing:

1. Authentication
Added a login system
Users receive a token after successful login
2. Authorization
Server validates user identity using the token
Users can only access their own data
3. Access Control Check
if user_id != requested_id:
    return "Access denied"

    Secure Behavior

After fixing:

User 1 can access /user/1 
User 1 cannot access /user/2 
-Key Learnings
Difference between authentication and authorization
Importance of access control in APIs
How IDOR vulnerabilities occur in real-world applications
How to test APIs using Burp Suite
How to implement secure coding practices

Conclusion
------------
This project highlights how a simple lack of authorization checks can lead to critical security issues. Implementing proper authentication and authorization mechanisms is essential to secure APIs against such attacks.
