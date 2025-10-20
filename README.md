***

# HNG Internship Stage 0: Dynamic Profile API

This project is a simple RESTful API built with Django and Django REST Framework for the HNG Internship Stage 0 Backend Task. The API serves personal profile data and integrates with a third-party service to provide a random cat fact with each request.

The live, deployed application can be accessed here:
**[https://hngprofileproject-zichdan7442-tho7lc5q.leapcell.dev/](https://hngprofileproject-zichdan7442-tho7lc5q.leapcell.dev/)**

## Features & Acceptance Criteria Checklist

This project successfully implements all the core requirements of the task:

-   [x] A working GET `/me/` endpoint is accessible and returns a 200 OK status.
-   [x] The response structure strictly follows the required JSON schema.
-   [x] All required fields (`status`, `user`, `timestamp`, `fact`) are present.
-   [x] The `user` object contains `email`, `name`, and `stack` fields with valid string values.
-   [x] The `timestamp` field returns the current UTC time in ISO 8601 format and updates dynamically with every request.
-   [x] The `fact` field contains a cat fact fetched live from the Cat Facts API.
-   [x] A new cat fact is fetched on every request (not cached).
-   [x] The response `Content-Type` header is `application/json`.
-   [x] The code is well-structured and follows best practices for the Django stack.
-   [x] Robust logging and error handling are implemented for the external API call.
-   [x] The project includes interactive API documentation via Swagger UI.

## API Documentation

This project includes interactive API documentation generated with `drf-yasg` (Swagger UI). The documentation allows for easy exploration and testing of the endpoint directly in the browser.

**API Docs URL:** **[https://hngprofileproject-zichdan7442-tho7lc5q.leapcell.dev/](https://hngprofileproject-zichdan7442-tho7lc5q.leapcell.dev/)**

### Endpoint Details

-   **Endpoint:** `/me/`
-   **Method:** `GET`
-   **Description:** Retrieves the user's profile information and a random cat fact.
-   **Success Response (200 OK):**
    ```json
    {
      "status": "success",
      "user": {
        "email": "zichdan1999@gmail.com",
        "name": "Daniel Ezichi Okorie",
        "stack": "Python/Django"
      },
      "timestamp": "2025-10-20T12:00:00.123456Z",
      "fact": "A cat can jump up to five times its own height in a single bound."
    }
    ```
-   **Error Handling:** If the external Cat Facts API fails, the `fact` field will contain a descriptive error message, ensuring the endpoint remains stable.
    ```json
    {
        // ... other fields
        "fact": "Error: The request to the Cat Facts API timed out."
    }
    ```

## Technology Stack

-   **Backend:** Django, Django REST Framework
-   **Web Server:** Gunicorn
-   **API Documentation:** drf-yasg (Swagger UI)
-   **Deployment:** Leapcell

---

## Local Setup and Installation

Follow these instructions to set up and run the project on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   `pip` and `venv`
-   Git

### 2. Clone the Repository

```bash
git clone https://github.com/zichdan/hng_profile_project.git
cd hng_profile_project
```

### 3. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install Dependencies

All required packages are listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

This project uses environment variables for configuration. Create a `.env` file in the project's root directory. For this simple project, the key variables (`SECRET_KEY` and `DEBUG`) have safe defaults for local development.

### 6. Run the Development Server

You can now start the local development server.

```bash
python manage.py runserver
```

The application will be available at **`http://127.0.0.1:8000/`**.

## Environment Variables

For production deployment, the following environment variables are required. For local development, safe defaults are provided in `settings.py`.

| Variable | Description | Example Value |
| :--- |:---| :--- |
| `SECRET_KEY` | The secret key for your Django application. | `your-super-secret-django-key` |
| `DEBUG` | Toggles Django's debug mode. Should be `False` in production. | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of trusted hostnames. | `yourdomain.com,127.0.0.1` |


## How to Test the Endpoint

You can test the endpoint in several ways:

1.  **Via Swagger UI (Recommended):**
    -   Run the server and navigate to `http://127.0.0.1:8000/`.
    -   Expand the `GET /me/` endpoint.
    -   Click the **"Try it out"** button, then **"Execute"**.

2.  **Via Browser:**
    -   Simply navigate to `http://12-7.0.0.1:8000/me/` in your web browser.

3.  **Via `curl`:**
    -   Open your terminal and run the following command:
        ```bash
        curl http://127.0.0.1:8000/me/
        ```

## Author

-   **Name:** Daniel Ezichi Okorie
-   **Email:** zichdan1999@gmail.com





***
