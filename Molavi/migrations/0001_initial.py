# Generated by Django 3.0.5 on 2020-04-04 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='zamimeh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='raftar_mosbat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='raftar_manfi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='nezame_tabieye_donya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='masnavi_manavi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='jameh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='jahl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='ghodrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='elm_o_andisheh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Molavi.categories')),
            ],
        ),
    ]
