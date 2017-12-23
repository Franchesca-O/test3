from __future__ import unicode_literals
from django.db import models
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt
import datetime
import re


hash1 = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())


class UserManager(models.Manager):
    
    def validate(self, postData):
        errors = {}
        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')
        hash1 = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        print hash1
    
        if len(postData['name']) < 3 or len(postData['username']) < 3:
            errors['name_errors'] = "Name and username should be at least 3 characters"

        if not re.match(NAME_REGEX, postData['name']): 
            errors["name"] = "Name takes only characters"

        if not re.match(NAME_REGEX, postData['username']):
            errors["username"] = "Username takes only characters"
        
        if len(postData['password']) < 8:
            errors['password']="Password needs to have 8 characters or more. "
        
        if postData['password'] != postData['confirm_password']:
            errors["password"] = "Password and confirm password must match"
            
        print len(errors)

        if len(errors) > 0:
            return (False, errors)
        else:
            hash1 = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt(5))
            user = User.objects.create(
                name = postData ['name'],
                username = postData ['username'],
                email = postData ['email'],
                date_of_birth = postData ['dob'],
                password = hash1
            )
            return (True, user)

    def login(self, postData):
        errors = {}

        if len(self.filter(username=postData['username'])) > 0:
            user = self.filter(username=postData['username'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors ['password'] = "password"
                return False
            else:
                return (True, user)
        else:
            errors ['username'] = "Wrong username"
            return False
    

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    objects = UserManager()


