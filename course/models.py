from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Topics(models.Model):
    topicName = models.CharField(max_length=255)
    link = models.CharField(max_length=2083)
    courses = models.ForeignKey(Courses, on_delete=models.PROTECT)

    def __str__(self):
        return self.topicName

