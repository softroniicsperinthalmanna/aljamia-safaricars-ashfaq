# Generated by Django 4.1.7 on 2023-02-27 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('safariapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Contact_info', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Address', to='safariapp.address')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safariapp.add_product')),
                ('Your_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Name', to='safariapp.address')),
                ('contact_number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Phone', to='safariapp.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
