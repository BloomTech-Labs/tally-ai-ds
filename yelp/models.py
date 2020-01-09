# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid


class YelpBusiness(models.Model):
    business_id = models.CharField(primary_key=True, max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    stars = models.FloatField(blank=True, null=True)
    review_count = models.IntegerField(blank=True, null=True)
    is_closed = models.BooleanField(blank=True, null=True)
    is_claimed = models.BooleanField(blank=True, null=True)
    display_phone = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    data_source = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.business_id)
        
    class Meta:
        managed = False
        db_table = 'business'


class YelpReview(models.Model):
    uuid = models.UUIDField(primary_key=True)
    review_id = models.CharField(max_length=100, blank=True, null=True)
    business_id = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    stars = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    text = models.CharField(max_length=5000, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    data_source = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.uuid)

    class Meta:
        managed = False
        db_table = 'review'


class YelpYelpScraping(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review_id = models.CharField(max_length=100, blank=True, null=True)
    business_id = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    stars = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    text = models.CharField(max_length=5000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.uuid)

    class Meta:
        managed = False
        db_table = 'yelp_scraping'