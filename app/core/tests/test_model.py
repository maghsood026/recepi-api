from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):
    def test_create_model(self):
        email = "maghsood026@yahoo.com"
        password = "M#12345"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalized_email(self):
        email = "maghsood026@YAHOO.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password="test1234"
        )
        self.assertEqual(user.email, email.lower())

    def test_raise_value_error_for_invalid_email(self):
        email = None
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=email, password='test123')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            email='maghsood95@gmail.com',
            password="M#123456"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
