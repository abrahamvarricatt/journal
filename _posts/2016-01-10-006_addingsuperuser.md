---
published: false
layout: post
title: Adding a SuperUser
---

Now that the site is up and running, its time to figure out how to add a superuser account to access the admin page. On the good side, the admin login page itself is accessible over the internet. 

Hmm.. 

A quick search shows me that there are a few ways to add in a superuser account from commandline without interaction,

http://stackoverflow.com/a/28064218/198660
http://source.mihelac.org/2009/10/23/django-avoiding-typing-password-for-superuser/

Here's the line,
> echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | ./manage.py shell

Problem is, I can't run that twice on the same database. It gives me an error about user already present. Hey, that *might* work out! I'm not particularily interested in migrations for this project right now, so it should be alright to just delete the sqlite database and recreate it during each deploy. Let me check the script again.

Yes, I've scripted it like that. Delete database, migrate, then add user via shell. (ref: http://superuser.com/a/887349/147726 , for deleting if file not present )

Caveat: I'm hard-coding the superuser credentials into my fabfile which I'm going to upload to github. Not really something I would do on a production system - need to use another way to pass in those values. But should do for this deployment. 

