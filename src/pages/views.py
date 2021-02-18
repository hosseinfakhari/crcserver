from django.shortcuts import render

# Create your views here.
def homepageview(request):
    return render(request, 'pages/homepage.html', {})

def aboutpageview(request):
    return render(request, 'pages/about.html', {})

def faqpageview(request):
    return render(request, 'pages/faq.html', {})