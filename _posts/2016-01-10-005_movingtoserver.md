---
published: false
layout: post
title: Moving To Server
---

I tried copying the scripts I used for my TDD project over here. For the most part, they look alright. But then I encountered an odd hitch around the fabric dependency. 

To make things easy for a developer, I decided to add fabric to my requirements.txt. Strictly speaking, this is only needed for my local system and not on the server. Still, I was not in a mood to maintain 2 different requirements, so decided to use the same one anyway. This .. caused an issue with creating the virutalenv on the server. Something about a 'python.h' missing. Stackoverflow tells me that the python development libraries are not installed on my server. I've updated my provisioning_notes in the repo to reflect this and have just logged into the server to run this;

> apt-get install python-dev

A message came up about a package not being authenticated (libpython-dev python-dev). For now, I'm going to let this be. Might have to investigate it at a later date, though. 

Running the fabric script now, tells me that the virtualenv has been created successfully and that there are no issues. Now I need to log into the box and activate nginx & gunicorn configs for the site.

Hmm.. almost got it. There was an error with activating the gunicorn service, but it looks like I didn't have it inside my virutalenv. Adding it in and going to commit it. 

And now I'm getting 502 gateway errors from nginx. This took a bit of debugging. Running over the nginx logs .. etc. It turns out, my gunicorn process hadn't started properly. when I copied over my deployment scripts, I forget to reset the wsgi application path. After correcting it, the server is now up and running. :)

[http://journal.abraham-v.com/]()


