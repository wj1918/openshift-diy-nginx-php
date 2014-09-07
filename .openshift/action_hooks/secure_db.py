#!/usr/bin/env python
import os
import sys
import django
from django.contrib.auth.models import User

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'mysite'))

django.setup()

u = User.objects.get(username__exact='admin')
new_pass="password"
u.set_password(new_pass)
u.save()
# Print the new password info
#print "Django application credentials:\n\tuser: admin\n\t" + new_pass