# Generated by Django 2.1.3 on 2018-12-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted time')),
                ('is_deleted', models.BooleanField(default=False)),
                ('level_name', models.CharField(max_length=255, verbose_name='Level')),
                ('asctime', models.DateTimeField(verbose_name='Time')),
                ('pathname', models.CharField(max_length=255, verbose_name='File Path')),
                ('funcname', models.CharField(max_length=255, verbose_name='Function Name')),
                ('lineno', models.IntegerField(default=0, verbose_name='line Number')),
                ('message', models.TextField(verbose_name='Message')),
                ('traceback', models.TextField(verbose_name='Traceback')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
