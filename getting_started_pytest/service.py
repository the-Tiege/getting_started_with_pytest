"""
User Database Module

This module provides functions to interact with a local user database and an external user API.

Functions:
- get_user_from_db(user_id): Retrieves a user from the local database based on the user ID.
- get_users(): Retrieves a list of users from an external API (jsonplaceholder.typicode.com).
              Raises an HTTPError if the request is unsuccessful.

Note: The local database is a simple dictionary for demonstration purposes.
"""

import requests

# A simple local user database
database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}


def get_user_from_db(user_id: int) -> str:
    """
    Retrieve a user from the local database based on the user ID.

    Parameters:
    - user_id: int
               The ID of the user to retrieve.

    Returns:
    str or None: The name of the user if found, None if the user ID is not present in the database.
    """
    return database.get(user_id)


def get_users() -> list:
    """
    Retrieve a list of users from an external API.

    Returns:
    list: A list of user data obtained from the external API.

    Raises:
    requests.HTTPError: If the API request is unsuccessful (status code other than 200).
    """
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
