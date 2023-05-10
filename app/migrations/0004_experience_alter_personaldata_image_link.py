# Generated by Django 4.2.1 on 2023-05-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_personaldata_image_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('role', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('links', models.URLField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=False, verbose_name='Working Currently')),
            ],
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='image_link',
            field=models.URLField(default='', help_text='Use 1:1 image for better results', verbose_name='Image Link'),
        ),
    ]
