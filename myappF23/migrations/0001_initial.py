# Generated by Django 4.2.6 on 2023-10-18 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('level', models.CharField(choices=[('BE', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced')], max_length=10)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappF23.category')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('date_of_birth', models.DateField()),
                ('status', models.CharField(choices=[('ER', 'Enrolled'), ('SP', 'Suspended'), ('GD', 'Graduated')], default='ER', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('courses_taught', models.ManyToManyField(blank=True, related_name='instructors', to='myappF23.course')),
                ('students_taught', models.ManyToManyField(blank=True, to='myappF23.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myappF23.instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, to='myappF23.student'),
        ),
    ]
