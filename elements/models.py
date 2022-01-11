from django.db import models


class Element(models.Model):
    content = models.BigIntegerField(null=False)
    order = models.IntegerField(unique=True)

    class Meta:
        verbose_name = 'Element'
        verbose_name_plural = 'Elements'

    def __str__(self):
        return (f"| {self.content} |")
