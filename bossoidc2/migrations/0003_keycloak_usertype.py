from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bossoidc2', '0002_keycloak_subdomain'),
    ]

    operations = [
        migrations.AddField(
            model_name='keycloak',
            name='user_type',
            field=models.CharField(default=b'', max_length=64),
        ),
    ]