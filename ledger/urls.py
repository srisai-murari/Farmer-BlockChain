
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ledger_home, name='ledger_home'),
    path('add/', views.add_demo_block, name='add_block'),
]
