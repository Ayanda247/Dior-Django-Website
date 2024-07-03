from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    """
    Form for user registration.

    :param username: CharField for username with validation on length and widget for styling.
    :type username: django.forms.CharField
    :param email: EmailField for email with validation on length and widget for styling.
    :type email: django.forms.EmailField
    :param password1: CharField for password with validation on length and widget for password input.
    :type password1: django.forms.CharField
    :param password2: CharField for confirming password with validation on length and widget for password input.
    :type password2: django.forms.CharField
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

    :param payment_method: ChoiceField for selecting payment method with predefined choices and radio widget.
    :type payment_method: django.forms.ChoiceField
    :param first_name: CharField for first name.
    :type first_name: django.forms.CharField
    :param last_name: CharField for last name.
    :type last_name: django.forms.CharField
    :param email: EmailField for email.
    :type email: django.forms.EmailField
    :param address: CharField for address.
    :type address: django.forms.CharField
    :param postal_code: CharField for postal code.
    :type postal_code: django.forms.CharField
    :param city: CharField for city.
    :type city: django.forms.CharField
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

    :param name: CharField for user's name.
    :type name: django.forms.CharField
    :param email: EmailField for user's email.
    :type email: django.forms.EmailField
    :param message: CharField for user's message with TextArea widget.
    :type message: django.forms.CharField
    """
    
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")


