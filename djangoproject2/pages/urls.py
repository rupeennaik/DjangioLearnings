from django.urls import path
from .views import HomePageView, AboutUsPageView, BasePageView

urlpatterns =[

    path("", BasePageView.as_view(), name = "Base"),
    path("aboutus/", AboutUsPageView.as_view(), name = "AboutUs"),
    path("home/", HomePageView.as_view(), name = "Home"),
]
