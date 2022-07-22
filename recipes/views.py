import os

from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.pagination import make_pagination

from .models import Recipe

PER_PAGE = int(os.environ.get("PER_PAGE", 3))


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by("-id")
    page_obj, pagination_range = make_pagination(
        request=request, queryset=recipes, per_page=PER_PAGE)
    return render(
        request=request,
        template_name="recipes/pages/home.html",
        context={
            "recipes": page_obj,
            "pagination_range": pagination_range,
        }
    )


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by("-id")
    )
    page_obj, pagination_range = make_pagination(
        request=request, queryset=recipes, per_page=PER_PAGE)
    return render(
        request=request,
        template_name="recipes/pages/category.html",
        context={
            "recipes": page_obj,
            "pagination_range": pagination_range,
            "title": f"{recipes[0].category.name} - Category | ",
        }
    )


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)
    return render(
        request=request,
        template_name="recipes/pages/recipe-view.html",
        context={
            "recipe": recipe,
            "is_detail_page": True,
        }
    )


def search(request):
    search_term = request.GET.get("search", "").strip()
    if not search_term:
        raise Http404
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True,
    ).order_by("-id")
    page_obj, pagination_range = make_pagination(
        request=request, queryset=recipes, per_page=PER_PAGE)
    return render(request, "recipes/pages/search.html", {
        "page_title": f'search for "{search_term}" | ',
        "search_term": search_term,
        "recipes": page_obj,
        "pagination_range": pagination_range,
        "aditional_url_query": f"&search={search_term}",
    })
