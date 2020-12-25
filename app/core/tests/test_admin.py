from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class TestAdmin(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@yahoo.com',
            password='M#123456.com'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="maghsood026ss1@gmail.com",
            password='test1234',
        )

    def test_user_list(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.admin_user.email)

    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_add_new_user(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
