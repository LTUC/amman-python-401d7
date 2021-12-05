from django.urls import path
from .views import AboutUsView

urlpatterns = [
    # path('/', HomeView.as_view(), name = 'main'),
    path('about-us/', AboutUsView.as_view(), name = 'about-us'),
]