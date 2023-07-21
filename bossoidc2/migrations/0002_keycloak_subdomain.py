from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bossoidc2', '0002_auto_20201110_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='keycloak',
            name='subdomain',
            field=models.CharField(default=b'', max_length=64),
        ),
    ]