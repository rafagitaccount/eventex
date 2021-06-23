# Generated by Django 3.2.4 on 2021-06-22 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210622_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('talk_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.talk')),
                ('slots', models.IntegerField()),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
            },
            bases=('core.talk',),
        ),
    ]