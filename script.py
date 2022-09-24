import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_book.settings')
django.setup()

from core.models import *

# test2 = User(username='chester2')
# test2.save()

# test2 = Profile(test1.id_user='someiduser')
# test2.save()
