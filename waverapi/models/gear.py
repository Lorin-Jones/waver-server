from django.db import models

class Gear(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    specifications = models.ForeignKey('Specification', on_delete=models.CASCADE)

    @property
    def reviews(self):
        return self.reviews

    @property
    def average_rating(self):
        avg = 0
        all_ratings = self.reviews.all()
        for rating in all_ratings:
            avg = avg + rating.rating

        try:
            avg = avg / len(all_ratings)
        except ZeroDivisionError:
            pass
        return avg