# Generated by Django 2.2.1 on 2019-05-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='org_type',
            field=models.CharField(choices=[(1, '培训机构'), (2, '高校'), (3, '个人')], default=1, max_length=10, verbose_name='机构类别'),
        ),
    ]
