
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='연구책임기관')),
                ('department', models.CharField(max_length=127, verbose_name='진료과')),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=31, primary_key=True, serialize=False, verbose_name='과제번호')),
                ('title', models.CharField(max_length=255, verbose_name='과제명')),
                ('period', models.CharField(blank=True, default='', max_length=20, verbose_name='연구기간')),
                ('stage', models.CharField(blank=True, default='', max_length=31, verbose_name='임상시험단계')),
                ('total_target', models.PositiveIntegerField(blank=True, default=0, verbose_name='전체목표연구대상자수')),
                ('scope', models.CharField(choices=[('국내다기관', '국내다기관'), ('단일기관', '단일기관')], max_length=20, verbose_name='연구범위')),
                ('category', models.CharField(choices=[('관찰연구', '관찰연구'), ('중재연구', '중재연구'), ('기타', '기타')], max_length=20, verbose_name='연구종류')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studies.institute')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
