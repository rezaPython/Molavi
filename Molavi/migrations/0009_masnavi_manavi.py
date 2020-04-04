# Generated by Django 3.0.5 on 2020-04-04 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Molavi', '0008_nezame_tabieye_donya'),
    ]

    operations = [
        migrations.CreateModel(
            name='masnavi_manavi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
    ]