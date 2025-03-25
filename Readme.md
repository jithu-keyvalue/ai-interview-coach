💭 How can we simplify validation and keep our code clean?
We’ve been manually validating input — let’s use Pydantic to do it the clean way.

🎯 Problem  
Use Pydantic to cleanly validate and parse the user profile.

✅ Your Task
- Define a Pydantic model `User` for input to `/api/users` with validation logic:
  - `name`: min length 2, max_length 10
  - `role`: must be one of `"developer"`, `"designer"`, `"product-manager"`, `"tester"`
  - `place`: min length 2

🧪 Test
- Try valid and invalid requests using Swagger UI: http://localhost:8000/docs
