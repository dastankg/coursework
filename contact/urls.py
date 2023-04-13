from django.urls import path

from .views import FeedbackView, subscribe

urlpatterns = [
    path('', FeedbackView.as_view(), name='feedback_view'),
    path('c/', subscribe, name='subscribe')
]
