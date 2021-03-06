from unittest import skip
from unittest.mock import patch

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeHomeViewsTest(RecipeTestBase):

    def test_recipes_home_views_function_is_bugfree(self):
        view = resolve(
            reverse(viewname="recipes:home")
        )
        self.assertIs(view.func, views.home)

    def test_if_recipe_home_view_returns_OK_for_200_http_status_code(self):
        response = self.client.get(
            path=reverse(viewname="recipes:home")
        )
        self.assertEqual(response.status_code, 200)

    def test_if_recipe_home_view_loads_correct_template(self):
        response = self.client.get(
            path=reverse(viewname="recipes:home")
        )
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    @skip("WIP")
    def test_if_recipe_home_template_shows_no_recipe_found_if_no_recipes(self):
        response = self.client.get(
            path=reverse(viewname="recipes:home")
        )
        self.assertIn(
            "<h1>No recipes found!😢</h1>",
            response.content.decode("UTF-8")
        )
        # o fail está aqui apenas a título de aprendizado
        self.fail("this test is not fully implemented yet")

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()

        response = self.client.get(reverse("recipes:home"))

        content = response.content.decode("UTF-8")
        response_context_recipes = response.context["recipes"]

        self.assertIn("Recipe Title", content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_if_recipe_home_template_is_loading_not_published_recipes(self):
        """recipes:home is not intended to read non published recipes.
        In case it does, the test fails"""
        self.make_recipe(is_published=False)
        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            "<h1>No recipes found!😢</h1>",
            response.content.decode("UTF-8")
        )

    # patch pode ser usado como decorator
    # @patch("recipes.views.PER_PAGE", new=6)
    def test_recipe_home_paginator(self):
        for i in range(8):
            kwargs = {"slug": f"r{i}", "author_data": {"username": f"u{i}"}}
            self.make_recipe(**kwargs)

        # alternativamente, patch pode ser usado com context manager
        with patch("recipes.views.PER_PAGE", new=3):
            response = self.client.get(reverse("recipes:home"))
            recipe = response.context["recipes"]
            paginator = recipe.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)
