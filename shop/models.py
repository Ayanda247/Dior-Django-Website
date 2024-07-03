from django.db import models
from django.utils.text import slugify


# -----------------------------------------------------------------------------
# Order Model
# -----------------------------------------------------------------------------
class Order(models.Model):
    """
    Represents a customer order.

    This model stores information about a customer's order, including their
    personal details, shipping address, order date, and payment status.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        """
        Returns a string representation of the order.

        Returns:
            str: The string representation of the order (e.g., "Order 123").
        """
        return f"Order {self.id}"


# -----------------------------------------------------------------------------
# Category Model
# -----------------------------------------------------------------------------
class Category(models.Model):
    """
    Represents a product category.

    This model stores the name and slug of a product category.
    """

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        """
        Returns a string representation of the category.

        Returns:
            str: The name of the category.
        """
        return self.name


# -----------------------------------------------------------------------------
# Product Model
# -----------------------------------------------------------------------------
class Product(models.Model):
    """
    Represents a product.

    This model stores information about a product, including its name,
    category, description, price, image, rating, slug, and availability.
    """

    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    slug = models.SlugField(max_length=255, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: The name of the product.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Saves the product instance.

        This method automatically generates a slug from the product name if
        one doesn't exist.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


# -----------------------------------------------------------------------------
# Order Item Model
# -----------------------------------------------------------------------------
class OrderItem(models.Model):
    """
    Represents an item in an order.

    This model stores information about a specific product included in an
    order, including its price and quantity.
    """

    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        """
        Returns a string representation of the order item.

        Returns:
            str: The ID of the order item.
        """
        return str(self.id)

    def get_cost(self):
        """
        Calculates the total cost of the order item.

        Returns:
            decimal.Decimal: The total cost of the order item (price * quantity).
        """
        return self.price * self.quantity


# -----------------------------------------------------------------------------
# Inquiry Model
# -----------------------------------------------------------------------------
class Inquiry(models.Model):
    """
    Represents a customer inquiry.

    This model stores information about a customer's inquiry, including their
    name, email address, and message.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the inquiry.

        Returns:
            str: A formatted string representing the inquiry.
        """
        return f"Inquiry from {self.name}"

