from django.urls import path
from .views import (
                        ThingsListView,
                        ThingDetailView
                        )


urlpatterns = [
    path("", ThingsListView.as_view(), name="things_list"),
    path("<int:pk>", ThingDetailView.as_view(), name="things_detail"),

]