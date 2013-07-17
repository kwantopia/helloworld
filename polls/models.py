from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models. CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)