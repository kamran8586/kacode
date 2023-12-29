# API Endpoints Documentation

## Authentication

- **User Registration**
  - Endpoint: `/auth/register/`
  - Description: Registers a new user.
  - Method: `POST`
  
- **User Login**
  - Endpoint: `/auth/signin/`
  - Description: Logs in a user.
  - Method: `POST`
  
- **Change Password**
  - Endpoint: `/auth/changepassword/`
  - Description: Allows a user to change their password.
  - Method: `POST`

## Code Part

### Problem Related Endpoints

- **List Problems**
  - Endpoint: `/problems/`
  - Description: Lists all problems.
  - Methods: `GET`

- **Create Problem**
  - Endpoint: `/problems/`
  - Description: Creates a new problem.
  - Methods: `POST`

- **Retrieve Problem Details**
  - Endpoint: `/problems/<int:problem_id>/`
  - Description: Retrieves details for a specific problem.
  - Methods: `GET`

- **Update Problem**
  - Endpoint: `/problems/<int:problem_id>/`
  - Description: Updates details for a specific problem.
  - Methods: `PUT`

- **Delete Problem**
  - Endpoint: `/problems/<int:problem_id>/`
  - Description: Deletes a specific problem.
  - Methods: `DELETE`

### Submission Related Endpoints

- **List Submissions for a Problem**
  - Endpoint: `/code/<int:problem_id>/submissions/`
  - Description: Lists all submissions for a specific problem.
  - Methods: `GET`

- **Create Submission for a Problem**
  - Endpoint: `/code/<int:problem_id>/submissions/`
  - Description: Creates a new submission for a specific problem.
  - Methods: `POST`

- **Retrieve Submission Details**
  - Endpoint: `/code/<int:problem_id>/submissions/<int:submission_id>/`
  - Description: Retrieves details for a specific submission.
  - Methods: `GET`

- **Update Submission**
  - Endpoint: `/code/<int:problem_id>/submissions/<int:submission_id>/`
  - Description: Updates details for a specific submission.
  - Methods: `PUT`

- **Delete Submission**
  - Endpoint: `/code/<int:problem_id>/submissions/<int:submission_id>/`
  - Description: Deletes a specific submission.
  - Methods: `DELETE`

Note: The submission URLs are now nested under `/problems/<int:problem_id>/submissions/` to ensure that submissions are retrieved in the context of a specific problem. Adjust the documentation based on your actual implementation details and any additional information you want to provide.

### Course Related Endpoints

- **List Courses**
  - Endpoint: `/courses/`
  - Description: Lists all courses.
  - Methods: `GET`

- **Create Course**
  - Endpoint: `/courses/`
  - Description: Creates a new course.
  - Methods: `POST`

- **Retrieve Course Details**
  - Endpoint: `/courses/<int:course_id>/`
  - Description: Retrieves details for a specific course.
  - Methods: `GET`

- **Update Course**
  - Endpoint: `/courses/<int:course_id>/`
  - Description: Updates details for a specific course.
  - Methods: `PUT`

- **Delete Course**
  - Endpoint: `/courses/<int:course_id>/`
  - Description: Deletes a specific course.
  - Methods: `DELETE`

- **List Comments for a Course**
  - Endpoint: `/courses/co/<int:course_id>/comments/`
  - Description: Lists all comments for a specific course.
  - Methods: `GET`

- **Create Comment for a Course**
  - Endpoint: `/courses/co/<int:course_id>/comments/`
  - Description: Creates a new comment for a specific course.
  - Methods: `POST`

Note: The course-related URLs are nested under `/courses/` and `/courses/<int:course_id>/` to ensure proper organization. Adjust the documentation based on your actual implementation details and any additional information you want to provide.
