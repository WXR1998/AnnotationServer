from django.db import models

class Record(models.Model):
    filename = models.CharField(max_length=128)
    status = models.IntegerField(default=0, db_index=True)
    class_label = models.IntegerField(default=0, db_index=True)
    img_id = models.IntegerField(default=-1)