from django.urls import path

from .views import blog, post

urlpatterns = [
    path('', blog, name="blog"),
    path('<int:id>/', post, name='post'),
]
