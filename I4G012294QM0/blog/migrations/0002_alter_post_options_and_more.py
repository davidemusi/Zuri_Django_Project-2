# Generated by Django 4.0.5 on 2022-06-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='post',
            name='Published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]