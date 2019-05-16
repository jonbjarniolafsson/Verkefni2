# Generated by Django 2.2.1 on 2019-05-16 15:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('size', models.IntegerField(max_length=50)),
                ('rooms', models.IntegerField(max_length=50)),
                ('bathrooms', models.IntegerField(max_length=50)),
                ('type', models.CharField(default='Apartment', max_length=50)),
                ('aptsuite', models.CharField(blank=True, max_length=30, null=True)),
                ('timeofconstruction', models.CharField(default=2000, max_length=50)),
                ('displayimage', models.CharField(max_length=5000)),
                ('forsale', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=5000)),
                ('backgroundPhoto', models.CharField(max_length=5000)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('officeHours', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(max_length=200)),
                ('description', models.TextField()),
                ('registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('soldondate', models.DateTimeField(blank=True, default=None, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
                ('apartmentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.Apartments')),
            ],
        ),
        migrations.CreateModel(
            name='PriceLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salescost', models.CharField(max_length=20)),
                ('appraisalcost', models.CharField(max_length=15)),
                ('photocost', models.CharField(max_length=15)),
                ('managementcost', models.CharField(max_length=15)),
                ('datacollection', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ViewHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartmentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.Apartments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=4000)),
                ('date', models.DateField()),
                ('isseller', models.BooleanField()),
                ('listingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.Listings')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.CharField(max_length=30)),
                ('cardholder', models.CharField(max_length=80)),
                ('expmonth', models.CharField(max_length=50)),
                ('expyear', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('aptsuite', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('zip', models.CharField(max_length=80)),
                ('ssn', models.CharField(max_length=40)),
                ('isreviewed', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
        ),
        migrations.CreateModel(
            name='OpenHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openhousestart', models.DateTimeField(default=None, max_length=75)),
                ('openhouseend', models.DateTimeField(default=None, max_length=75)),
                ('listingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.Listings')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=15)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.Country')),
            ],
        ),
        migrations.CreateModel(
            name='ListingMiscs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footpreschool', models.CharField(blank=True, max_length=5, null=True)),
                ('carpreschool', models.CharField(blank=True, max_length=5, null=True)),
                ('footbusstop', models.CharField(blank=True, max_length=5, null=True)),
                ('carbusstop', models.CharField(blank=True, max_length=5, null=True)),
                ('carsupermarket', models.CharField(blank=True, max_length=5, null=True)),
                ('footsupermarket', models.CharField(blank=True, max_length=5, null=True)),
                ('footmetro', models.CharField(blank=True, max_length=5, null=True)),
                ('carmetro', models.CharField(blank=True, max_length=5, null=True)),
                ('listingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.Listings')),
            ],
        ),
        migrations.CreateModel(
            name='ListingDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.CharField(default=None, max_length=500)),
                ('description', models.CharField(default=None, max_length=500)),
                ('listingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.Listings')),
            ],
        ),
        migrations.AddField(
            model_name='apartments',
            name='locationid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.Locations'),
        ),
        migrations.AddField(
            model_name='apartments',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
        migrations.CreateModel(
            name='ApartmentImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=5000)),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.Apartments')),
            ],
        ),
    ]
