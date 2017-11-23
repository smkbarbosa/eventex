from django.test import TestCase

# Create your tests here.


class CertificateTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/certificate/')

    def test_get(self):
        """GET /certificate must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use certificate.html"""
        self.assertTemplateUsed(self.response, 'certificate.html')