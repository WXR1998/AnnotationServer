# Generated by Django 3.1.7 on 2021-03-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnnotationServer', '0004_record_img_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='class_label',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='record',
            name='status',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
