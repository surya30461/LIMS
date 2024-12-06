# LIMS
Reverse Engineering Project

Secure LIMS Application
This project implements a basic Laboratory Information Management System (LIMS) with a focus on data security and user authentication. It was developed from scratch in Django and Python within two weeks, after pivoting from an initial plan due to compatibility issues.

Features
CRUD Operations:
Create, Read, Update, and Delete functionality for managing sample data.
Data Encryption:
Sensitive fields (name, sample_type) are encrypted using django-encrypted-model-fields to ensure secure storage in the database.
User Authentication:
Login system built on Django's default authentication framework.
Planned support for Multi-Factor Authentication (MFA).
Enhanced UI:
User-friendly interface styled with Bootstrap for seamless interactions.
Technologies Used
Backend: Django
Frontend: HTML, CSS, Bootstrap
Database: SQLite
Encryption: cryptography library with django-encrypted-model-fields
Challenges
Initial plan to reverse-engineer a GitHub-based LIMS built on Python 2.7 faced compatibility issues with Python 3.13.
Pivoted to a new plan, focusing on building a secure LIMS-like system from scratch.
Future Work
Full implementation of Multi-Factor Authentication (MFA).
Comprehensive testing for vulnerabilities.
Deployment to a production-ready environment.
