# Generated by Django 4.1.2 on 2022-10-10 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aulas', to='teacher.teacher')),
            ],
        ),
    ]
