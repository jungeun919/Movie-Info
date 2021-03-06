# Generated by Django 3.2.3 on 2021-08-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('grade', models.CharField(choices=[('0.5', '0.5'), ('1.0', '1.0'), ('1.5', '1.5'), ('2.0', '2.0'), ('2.5', '2.5'), ('3.0', '3.0'), ('3.5', '3.5'), ('4.0', '4.0'), ('4.5', '4.5'), ('5.0', '5.0')], max_length=10)),
                ('pub_date', models.DateField()),
                ('running_time', models.IntegerField(help_text='시간 단위 : 분')),
                ('category', models.CharField(max_length=12)),
                ('rank', models.CharField(choices=[('all', '전체 관람가'), ('12', '12세 이상 관람가'), ('15', '15세 이상 관람가'), ('19', '청소년 관람불가')], max_length=10)),
                ('image', models.FileField(blank=True, null=True, upload_to='main/')),
            ],
        ),
    ]
