import uuid

from django.db import models
from django.urls import reverse


class Services(models.Model):
    """Model representing a service offered on Sidehustles."""

    # A character field for the service name.
    service_name = models.CharField(max_length=200, default = "Tupac's 3-Pack Sodas")
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, blank=True, null=True, related_name='service_provider')
    # A integer field for the service cost.
    service_cost = models.IntegerField()

    # A character field for the service category.
    service_category = models.CharField(max_length=200, default = "J Cole")

    # A character field to indicate the service's location.
    service_location = models.CharField(max_length=200, default = "Grandmaster Flash")

    # A integer field to indicate proficieny (scale to be determined)
    service_proficiency = models.IntegerField()

    skill_info = models.CharField(max_length=1000, help_text="Tell us more about your skill!", default="I am very skilled!")
    SKILL_TYPE = [("Computers", "Computers"), ("Music", "Music"), ("Art", "Art"), ("Sports", "Sports"), ("Manual Labor", "Manual Labor"),
                  ("Tutoring", "Tutoring")]
    skill = models.CharField(max_length=50, choices=SKILL_TYPE, default='Computers')
    LOCATION_TYPE = [("UMass Amherst", "UMass Amherst"), ("5-College", "5-College"), ("Off Campus", "Off Campus")]
    location = models.CharField(max_length=50, choices=LOCATION_TYPE, default='1')
    AVAILABILITY_TYPE = [("M", "M"), ("T", "T"), ("W", "W"), ("Th", "Th"), ("F", "F"),
                  ("Sat", "Sat"), ("Sun", "Sun"), ("Unavailable", "Unavailable")]
    availability = models.CharField(max_length=9, choices=AVAILABILITY_TYPE, default='8')
    # id = models.UUIDField(primary_key = True, default=uuid.uuid4, unique=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.skill_info

    def get_absolute_url(self):
        return reverse("product", args=[str(self.id)])

class Reviews(models.Model):
    """Model representing a customer review."""
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, related_name='service')
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, blank=True, null=True, related_name='user')
    review_like_count = models.IntegerField(null=True)
    review_text = models.TextField(help_text = "Type a review")
    #editable review text not being generated with fake data
    editable_text = models.TextField(help_text = "Type a review")
    review_date_posted = models.DateField(null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.review_text
