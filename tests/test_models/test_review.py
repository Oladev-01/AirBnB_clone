#!/usr/bin/python3
import unittest
from models.review import Review
from models import storage
import datetime

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()
    def test_review_instances(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_instances_update(self):
        self.review.place_id = "124"
        self.review.user_id = "123"
        self.review.text = "a good institution"
        self.assertEqual(self.review.place_id, "124")
        self.assertEqual(self.review.user_id, "123")
        self.assertEqual(self.review.text, "a good institution")

if __name__ == "__main__":
    unittest.main()