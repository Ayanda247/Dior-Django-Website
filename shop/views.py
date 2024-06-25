from django.shortcuts import render, get_object_or_404, redirect
from diorwebsite.settings import LOGOUT_URL
from .models import Category, Product, Order, OrderItem, Inquiry
from django.urls import reverse
from .forms import PaymentForm, ContactForm, UserRegistrationForm
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# -----------------------------------------------------------------------------
# User Profile View
# -----------------------------------------------------------------------------
@login_required
def profile(request):
    """
    Displays the user's profile page.

    This view fetches the logged-in user's information and displays it on the
    profile page. It also includes placeholders for previous orders and favorite
    items, which will need to be implemented based on your application's logic.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for the user's profile page.
    """
    # Fetch user information dynamically
    user = request.user

    # Placeholder for previous orders and favorite items
    previous_orders = []  # You will need to implement this logic
    favorite_items = []  # You will need to implement this logic

    context = {
        "user": user,
        "previous_orders": previous_orders,
        "favorite_items": favorite_items,
    }
    return render(request, "shop/profile.html", context)


# -----------------------------------------------------------------------------
# User Login View
# -----------------------------------------------------------------------------
def login_user(request):
    """
    Handles user login.

    This view processes the login form submission. If the form is valid, it
    authenticates the user and logs them in. If the login is successful, the
    user is redirected to the home page. Otherwise, error messages are displayed.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for the login page or a redirect to the home page.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("shop:home")  # Redirect to the home page
            else:
                # Handle invalid login attempts (e.g., display error messages)
                return render(
                    request,
                    "shop/registration/login.html",
                    {"form": form, "error": "Invalid username or password"},
                )
        else:
            # Handle invalid form submissions (e.g., display error messages)
            return render(
                request,
                "shop/registration/login.html",
                {"form": form, "error": "Form is not valid"},
            )
    else:
        form = AuthenticationForm()
        return render(request, "shop/registration/login.html", {"form": form})


# -----------------------------------------------------------------------------
# User Logout View
# -----------------------------------------------------------------------------
def logout_user(request):
    """
    Logs out the current user.

    This view logs out the user and redirects them to the home page.

    Args:
        request: The HTTP request object.

    Returns:
        A redirect to the home page.
    """
    logout(request)
    return redirect("shop:home")


# -----------------------------------------------------------------------------
# User Logout View (Alternative)
# -----------------------------------------------------------------------------
def LogoutView(request):
    """
    Logs out the current user (alternative implementation).

    This view logs out the user and redirects them to the home page. It also
    handles invalid request methods (e.g., GET requests) by returning an error
    response.

    Args:
        request: The HTTP request object.

    Returns:
        A redirect to the home page or an error response.
    """
    if request.method == "POST":
        logout(request)
        return redirect("shop:home")
    else:
        # Handle invalid request method (e.g., return an error message)
        return HttpResponse("Invalid request method.", status=405)


# -----------------------------------------------------------------------------
# User Registration View (Class-Based View)
# -----------------------------------------------------------------------------
class MyRegisterView(View):
    """
    Handles user registration.

    This class-based view processes the registration form submission. It
    validates the form data, checks for existing users, and creates a new
    user account if the form is valid. Error messages are displayed if the
    form is invalid or if there are conflicts with existing users.

    Attributes:
        template_name: The name of the template to render.
        form_class: The form class to use for registration.
    """

    template_name = "shop/register.html"
    form_class = UserRegistrationForm

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests for the registration page.

        This method renders the registration form.

        Args:
            request: The HTTP request object.

        Returns:
            A rendered template for the registration page.
        """
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for the registration form.

        This method processes the registration form submission. It validates
        the form data, checks for existing users, and creates a new user
        account if the form is valid. Error messages are displayed if the
        form is invalid or if there are conflicts with existing users.

        Args:
            request: The HTTP request object.

        Returns:
            A rendered template for the registration page or a redirect to
            the home page.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            email = form.cleaned_data["email"]

            if password1 != password2:
                messages.error(
                    request,
                    "Password doesn't match!",
                    extra_tags="alert alert-warning alert-dismissible fade show ",
                )
            elif User.objects.filter(email=email).exists():
                messages.error(
                    request,
                    "Email already exists!",
                    extra_tags="alert alert-warning alert-dismissible fade show ",
                )
            elif User.objects.filter(username=username).exists():
                messages.error(
                    request,
                    "Username already exists!",
                    extra_tags="alert alert-warning alert-dismissible fade show ",
                )
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email
                )
                messages.success(
                    request,
                    "Thanks for registering!",
                    extra_tags="alert alert-success alert-dismissible fade show",
                )
                return redirect("shop:home")
        return render(request, self.template_name, {"form": form})


# -----------------------------------------------------------------------------
# Purchase View
# -----------------------------------------------------------------------------
def purchase(request):
    """
    Handles product purchase.

    This view processes the purchase form submission. It validates the form
    data, processes the payment (assuming a successful payment for simplicity),
    creates an order and order item, and redirects to a thank you page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for the purchase page or a redirect to the thank
        you page.
    """
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process the payment here based on the selected payment method
            # For simplicity, let's assume the payment is successful
            # You would normally integrate with a payment gateway here

            # Create an order
            order = Order.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                address=form.cleaned_data["address"],
                postal_code=form.cleaned_data["postal_code"],
                city=form.cleaned_data["city"],
            )

            # Retrieve the product to be purchased
            product_id = request.POST["product_id"]
            product = Product.objects.get(id=product_id)

            # Create an order item
            OrderItem.objects.create(
                order=order, product=product, price=product.price, quantity=1
            )

            # Redirect to a thank you page
            return redirect(reverse("thank_you"))
    else:
        # If the request method is GET, render the purchase page
        # with the payment options and form
        form = PaymentForm()

    return render(request, "shop/purchase.html", {"form": form})


# -----------------------------------------------------------------------------
# Product List View
# -----------------------------------------------------------------------------
def product_list(request, category_slug=None):
    """
    Displays a list of products.

    This view retrieves all products or products filtered by a specific
    category (if a category slug is provided).

    Args:
        request: The HTTP request object.
        category_slug: The slug of the category to filter products by (optional).

    Returns:
        A rendered template for the product list page.
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(
        request,
        "shop/product_list.html",
        {"category": category, "categories": categories, "products": products},
    )


# -----------------------------------------------------------------------------
# Product List View (Alternative)
# -----------------------------------------------------------------------------
def product_list_by_category(request, category_slug):
    """
    Displays a list of products for a specific category (alternative implementation).

    This view retrieves all products belonging to a specific category.

    Args:
        request: The HTTP request object.
        category_slug: The slug of the category to filter products by.

    Returns:
        A rendered template for the product list page.
    """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(
        request, "shop/product_list.html", {"category": category, "products": products}
    )


# -----------------------------------------------------------------------------
# Product Detail View
# -----------------------------------------------------------------------------
def product_detail(request, id, slug):
    """
    Displays the details of a specific product.

    This view retrieves the details of a product based on its ID and slug.

    Args:
        request: The HTTP request object.
        id: The ID of the product.
        slug: The slug of the product.

    Returns:
        A rendered template for the product detail page.
    """
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, "shop/product_detail.html", {"product": product})


# -----------------------------------------------------------------------------
# Category List View
# -----------------------------------------------------------------------------
def category_list(request):
    """
    Displays a list of all categories.

    This view retrieves all categories and displays them on the category list
    page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for the category list page.
    """
    categories = Category.objects.all()
    return render(request, "shop/category_list.html", {"categories": categories})


# -----------------------------------------------------------------------------
# Home Page View
# -----------------------------------------------------------------------------
def home(request):
    """
    Displays the home page.

    This view retrieves a random selection of products and displays them on
    the home page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for the home page.
    """
    random_products = Product.objects.order_by("?")[:15]
    return render(request, "shop/home.html", {"random_products": random_products})


# -----------------------------------------------------------------------------
# Update Random Products View (AJAX)
# -----------------------------------------------------------------------------
def update_random_products(request):
    """
    Updates the random products displayed on the home page (AJAX).

    This view retrieves a new set of random products and returns the HTML
    for the product list, which can be used to update the home page via AJAX.

    Args:
        request: The HTTP request object.

    Returns:
        A JSON response containing the HTML for the updated product list.
    """
    random_products = Product.objects.order_by("?")[:15]
    html = render_to_string(
        "shop/random_products.html", {"random_products": random_products}
    )
    return JsonResponse({"html": html})


# -----------------------------------------------------------------------------
# Women's Products View
# -----------------------------------------------------------------------------
def womans(request):
    """
    Displays a list of women's products.

    This view retrieves products from specific categories related to women's
    fashion and displays them on the women's products page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for the women's products page.
    """
    products = Product.objects.filter(
        category__slug__in=[
            "womans",
            "womans-shoes",
            "beauty",
            "handbags-purse",
            "unisex-shoes",
        ]
    ).order_by("-category__slug")
    context = {
        "products": products,
        "category_slugs": [
            "womans",
            "womans-shoes",
            "beauty",
            "handbags-purse",
            "unisex-shoes",
        ],
    }
    return render(request, "shop/womans.html", context)


# -----------------------------------------------------------------------------
# Cologne and Beauty Products View
# -----------------------------------------------------------------------------
def cologneandbeauty(request):
    """
    Displays a list of cologne and beauty products.

    This view retrieves products from the "cologne" and "beauty" categories
    and displays them on the cologne and beauty products page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for the cologne and beauty products page.
    """
    products = Product.objects.filter(category__slug__in=["cologne", "beauty"])
    context = {
        "products": products,
        "category_slugs": ["cologne", "beauty"],
    }
    return render(request, "shop/cologneandbeauty.html", context)


# -----------------------------------------------------------------------------
# Men's Products View
# -----------------------------------------------------------------------------
def mens(request):
    """
    Displays a list of men's products.

    This view retrieves products from specific categories related to men's
    fashion and displays them on the men's products page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for the men's products page.
    """
    products = Product.objects.filter(
        category__slug__in=[
            "mens",
            "womans-shoes",
            "mens-shoes",
            "cologne",
            "unisex-shoes",
        ]
    ).order_by("-category__slug")
    context = {
        "products": products,
        "category_slugs": [
            "mens",
            "womans-shoes",
            "mens-shoes",
            "cologne",
            "unisex-shoes",
        ],
    }
    return render(request, "shop/mens.html", context)


# -----------------------------------------------------------------------------
# Contact View
# -----------------------------------------------------------------------------
def contact_view(request):
    """
    Handles contact form submissions.

    This view processes the contact form submission. It validates the form
    data, saves the inquiry to the database, sends a confirmation email, and
    redirects to a thank you page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered template for the contact page or a redirect to the thank
        you page.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save inquiry to the database
            Inquiry.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"],
            )
            # Send confirmation email
            send_mail(
                "Thank you for your inquiry",
                "We have received your inquiry and will get back to you soon.",
                settings.DEFAULT_FROM_EMAIL,
                [form.cleaned_data["email"]],
                fail_silently=False,
            )
            return redirect("contact_thanks")
    else:
        form = ContactForm()

    faqs = [
        {
            "question": "What is your return policy?",
            "answer": "You can return any item within 30 days.",
        },
        {
            "question": "Do you ship internationally?",
            "answer": "Yes, we ship to most countries worldwide.",
        },
        {
            "question": "How can I track my order?",
            "answer": "You will receive a tracking link via email once your order is shipped.",
        },
        # Add more FAQs as needed
    ]

    return render(request, "shop/contact.html", {"form": form, "faqs": faqs})


def contact_thanks_view(request):
    return render(request, "shop/contact_thanks.html")


# -----------------------------------------------------------------------------
# search_products
# -----------------------------------------------------------------------------
def search_products(request):
    """
    View function to perform product search based on query string.

    Retrieves products whose names contain the query string (case insensitive)
    and returns JSON response with matching products' names, images, and prices.

    Parameters:
    - request: HttpRequest object containing query parameters.

    Returns:
    - JsonResponse: JSON response containing search results.
      Format: {"results": [{"name": "Product Name", "image": "image_url", "price": "Product Price"}, ...]}

    """
    if request.method == "GET":
        # Retrieve the query parameter 'query' from the request
        query = request.GET.get("query", "")

        if query:
            # Filter products whose names contain the query (case insensitive)
            products = Product.objects.filter(name__icontains=query)

            # Construct a list of dictionaries containing product details
            results = [
                {
                    "name": product.name,
                    "image": product.image.url,
                    "price": product.price,
                }
                for product in products
            ]

            # Return JSON response with search results
            return JsonResponse({"results": results})

        # If no query parameter provided or no matching products found, return empty results
        return JsonResponse({"results": []})
