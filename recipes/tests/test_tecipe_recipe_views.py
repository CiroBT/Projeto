from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeRecipeViewsTest(RecipeTestBase):

    def test_recipes_recipe_views_function_is_bugfree(self):
        view = resolve(
            reverse(viewname="recipes:recipe", kwargs={"id": 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_template_is_loading_not_published_recipes(self):
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                "recipes:recipe",
                kwargs={
                    "id": recipe.id
                }
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse(viewname="recipes:recipe", kwargs={"id": 1000})
        )
        self.assertEqual(response.status_code, 404)
