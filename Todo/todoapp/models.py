from django.db import models

# Create your models here.
class todo(models.Model):
    name=models.CharField(max_length=250)
    priority = models.PositiveSmallIntegerField(unique=True)

    def save(self, *args, **kwargs):
        if not self.priority:
            last_task = todo.objects.order_by('-number').first()
            if last_task:
                self.priority = last_task.priority + 1
            else:
                self.priority = 1
        super().save(*args, **kwargs)

    date = models.DateField()





    class Meta:
        ordering=['priority']


    def __str__(self):
        return self.name