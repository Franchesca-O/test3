from __future__ import unicode_literals

from django.db import models

from ..users.models import User 
import datetime
import re


class CiteManager(models.Manager):

    def citation(self, postData, user_id):
        errors = []
        if len(postData['author']) < 3:
            errors.append("'Quoted by:' should have more than 3 characters") 

        if len(postData['quote']) < 11:
            errors.append("'Quote' should have more than 10 characters") 
        
        print len(errors)

        if len (errors) > 0:
            return (False, errors)
        else:
            newposter = User.objects.get(id=user_id)
            newquote = Cite.objects.create(
            author = postData ['author'],
            quote = postData['quote'],
            poster = newposter
        )
        newquote.shared_with.add(newposter)
        newquote.save()

        return (True, "success")

    def join(self, user_id, quote_id):
        person = User.objects.get(id=user_id)
        instance = Cite.objects.get(id=quote_id)
        instance.shared_with.add(person)
        instance.save()

    def leave(self, user_id, quote_id):
        person = User.objects.get(id=user_id)
        instance= Cite.objects.get(id=quote_id)
        instance.shared_with.remove(person)
        instance.save()



class Cite(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length = 50)
    poster = models.ForeignKey(User, related_name = 'post_person')
    shared_with = models.ManyToManyField(User, related_name='shared')
    objects = CiteManager()