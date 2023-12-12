from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
  def handle(self, *args, **options):
    if not User.objects.filter(email="email@example.com").exists():
      User.objects.create_superuser(
          # username=settings.SUPERUSER_NAME,
          email="email@example.com",
          password="1password"
      )
      print("スーパーユーザー作成")