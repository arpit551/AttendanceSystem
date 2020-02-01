# Generated by Django 3.0.2 on 2020-02-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0002_auto_20200201_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contact_number',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='centers',
            name='center_id',
            field=models.UUIDField(default='983d8', editable=False, primary_key=True, serialize=False),
        ),
    ]
