from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    """
    Form for user registration.

    Fields:
    - username: CharField for username with validation on length and widget for styling.
    - email: EmailField for email with validation on length and widget for styling.
    - password1: CharField for password with validation on length and widget for password input.
    - password2: CharField for confirming password with validation on length and widget for password input.

    """
    username = forms.CharField(
        label='Username',
        max_length=10,
        min_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        max_length=20,
        min_length=5,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        max_length=15,
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        max_length=15,
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class PaymentForm(forms.Form):
    """
    Form for payment details.

    Fields:
    - payment_method: ChoiceField for selecting payment method with predefined choices and radio widget.
    - first_name: CharField for first name.
    - last_name: CharField for last name.
    - email: EmailField for email.
    - address: CharField for address.
    - postal_code: CharField for postal code.
    - city: CharField for city.

    """
    CARD_CHOICES = [
        ('Mastercard', 'Mastercard'),
        ('Visa', 'Visa'),
        ('American_Express', 'American Express'),
    ]
    
    payment_method = forms.ChoiceField(
        choices=CARD_CHOICES,
        widget=forms.RadioSelect
    )
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    address = forms.CharField(max_length=250)
    postal_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=100)


class ContactForm(forms.Form):
    """
    Form for contacting the website.

    Fields:
    - name: CharField for user's name.
    - email: EmailField for user's email.
    - message: CharField for user's message with TextArea widget.

    """
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")

