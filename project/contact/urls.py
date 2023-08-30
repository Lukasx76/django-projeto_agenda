from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/create/', views.create, name='create'),
    path('contact/search/', views.search, name='search'),
    path('contact/<int:contact_id>/', views.contact, name='contact'),
]