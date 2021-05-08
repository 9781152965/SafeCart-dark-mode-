from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

CATEGORY_CHOICES=(
    ("M", "Mobile"),
    ("L", "Laptop"),
    ("TW", "Top Wear"),
    ("BW", "Bottom Wear"),
)
class Product(models.Model):
    GST_CHOICES = (("0",'0'),("3",'3'),("5",'5'),("12",'12'),("18",'18'),("28",'28'))

    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField( choices=CATEGORY_CHOICES, max_length=2 )
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    marked_price = models.PositiveIntegerField( default = "0")
    selling_price = models.PositiveIntegerField( default = "0")
    desc = models.CharField(max_length=300, default="its is good for daily use")
    pub_date = models.DateField()
    gst = models.CharField(default='0',max_length=3,choices=GST_CHOICES)
    image = models.ImageField(upload_to='shop/images', default="")
    image1 = models.ImageField(upload_to='shop/images', default="", null=True)
    image2 = models.ImageField(upload_to='shop/images', default="", null=True, blank=True)
    image3 = models.ImageField(upload_to='shop/images', default="", null=True, blank=True)
    image4 = models.ImageField(upload_to='shop/images', default="", null=True, blank=True)
    image5 = models.ImageField(upload_to='shop/images', default="", null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img1 = Image.open(self.image1.path)
        if img1.height > 1500 or img1.width > 1500:
            output_size = (1500, 1500)
            img1.thumbnail(output_size)
            img1.save(self.image1.path)
        if self.image2:
            img2 = Image.open(self.image2.path)
            if img2.height > 1500 or img2.width > 1500:
                output_size = (1500, 1500)
                img2.thumbnail(output_size)
                img2.save(self.image2.path)

        if self.image3:
            img3 = Image.open(self.image3.path)
            if img3.height > 1500 or img3.width > 1500:
                output_size = (1500, 1500)
                img3.thumbnail(output_size)
                img3.save(self.image3.path)

        if self.image4:
            img4 = Image.open(self.image4.path)
            if img4.height > 1500 or img4.width > 1500:
                output_size = (1500, 1500)
                img4.thumbnail(output_size)
                img4.save(self.image4.path)

        if self.image5:
            img5 = Image.open(self.image5.path)
            if img5.height > 1500 or img5.width > 1500:
                output_size = (1500, 1500)
                img5.thumbnail(output_size)
                img5.save(self.image5.path)

    def __str__(self):
        return f'{self.product_id}'



    def __str__(self):
        return self.product_name


class Category(models.Model):
    title = models.CharField(max_length=50 , default="" )
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return self.title
CATEGORY_CHOICES=(
    ("M", "Mobile"),
    ("L", "Laptop"),
    ("TW", "Top Wear"),
    ("BW", "Bottom Wear"),
)
class Product2(models.Model):
  
    image = models.ImageField(upload_to='shop2/images2', default="")
    title = models.CharField(max_length=500 , default="")
    slug = models.SlugField(unique=True, default="")
    brand = models.CharField(max_length=100, default="")
    category = models.CharField( choices=CATEGORY_CHOICES, max_length=2 )
    warranty = models.CharField(max_length=300, null=True, blank=True)
    return_policy = models.CharField(max_length=300, null=True, blank=True)
    marked_price = models.PositiveIntegerField( default = "0")
    selling_price = models.PositiveIntegerField( default = "0")
    descripton = models.TextField(default=" this product is best in all aspects in term of price ")
    
    view_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product2, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField( default ="")
    subtotal = models.PositiveIntegerField(default = "")
   
    def __str__(self):
        return "Cart: " + str(self.cart.id) + "CartProduct: " + str(self.id)

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"), 
    ("Order Cancelled", "Order Cancelled"),
)

class Order2(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField( default = "")
    discount = models.PositiveIntegerField( default="")
    total = models.PositiveIntegerField(default="")
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Order2: " + str(self.id)



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    amount = models.CharField(max_length=5000000,default=0)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc


