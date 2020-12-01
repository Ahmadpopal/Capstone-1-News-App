from unittest import TestCase
from app import app


class Routes(TestCase):

    # Home Page Route Testing
    def test_indexPage(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<h3 class='mt-4'>Top Headlines</h3>", html)
            self.assertIn("<h3 class='mt-2'>Tech News </h3>", html)
            self.assertIn("<h3 class='mt-2'>Region News</h3>", html)

    # Headlines Route redirecting  Testing
    def test_headlinesPage(self):
        with app.test_client() as client:
            res = client.get("/headlines")

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, "http://localhost/login")

    # Headlines follow Route Testing
    def test_headlinesPage_followed(self):
        with app.test_client() as client:
            res = client.get("/headlines", follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                "<h3 class='h3 m-4'>Sign In to your Account</h3>", html)

    # Search Route redirecting  Testing
    def test_search(self):
        with app.test_client() as client:
            res = client.get("/search", data={"search": ""})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, "http://localhost/login")

    # Region Redirecting Route Testing
    def test_Region_US(self):
        with app.test_client() as client:
            res = client.get("/region/us")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, "http://localhost/login")

     # Headlines follow Route Testing
    def test_Region_US_Followed(self):
        with app.test_client() as client:
            res = client.get("/region/us", follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                "<h3 class='h3 m-4'>Sign In to your Account</h3>", html)
