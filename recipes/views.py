from django.shortcuts import render


def home(request):
    return render(request=request, template_name="recipes/pages/home.html", context={"exemplo": "exemplo"})
