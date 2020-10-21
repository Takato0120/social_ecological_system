# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-16 07:16


import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20160202_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='log_type',
            field=models.CharField(choices=[('Experimenter', 'Experimenter'), ('Scheduled', 'Scheduled'), ('System', 'System')], default='System', max_length=64),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='authentication_code',
            field=models.CharField(default='vcweb.auth.code', max_length=32),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'Not active'), ('ACTIVE', 'Active, no round in progress'), ('ROUND_IN_PROGRESS', 'Round in progress'), ('COMPLETED', 'Completed'), ('PUBLISHED', 'Published')], default='INACTIVE', max_length=32),
        ),
        migrations.AlterField(
            model_name='experimentgroup',
            name='session_id',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='experimentmetadata',
            name='namespace',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator('^[\\w_-]*$')]),
        ),
        migrations.AlterField(
            model_name='experimentmetadata',
            name='parameters',
            field=models.ManyToManyField(blank=True, to='core.Parameter'),
        ),
        migrations.AlterField(
            model_name='groupcluster',
            name='session_id',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='display_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='scope',
            field=models.CharField(choices=[('round', 'Round configuration data applicable to all groups for a given round'), ('experiment', 'Experiment configuration data relevant to the entire experiment'), ('group', 'Group data for a given group in a given round'), ('group_cluster', 'Group cluster data for a given group cluster in a given round'), ('participant', 'Participant data for a given participant in a given round')], default='round', max_length=32),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='type',
            field=models.CharField(choices=[('int', 'Integer value'), ('string', 'String value'), ('foreignkey', 'Foreign key'), ('float', 'Floating-point number'), ('boolean', 'Boolean value (true/false)'), ('enum', 'Enumeration')], max_length=32),
        ),
        migrations.AlterField(
            model_name='participant',
            name='class_status',
            field=models.CharField(blank=True, choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior'), ('Graduate', 'Graduate'), ('Other', 'Other')], max_length=32),
        ),
        migrations.AlterField(
            model_name='participant',
            name='favorite_color',
            field=models.CharField(blank=True, choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('yellow', 'yellow'), ('black', 'black'), ('white', 'white'), ('pink', 'pink'), ('purple', 'purple'), ('other', 'other')], max_length=32),
        ),
        migrations.AlterField(
            model_name='participant',
            name='favorite_food',
            field=models.CharField(blank=True, choices=[('Fast food', 'Fast food'), ('Haute cuisine', 'Haute cuisine'), ('Asian', 'Asian'), ('Mexican', 'Mexican'), ('Other', 'Other')], max_length=32),
        ),
        migrations.AlterField(
            model_name='participant',
            name='favorite_movie_genre',
            field=models.CharField(blank=True, choices=[('Family', 'Family'), ('Action', 'Action'), ('Comedy', 'Comedy'), ('Science Fiction', 'Science Fiction'), ('Documentary', 'Documentary'), ('Cult', 'Cult'), ('Sport', 'Sport'), ('Musical', 'Musical'), ('Horror', 'Horror'), ('Foreign', 'Foreign'), ('Romance', 'Romance'), ('Independent', 'Independent'), ('Drama', 'Drama')], max_length=64),
        ),
        migrations.AlterField(
            model_name='participant',
            name='favorite_sport',
            field=models.CharField(blank=True, choices=[('Football', 'Football'), ('Baseball', 'Baseball'), ('Hockey', 'Hockey'), ('Basketball', 'Basketball'), ('Other', 'Other')], max_length=32),
        ),
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Prefer not to say')], max_length=1),
        ),
        migrations.AlterField(
            model_name='participantgrouprelationship',
            name='survey_completed',
            field=models.BooleanField(default=False, help_text='Flag signifying that a survey was completed, automatically reset to False at the end of every round.'),
        ),
        migrations.AlterField(
            model_name='roundconfiguration',
            name='round_type',
            field=models.CharField(choices=[('WELCOME', 'Initial welcome page'), ('GENERAL_INSTRUCTIONS', 'General introduction'), ('REGULAR', 'Regular experiment round'), ('CHAT', 'Communication round'), ('DEBRIEFING', 'Debriefing round summary'), ('INSTRUCTIONS', 'Instructions'), ('PRIVATE_PRACTICE', 'Private practice round'), ('PRACTICE', 'Group practice round'), ('QUIZ', 'Quiz round'), ('SURVEY', 'Survey round')], default='REGULAR', max_length=32),
        ),
        migrations.AlterField(
            model_name='roundconfiguration',
            name='session_id',
            field=models.CharField(blank=True, default='', help_text=" Session id to associate with this round data and the groups in this experiment, useful for longer\n    multi-session experiments where group membership may change.  We don't want to destroy the old groups as that\n    information is still needed to determine payments, etc. Instead we need to create a new set of\n    Group/ParticipantGroupRelationship models that can live in conjunction with the existing\n        Group/ParticipantGroupRelationship models. ", max_length=64),
        ),
    ]
