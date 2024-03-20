# Generated by Django 4.1.7 on 2024-03-20 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='coverletter',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='application',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='job.job'),
        ),
    ]
