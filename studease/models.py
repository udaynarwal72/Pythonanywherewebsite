from django.db import models
# from models import branchDetails

# Create your models here.
# we can understand this as we created a xcel sheet named contact
class contact(models.Model):
    name = models.CharField(max_length=122,default='')
    email = models.CharField(max_length=122,default='')
    # date = models.DateField()

    def __str__(self):
        return self.name
    
class SubSection(models.Model):
    sub_section_name = models.CharField(max_length=100,default='')

class RollNumber(models.Model):
    sub_section = models.ForeignKey(SubSection, on_delete=models.CASCADE)
    roll_number = models.IntegerField(max_length=100)
    username = models.CharField(max_length=100,default='')
    token = models.CharField(max_length=256, default="")


class TimeTable(models.Model):
    sub_section = models.ForeignKey(SubSection, on_delete=models.CASCADE, default=None, null=True)
    period = models.CharField(max_length=100, default='')
    monday = models.CharField(max_length=100, default='')
    tuesday = models.CharField(max_length=100, default='')
    wednesday = models.CharField(max_length=100, default='')
    thursday = models.CharField(max_length=100, default='')
    friday = models.CharField(max_length=100, default='')
    time = models.TimeField(default="00:00:00", null=True) # type: ignore
    newtime = models.TimeField(default="00:00:00", null=True) # type: ignore


class userfeedbacktable(models.Model):
    feedbackfirstname=models.CharField(max_length=100)
    feedbacklastname=models.CharField(max_length=100)
    feedbackemail= models.CharField(max_length=100)
    feedbackmessage=models.CharField(max_length=100)
    def __str__(self):
        return self.feedbackemail

class vacantvenue(models.Model):
    day = models.CharField(max_length=100)
    room=models.CharField(max_length=100)
    p1 = models.IntegerField(max_length=100)
    p2 = models.IntegerField(max_length=100)
    p3 = models.IntegerField(max_length=100)
    p4 = models.IntegerField(max_length=100)
    p5 = models.IntegerField(max_length=100)
    p6 = models.IntegerField(max_length=100)
    p7 = models.IntegerField(max_length=100)
    p8 = models.IntegerField(max_length=100)
    p9 = models.IntegerField(max_length=100)
    p10 = models.IntegerField(max_length=100)

class subject(models.Model):
    sub_section = models.ForeignKey(SubSection, on_delete=models.CASCADE, default=None, null=True)
    user_subject = models.CharField(max_length=100,default='')

class userAttendance(models.Model):
    user_rollnumber = models.IntegerField(max_length=100,default=0)
    user_subject=models.CharField(max_length=100,default='')
    user_actions = models.CharField(max_length=10,default='noclass')
    date = models.DateField()