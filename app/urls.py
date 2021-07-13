from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home_view'),
    path('new/',views.ContactCreateView.as_view(),name='create_view'),
    path('contact/detail/<int:pk>/',views.ContactDetailView.as_view(),name='detail_view'),
    path('search/',views.search,name='search'),
    path('contact/update/<int:pk>/',views.ContactUpdateView.as_view(),name='update_view'),
    path('contact/delete/<int:pk>/',views.ContactDeleteView.as_view(),name='delete_view'),
    path('signup/',views.SignupView.as_view(),name='signup_view'),
    path('contact/',views.MessageView.as_view(),name='message_view'),
]