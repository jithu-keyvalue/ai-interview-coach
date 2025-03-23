# 06-validate-input

## 🎯 Problem
The coach shouldn’t crash when we send bad input. Let’s validate and respond cleanly.

## ✅ Your Task
In create_user:
- Validate role is one of: developer, designer, product-manager
- validate place is present and is a string

In get_user:
- Return 404 if user not found, instead of crashing

## 🧪 Test
Use Swagger UI (http://localhost:8000/docs) to try:
- invalid role
- Missing/invalid place
- get user id=0
