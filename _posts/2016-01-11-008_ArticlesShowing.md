---
published: true
layout: post
title: Articles Showing
---


This took longer than I planned, but the article list page and articles view is now up and comitted. Hmm.. better do a deploy, just to be sure on things. 

and it works! :)

At this point, things were rather straight-forward. Make a model with fields for articles. Make a view to show individual articles based on their id number (the primary key in the db, I think?) and a list view to show different articles. 

But darn, I'm getting rather sleepy right now. Spent too much time debugging an issue, which turned out to be a typo, where I forgot to use the 'return' keyword in a function. 

I put in a blank view, so that if nothing is stored on the DB, an error message shows up.
