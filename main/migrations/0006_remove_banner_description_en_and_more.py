# Generated by Django 4.0.3 on 2022-08-02 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_subcategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='product',
            name='options_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='options_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='options_uz',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='name_uz',
        ),
    ]
