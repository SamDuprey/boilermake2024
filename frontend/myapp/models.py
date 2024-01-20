from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    week_number = models.CharField(max_length=2, blank=True)
    end_date = models.DateField()

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]

        super().save(*args, **kwargs)


class MyForm(forms.Form):
    dropdown_choices = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    dropdown_field = forms.ChoiceField(choices=dropdown_choices)
    