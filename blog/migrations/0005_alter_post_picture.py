# Generated by Django 3.2.23 on 2023-12-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='uploads/default.jpg', upload_to='uploads/'),
        ),
    ]