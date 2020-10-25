# Generated by Django 3.0.7 on 2020-10-25 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('caixa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='valesfuncionarios',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sangria',
            name='cd_Caixa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='caixa.Caixa'),
        ),
        migrations.AddField(
            model_name='sangria',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entrada',
            name='cd_Caixa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='caixa.Caixa'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='despesacaixa',
            name='cd_Caixa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='caixa.Caixa'),
        ),
        migrations.AddField(
            model_name='despesacaixa',
            name='cd_DespesaTipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='caixa.DespesaTipo'),
        ),
        migrations.AddField(
            model_name='controlecaixa',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='caixa',
            name='cd_ControleCaixa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='caixa.ControleCaixa'),
        ),
    ]
