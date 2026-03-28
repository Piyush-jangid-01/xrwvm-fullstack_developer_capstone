from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user),
    path('logout/', views.logout_user),

    path('get_dealers/', views.get_dealers),
    path('get_dealer/<int:dealer_id>/', views.get_dealer_by_id),
    path('get_dealers_by_state/<str:state>/', views.get_dealers_by_state),
    path('get_reviews/<int:dealer_id>/', views.get_dealer_reviews),
]