from django.shortcuts import render


def home_view(request):
    template = "base.html"
    context = {}
    return render(request, template, context)
