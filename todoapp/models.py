from django.db import models



# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    due = models.DateField(blank=True,null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        if len(self.title) > 0:
            return self.title
        else:
            if len(self.content)>30 :
                return str(self.content[:30]) + "..." 
            else:
                return str(self.content[:30])