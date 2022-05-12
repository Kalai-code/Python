from django.urls import path
from .views import greetings
from .views import calc

urlpatterns = [
    # For URL: localhost:8000/multiple_views/hello and view function: hello
    # Usage Example URL: localhost:8000/multiple_views/hello/Kalai
    path('hello/<str:in_data>', greetings.hello, name='hello'),

    # For URL: localhost:8000/multiple_views/bday and view function: bday
    # Usage Example URL: localhost:8000/multiple_views/bday/Kalai
    path('bday/<str:in_data>', greetings.bday, name='bday'),
    
    # For URL: localhost:8000/multiple_views/num_square and view function: num_square
    # Usage Example URL: localhost:8000/multiple_views/num_square/3
    path('num_square/<int:in_number>', calc.num_square, name='num_square'),

    # For URL: localhost:8000/multiple_views/even_or_odd and view function: even_or_odd
    # Usage Example URL: localhost:8000/multiple_views/even_or_odd/1
    path('even_or_odd/<int:in_number>', calc.even_or_odd, name='even_or_odd'),
]