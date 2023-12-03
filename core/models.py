from django.db import models
from django.core.validators import MinValueValidator

class Competition(models.Model):
    competition_name = models.CharField(max_length=255)

    def __str__(self):
        return self.competition_name

class Role(models.Model):
    name_of_role = models.CharField(max_length=255)
    min_member = models.IntegerField(validators=[MinValueValidator(0)])
    max_member = models.IntegerField(validators=[MinValueValidator(1)])
    competitions = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_role

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)


    def __str__(self):
        return self.team_name

class Member_Detail(models.Model):
    GENDER_CHOICES = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('o', 'Others')
    )

    name = models.CharField(max_length=255)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField(validators=[MinValueValidator(limit_value=10)])
    your_city = models.CharField(max_length=1000000000)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Postal_code = models.IntegerField(null=True,blank=True)
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        return self.name
