from django.urls import path
from .views import HomeView, AnimalDetailView, AnimalCreateView, RatingCreateView, FeedbackCreateView, CartView, \
    WishlistView, PaymentView, CrueltyInfoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('animal/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
    path('animal/create/', AnimalCreateView.as_view(), name='animal_create'),
    path('rating/<int:seller_id>/', RatingCreateView.as_view(), name='rate_seller'),
    path('feedback/<int:receiver_id>/', FeedbackCreateView.as_view(), name='feedback'),
    path('cart/', CartView.as_view(), name='cart'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('cruelty-info/', CrueltyInfoView.as_view(), name='cruelty_info'),
]
