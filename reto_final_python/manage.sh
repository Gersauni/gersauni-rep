#!/bin/bash
# Requires the database to be up
FLASK_ENV=development DATABASE_URI=postgresql://kratos:admin@127.0.0.1:5432/testing python3 manage.py
