from django.db import models

class Entry(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300, unique=True)
    body = models.TextField()

    def __unicode__(self):
        return '%s : %s' % (self.title, self.pub_date)

class Comment(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(auto_now=True)
    entry = models.ForeignKey(Entry)
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=500)

    def __unicode__(self):
        return '%s : %s' % (self.username, self.pub_date)
