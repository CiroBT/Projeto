from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewsTest(RecipeTestBase):

    def test_recipes_category_views_function_is_bugfree(self):
        view = resolve(
            reverse(viewname="recipes:category", kwargs={"category_id": 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipes_category_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse(viewname="recipes:category", kwargs={"category_id": 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_the_correct_recipe(self):
        title = "This is a detail page - it loads one recipe only"
        self.make_recipe(title=title)
        response = self.client.get(
            reverse("recipes:recipe", kwargs={"id": 1})
        )
        content = response.content.decode("UTF-8")
        self.assertIn(title, content)
