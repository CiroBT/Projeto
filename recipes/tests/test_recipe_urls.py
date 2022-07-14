from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_if_recipes_home_url_is_bugfree(self):
        url = reverse(viewname="recipes:home")
        self.assertEqual(url, "/")

    def test_if_recipes_category_url_is_bugfree(self):
        url = reverse(viewname="recipes:category", kwargs={"category_id": 1})
        self.assertEqual(url, "/recipes/category/1/")

    def test_if_recipes_recipe_url_is_bugfree(self):
        url = reverse(viewname="recipes:recipe", kwargs={"id": 10})
        self.assertEqual(url, "/recipes/10/")

    def test_recipe_search_url_is_correct(self):
        url = reverse("recipes:search")
        self.assertEqual(url, "/recipes/search/")
