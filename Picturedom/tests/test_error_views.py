from django.test import TestCase


class TestErrorViews(TestCase):
    def test_error_400_view(self):
        response = self.client.get('/400/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.reason_phrase, 'Bad Request')
        self.assertTemplateUsed(response=response, template_name='errors/400.html')

    def test_error_403_view(self):
        response = self.client.get('/403/')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.reason_phrase, 'Forbidden')
        self.assertTemplateUsed(response=response, template_name='errors/403.html')

    def test_error_404_view(self):
        response = self.client.get('/404/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.reason_phrase, 'Not Found')
        self.assertTemplateUsed(response=response, template_name='errors/404.html')

    def test_error_500_view(self):
        # when set the raise_request_exception to False it gives the 500 status code
        self.client.raise_request_exception = False
        response = self.client.get('/500/')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.reason_phrase, 'Internal Server Error')
        self.assertTemplateUsed(response=response, template_name='errors/500.html')

