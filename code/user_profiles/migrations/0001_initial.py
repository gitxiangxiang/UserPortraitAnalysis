# Generated by Django 3.0.3 on 2020-03-27 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.BigIntegerField(unique=True)),
                ('acceptor_no', models.IntegerField(null=True)),
                ('acceptor_name', models.CharField(max_length=255, null=True)),
                ('raise_name', models.CharField(default='匿名', max_length=255)),
                ('classification', models.TextField(default='[]')),
                ('urgent_level', models.IntegerField(choices=[(None, '(OTHERS)'), (0, 'EMERGENCY'), (1, 'COMMON'), (2, 'INSIGNIFICANT')], default=1)),
                ('raise_category', models.IntegerField(choices=[(None, '(OTHERS)'), (0, 'Consult'), (1, 'Seek Help'), (2, 'Complain')], default=0)),
                ('raise_channel', models.IntegerField(choices=[(None, '(OTHERS)'), (0, 'CALL')], default=0)),
                ('content', models.TextField(default='')),
                ('raise_time', models.DateTimeField(default='2020-1-1 00:00:00')),
                ('notes', models.TextField(default='')),
                ('status', models.IntegerField(choices=[(None, '(OTHERS)'), (0, 'Finish'), (1, 'Transfer'), (2, 'Apartment')], default=2)),
                ('receive_category', models.IntegerField(choices=[(None, '(OTHERS)'), (0, 'Direct Handle'), (1, 'Transfer Handle')], default=0)),
                ('is_secrecy', models.BooleanField(default=True)),
                ('is_reply', models.BooleanField(default=False)),
                ('handle_department', models.CharField(default='', max_length=255)),
                ('transfer_time', models.DateTimeField(default='2020-1-1 00:00:00')),
                ('transfer_name', models.CharField(default='', max_length=255)),
                ('transfer_no', models.IntegerField(null=True)),
                ('transfer_opinion', models.TextField(default='')),
                ('finish_time', models.DateTimeField(default='2020-1-1 00:00:00')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalAppeal',
            fields=[
                ('appeal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user_profiles.Appeal')),
            ],
            bases=('user_profiles.appeal',),
        ),
    ]
