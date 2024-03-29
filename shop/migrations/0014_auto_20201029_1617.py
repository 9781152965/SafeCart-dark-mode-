# Generated by Django 3.1.2 on 2020-10-29 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0013_auto_20200930_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=1, max_length=50)),
                ('slug', models.SlugField(default=1, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.CharField(default=0, max_length=5000000),
        ),
        migrations.CreateModel(
            name='Order2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_by', models.CharField(max_length=200)),
                ('shipping_address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subtotal', models.PositiveIntegerField(default=1)),
                ('discount', models.PositiveIntegerField(default=1)),
                ('total', models.PositiveIntegerField(default=1)),
                ('order_status', models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('On the way', 'On the way'), ('Order Completed', 'Order Completed'), ('Order Cancelled', 'Order Cancelled')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
            ],
        ),
        migrations.CreateModel(
            name='item2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=1, max_length=500)),
                ('slug', models.SlugField(default=1, unique=True)),
                ('warranty', models.CharField(blank=True, max_length=300, null=True)),
                ('return_policy', models.CharField(blank=True, max_length=300, null=True)),
                ('marked_price', models.PositiveIntegerField(default=1)),
                ('selling_price', models.PositiveIntegerField(default=1)),
                ('descripton', models.TextField(default=1)),
                ('i_image', models.ImageField(default='', upload_to='shop2/images2')),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('subtotal', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item2')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.customer'),
        ),
    ]
