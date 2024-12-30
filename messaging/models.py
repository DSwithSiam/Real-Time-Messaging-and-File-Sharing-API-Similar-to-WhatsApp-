from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now, timedelta

class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete= models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True,  related_name='receiver_messages')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='group_messages')
    message = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    file_expiry = models.DateTimeField(default= now() + timedelta(days=10))

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver or self.group}"
    
    


