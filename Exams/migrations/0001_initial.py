# Generated by Django 2.2.4 on 2019-09-13 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя предмета')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_header', models.CharField(max_length=30, verbose_name='Заголовок экзамена')),
                ('exam_description', models.TextField(blank=True, null=True, verbose_name='Описание экзамена')),
                ('exam_date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('exam_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('exam_subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Exams.Subject', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Экзамен',
                'verbose_name_plural': 'Экзамены',
            },
        ),
    ]
