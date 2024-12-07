# Generated by Django 5.1.3 on 2024-12-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radicalConnect', '0006_remove_user_groups_remove_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futureskill',
            name='selected_skills',
            field=models.CharField(choices=[('AI', 'Artificial Intelligence'), ('BD', 'Big Data'), ('BA', 'Business Applications'), ('CP', 'Compliance-POSH'), ('DA', 'Data Analytics'), ('DO', 'DevOps'), ('IoT', 'Internet of Things (IoT)'), ('PBI', 'Power BI'), ('PR', 'Productivity'), ('AZ', 'Azure'), ('BC', 'Blockchain'), ('CC', 'Cloud Computing'), ('CS', 'Cybersecurity'), ('DS', 'Data Science'), ('HS', 'Human Skills'), ('MW', 'Modern Workplace'), ('PP', 'Power Platform')], default='AI', max_length=40),
        ),
    ]
