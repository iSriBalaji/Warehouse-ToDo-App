# Generated by Django 4.0 on 2022-01-15 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=200, null=True)),
                ('house_no', models.CharField(choices=[('48', '48 Callodine'), ('65', '65 Callodine')], default='48', max_length=7)),
                ('store', models.CharField(choices=[('INDSTORE', 'Indian Store'), ('TOPS', 'Tops'), ('WALMART', 'Walmart'), ('OTHERS', 'Others')], default='TOPS', max_length=25)),
                ('complete', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
            options={
                'ordering': ['complete', 'house_no'],
            },
        ),
    ]
