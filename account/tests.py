from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.

User = get_user_model()


class Registration(TestCase):

    def setUp(self) -> None:
        """
        Set up the test environment before each test case.

        This method creates an instance of APIClient to simulate HTTP requests.
        """
        self.client = APIClient()

    def test_registration_success(self):
        """
        Test successful user registration.

        This method tests the registration functionality by sending a POST request
        with valid email, password, and is_teacher flag set to True. It expects to
        receive an HTTP 201 Created status code, indicating successful registration.
        The test also verifies that a user object has been created with the provided email.
        """
        data = {
            "email": "test@example.com",
            "password": "testpassword",
            "is_teacher": True
        }
        response = self.client.post(
            path=reverse("user-list"),
            data=data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "test@example.com")

    def test_login_failure(self):
        """
        Test user registration failure due to missing password.

        This method tests the registration functionality by sending a POST request
        with a missing password field. It expects to receive an HTTP 400 Bad Request
        status code, indicating that the registration request was invalid.
        The test also verifies that no user object has been created in this scenario.
        """
        data = {
            "email": "test@example.com",
            "password": "",
            "is_teacher": True
        }
        response = self.client.post(
            path=reverse("user-list"),
            data=data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)


class LoginTest(TestCase):
    def setUp(self):
        """
        Set up the test environment before each test case.

        This method creates an instance of APIClient to simulate HTTP requests,
        and also creates a test user with a known email and password for login testing.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword")

    def test_login_success(self):
        """
        Test successful user login.

        This method tests the login functionality by sending a POST request
        with valid email and password. It expects to receive an HTTP 200 OK status 
        code and a JSON response containing "access" and "refresh" tokens.
        """
        data = {
            "email": "test@example.com",
            "password": "testpassword",
        }
        response = self.client.post(
            reverse("jwt-create"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_failure(self):
        """
        Test failed user login due to incorrect password.

        This method tests the login functionality by sending a POST request
        with a correct email but an incorrect password. It expects to receive
        The response should not contain "access" or "refresh" tokens.
        """
        data = {
            "email": "test@example.com",
            "password": "wrongpassword",  # Incorrect password should fail
        }
        response = self.client.post(
            reverse("jwt-create"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("access", response.data)
        self.assertNotIn("refresh", response.data)
