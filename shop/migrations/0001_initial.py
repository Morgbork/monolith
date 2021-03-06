# Generated by Django 2.2.6 on 2019-10-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.SlugField(max_length=150)),
                ('manufacturer', models.SlugField()),
                ('stock', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Goods',
                'ordering': ['product_code'],
            },
        ),
    ]
