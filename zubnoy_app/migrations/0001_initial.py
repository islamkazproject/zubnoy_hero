# Generated by Django 4.1.3 on 2023-05-27 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('doctor', 'Врач'), ('admin', 'Администратор'), ('registrar', 'Регистратор'), ('client', 'Клиент'), ('guest', 'Гость')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('user_password', models.CharField(max_length=50)),
                ('groups', models.ManyToManyField(related_name='zubnoy_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='zubnoy_users', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='zubnoy_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='zubnoy_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrarProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='zubnoy_app.user')),
            ],
        ),
    ]