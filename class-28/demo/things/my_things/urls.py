from django.urls import path
from .views import  ( 
                        ListThingView,
                        CreateThingView,
                        DeleteThingView,
                        UpdateThingView,
                        DetailThingView
                    )
urlpatterns = [
        path('', ListThingView.as_view(), name = 'thing_list'),
        path('<int:pk>', DetailThingView.as_view(), name = 'thing_detail'),
        path('create/', CreateThingView.as_view(), name = 'thing_create'),
        path('delete/<int:pk>', DeleteThingView.as_view(), name = 'thing_delete'),
        path('update/<int:pk>', UpdateThingView.as_view(), name = 'thing_update'),
        

]