from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bossoidc2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keycloak',
            name='subdomain',
            field=models.CharField(default=b'', max_length=64),
        ),
    ]