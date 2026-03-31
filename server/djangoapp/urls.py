from django.urls import path
from . import views

urlpatterns = [
    # AUTH
    path('login/', views.login_user),
    path('logout/', views.logout_user),

    # DEALERS
    path('fetchDealers', views.fetchDealers),
    path('fetchDealer/<int:dealer_id>', views.fetchDealer),
    path('fetchDealersByState/<str:state>', views.fetchDealersByState),

    # REVIEWS
    path('fetchReviews/dealer/<int:dealer_id>', views.fetchReviews),

    # CARS
    path('get_cars', views.get_cars),

    # SENTIMENT
    path('analyze/<str:text>', views.analyze),
]