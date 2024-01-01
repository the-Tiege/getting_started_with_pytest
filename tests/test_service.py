"""
Test Module for Service Functions

This module contains test cases for the functions in the 'service' module.
The tests use unittest.mock to create mock objects for external dependencies, such as the 'get_user_from_db' and 'requests.get' functions.

Test Functions:
- test_get_user_from_db(mock_get_user_from_db): Test case for the 'get_user_from_db' function.
- test_get_users(mock_get): Test case for the 'get_users' function with a successful response.
- test_get_users_error(mock_get): Test case for the 'get_users' function with an error response.

Example Usage:

Run the tests using pytest:
$ pytest test_service.py

Note: This module assumes the availability of the 'service' module and uses pytest for testing.
"""
import unittest.mock as mock

import pytest
import requests

import getting_started_pytest.service as service


@mock.patch("getting_started_pytest.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    """
    Test case for the 'get_user_from_db' function.

    Parameters:
    - mock_get_user_from_db: unittest.mock.Mock
                             Mock object for the 'get_user_from_db' function.
    """
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    expected_user_name = "Mocked Alice"

    assert user_name == expected_user_name


@mock.patch("requests.get")
def test_get_users(mock_get):
    """
    Test case for the 'get_users' function with a successful response.

    Parameters:
    - mock_get: unittest.mock.Mock
                Mock object for the 'requests.get' function.
    """
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    data = service.get_users()

    assert data == {"id": 1, "name": "John Doe"}


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    """
    Test case for the 'get_users' function with an error response.

    Parameters:
    - mock_get: unittest.mock.Mock
                Mock object for the 'requests.get' function.
    """
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        service.get_users()
