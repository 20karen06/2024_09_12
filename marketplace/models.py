from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    residential_address = models.CharField(max_length=155)

    def __str__(self):
        return self.user.username


class Animal(models.Model):
    ANIMAL_TYPES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('rabbit', 'Rabbit'),
        ('other', 'Other')
    ]
    sex_choices = [('M', 'Male'), ('F', 'Female')]
    value = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    animal_type = models.CharField(max_length=10, choices=ANIMAL_TYPES)
    breed = models.CharField(max_length=100)
    character_description = models.TextField()
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1, choices=sex_choices)
    picture = models.ImageField(upload_to='animal_pics/')
    is_purebred = models.BooleanField(default=False)
    is_neutered = models.BooleanField(default=False)
    is_available_for_adoption = models.BooleanField(default=True)
    if is_available_for_adoption is False:
        amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.breed} ({self.animal_type})"


class Rating(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='ratings')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return f"Rating: {self.rating} by {self.buyer.username} for {self.seller.user.username}"


class Feedback(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    animals = models.ManyToManyField(Animal, blank=True)


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    animals = models.ManyToManyField(Animal, blank=True)


class Payment(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment by {self.seller.user.username}-{'Paid' if self.status else 'Pending'}"
