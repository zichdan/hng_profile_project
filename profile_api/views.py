# profile_api/views.py

import logging
import requests
from datetime import datetime, timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Get a logger instance specific to this module.
# The logger is configured in `settings.py`.
logger = logging.getLogger(__name__)

# URL for the external Cat Facts API.
CAT_FACT_API_URL = "https://catfact.ninja/fact"


@api_view(['GET'])
def get_profile(request):
    """
    An API endpoint that returns a developer's profile information along with a
    dynamic, random cat fact fetched from an external API.

    This endpoint is designed with robust error handling and logging to ensure
    reliability and traceability.
    """
    
    logger.info("Request received for /me endpoint.")

    # --- 1. Fetch Dynamic Cat Fact ---
    cat_fact = None
    try:
        # It's crucial to set a timeout for any external API call to prevent
        # the server from hanging indefinitely if the external service is unresponsive.
        logger.debug(f"Attempting to fetch cat fact from: {CAT_FACT_API_URL}")
        response = requests.get(CAT_FACT_API_URL, timeout=10) # 10-second timeout

        # Raise an HTTPError if the HTTP request returned an unsuccessful status code.
        response.raise_for_status()

        # Extract the fact from the JSON response.
        cat_fact = response.json().get("fact")
        logger.info("Successfully fetched a random cat fact.")

    except requests.exceptions.Timeout:
        # This block catches connection timeouts.
        error_message = "The request to the Cat Facts API timed out."
        logger.error(error_message)
        cat_fact = f"Error: {error_message}"
        
    except requests.exceptions.RequestException as e:
        # This is a broad exception that catches all other `requests` related errors,
        # such as connection errors, DNS failures, or invalid responses.
        error_message = f"Failed to connect to the Cat Facts API: {e}"
        logger.error(error_message)
        cat_fact = f"Error: {error_message}"
        
    except Exception as e:
        # A general fallback exception to catch any other unexpected errors,
        # such as issues with JSON parsing if the API returns malformed data.
        error_message = f"An unexpected error occurred while fetching the cat fact: {e}"
        logger.error(error_message)
        cat_fact = f"Error: {error_message}"


    # --- 2. Prepare the Response Data ---
    try:
        # Hardcoded user data as per the task. In a real application,
        # this would typically come from the authenticated user's profile (request.user).
        user_data = {
            "email": "zichdan1999@gmail.com",
            "name": "DANIEL EZICHI OKORIE",
            "stack": "Python/Django"
        }

        # Generate the current timestamp in UTC ISO 8601 format.
        # This ensures the timestamp is dynamic for every request.
        current_utc_time = datetime.now(timezone.utc).isoformat()

        # Assemble the final response payload according to the specified structure.
        response_payload = {
            "status": "success",
            "user": user_data,
            "timestamp": current_utc_time,
            "fact": cat_fact if cat_fact else "Could not retrieve a cat fact at this time."
        }
        
        logger.info("Successfully assembled the response payload.")
        
        # Return the final JSON response with a 200 OK status.
        return Response(response_payload, status=status.HTTP_200_OK)

    except Exception as e:
        # This is a critical fallback. If an error occurs while assembling the
        # response, it indicates a server-side problem.
        critical_error_msg = f"A critical error occurred while preparing the response: {e}"
        logger.critical(critical_error_msg)
        
        # Return a 500 Internal Server Error response.
        return Response(
            {"status": "error", "message": "An internal server error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )