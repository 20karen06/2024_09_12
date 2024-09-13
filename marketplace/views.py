from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Animal, Seller, Rating, Feedback, Cart, Wishlist, Payment
from .forms import AnimalForm, RatingForm, FeedbackForm


class HomeView(ListView):
    model = Animal
    template_name = 'marketplace/home.html'
    context_object_name = 'animals'
    paginate_by = 10


class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'marketplace/animal_detail.html'


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'marketplace/animal_form.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        payment = Payment.objects.filter(seller=self.request.user.seller, status=True).exists()
        if payment:
            return super().form_valid(form)
        else:
            return redirect('payment_page')


class RatingCreateView(LoginRequiredMixin, CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'marketplace/rating_form.html'

    def form_valid(self, form):
        form.instance.buyer = self.request.user
        form.instance.seller = get_object_or_404(Seller, id=self.kwargs['seller_id'])
        return super().form_valid(form)


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'marketplace/feedback_form.html'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.receiver = get_object_or_404(User, id=self.kwargs['receiver_id'])
        return super().form_valid(form)


class CartView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'marketplace/cart.html'


class WishlistView(LoginRequiredMixin, DetailView):
    model = Wishlist
    template_name = 'marketplace/wishlist.html'


class PaymentView(LoginRequiredMixin, CreateView):
    model = Payment
    fields = ['amount']
    template_name = 'marketplace/payment_form.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        form.instance.status = True  # Mark as paid, normally handle with Stripe API
        return super().form_valid(form)


class CrueltyInfoView(TemplateView):
    template_name = 'marketplace/cruelty_info.html'
