# Generated by Django 4.0.3 on 2022-03-18 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_job_position_name'),
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.CreateModel(
            name='CandidateJobMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('accepted', 'accepted'), ('pending', 'pending'), ('rejected', 'rejected')], default='pending', max_length=50)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
    ]
