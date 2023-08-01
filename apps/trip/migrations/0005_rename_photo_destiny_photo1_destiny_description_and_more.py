# Generated by Django 4.2.3 on 2023-08-01 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0004_alter_statement_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destiny',
            old_name='photo',
            new_name='photo1',
        ),
        migrations.AddField(
            model_name='destiny',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='destiny',
            name='goal',
            field=models.CharField(default='', max_length=160),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destiny',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='destiny_photos'),
        ),
    ]