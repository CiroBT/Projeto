from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=1)
        self.assertEqual([1, 2, 3, 4], pagination["pagination"])

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa 501
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=1)
        self.assertEqual([1, 2, 3, 4], pagination["pagination"])

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=2)
        self.assertEqual([1, 2, 3, 4], pagination["pagination"])

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=3)
        self.assertEqual([2, 3, 4, 5], pagination["pagination"])

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=4)
        self.assertEqual([3, 4, 5, 6], pagination["pagination"])

    def test_make_sure_middle_range_are_correct(self):

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=10)
        self.assertEqual([9, 10, 11, 12], pagination["pagination"])

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=12)
        self.assertEqual([11, 12, 13, 14], pagination["pagination"])

    def test_make_pagination_range_is_static_when_next_page_is_last_page(self):

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=18)
        self.assertEqual([17, 18, 19, 20], pagination["pagination"])

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=19)
        self.assertEqual([17, 18, 19, 20], pagination["pagination"])

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), page_qty=4, current_page=20)
        self.assertEqual([17, 18, 19, 20], pagination["pagination"])
