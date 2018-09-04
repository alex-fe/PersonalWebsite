from django.db import models

# cooking, coding, soldering, music, About, rand.


class Catagory(models.Model):
    """
    name: Name of the Catagory
    """
    name = models.CharField(max_length=50)
    detail = models.TextField(blank=True)

    def __str__(self):
        return self.name
