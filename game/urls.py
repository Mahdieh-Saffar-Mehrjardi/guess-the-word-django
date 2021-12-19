from django.urls import path
from .views import guess_word
app_name = 'game'
urlpatterns = [
    path('', guess_word, name = 'guess_word'),
]