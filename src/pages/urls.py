from django.urls import path
from pages.views import homepageview, aboutpageview,  faqpageview

urlpatterns = [
    path('', homepageview),
    path('about', aboutpageview),
    path('faq', faqpageview),
]