# Generated by Django 4.0 on 2023-01-28 23:19

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('suppliers', '0001_initial'),
        ('species', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LossGainReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManualStockUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_code', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['reason__name', 'date'], unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('confirm_called_police', models.BooleanField(blank=True, null=True)),
                ('date_when_called', models.DateField(blank=True, null=True)),
                ('police_ref', models.CharField(blank=True, max_length=220, null=True)),
                ('incident_raport', models.TextField(blank=True, null=True)),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='manual_stock_update', to='stock.lossgainreason')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='manual_stock_update', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_code', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['species__name'], unique=True)),
                ('net_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_item', to='suppliers.purchaseinvoice')),
                ('manual_stock_update', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stock_item', to='stock.manualstockupdate')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stock_item', to='orders.customerorder')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_item', to='species.species')),
            ],
            options={
                'ordering': ['invoice__delivery_date'],
            },
        ),
    ]
