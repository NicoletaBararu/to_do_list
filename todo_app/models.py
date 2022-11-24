from django.db import models
from django.utils import timezone
from django.urls import reverse

#setting ToDoItem default due dates
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):  #returns URl for data item list
        return reverse("list", args=[self.id])
      
    def __str__(self):    #python representation of an obj:: easier to debug
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:   #set order for ToDoItem records
        ordering = ["due_date"]    



         

           
