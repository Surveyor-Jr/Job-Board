from django.shortcuts import render


def landing_page(request):
    return render(request, 'public_views/landing_page.html')
