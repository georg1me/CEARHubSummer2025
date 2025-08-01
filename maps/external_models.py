# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Communities(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.TextField()
    slug = models.TextField()
    cordslat = models.FloatField()
    cordslong = models.FloatField()
    streamid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'communities'


class Datastreams(models.Model):
    datastream_id = models.IntegerField(primary_key=True)
    thing = models.ForeignKey('Things', models.DO_NOTHING)
    sensor = models.ForeignKey('Sensors', models.DO_NOTHING)
    observed_property = models.ForeignKey('ObservedProperties', models.DO_NOTHING)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    observation_type = models.TextField(blank=True, null=True)
    unit_of_measurement_name = models.TextField(blank=True, null=True)
    unit_of_measurement_symbol = models.TextField(blank=True, null=True)
    unit_of_measurement_definition = models.TextField(blank=True, null=True)
    observed_area = models.JSONField(blank=True, null=True)
    phenomenon_time_start = models.TextField(blank=True, null=True)
    phenomenon_time_end = models.TextField(blank=True, null=True)
    result_time_start = models.TextField(blank=True, null=True)
    result_time_end = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datastreams'


class Events(models.Model):
    eid = models.AutoField(primary_key=True)
    cid = models.IntegerField()
    ename = models.TextField()
    edescription = models.TextField()
    eimg = models.TextField()
    edate = models.DateField()
    sensor_id = models.IntegerField(blank=True, null=True)
    data_type_id = models.IntegerField(blank=True, null=True)
    data_start_date = models.DateTimeField(blank=True, null=True)
    data_end_date = models.DateTimeField(blank=True, null=True)
    data_summary = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class FeaturesOfInterest(models.Model):
    feature_of_interest_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    encoding_type = models.TextField()
    feature = models.JSONField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'features_of_interest'


class HistoricalLocationLocations(models.Model):
    pk = models.CompositePrimaryKey('historical_location_id', 'location_id')
    historical_location = models.ForeignKey('HistoricalLocations', models.DO_NOTHING)
    location = models.ForeignKey('Locations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'historical_location_locations'
        unique_together = (('historical_location', 'location'),)


class HistoricalLocations(models.Model):
    historical_location_id = models.IntegerField(primary_key=True)
    thing = models.ForeignKey('Things', models.DO_NOTHING, blank=True, null=True)
    time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historical_locations'


class Locations(models.Model):
    location_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    location = models.JSONField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Observations(models.Model):
    observation_id = models.IntegerField(primary_key=True)
    datastream = models.ForeignKey(Datastreams, models.DO_NOTHING)
    phenomenon_time_start = models.TextField(blank=True, null=True)
    phenomenon_time_end = models.TextField(blank=True, null=True)
    result_time = models.TextField(blank=True, null=True)
    result = models.JSONField(blank=True, null=True)
    result_quality = models.JSONField(blank=True, null=True)
    valid_time_start = models.TextField(blank=True, null=True)
    valid_time_end = models.TextField(blank=True, null=True)
    parameters = models.JSONField(blank=True, null=True)
    feature_of_interest = models.ForeignKey(FeaturesOfInterest, models.DO_NOTHING)
    result_navd88 = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observations'


class ObservedProperties(models.Model):
    observed_property_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observed_properties'


class Reports(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reports'


class Sensors(models.Model):
    sensor_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensors'


class SotLocations(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    facing_direction = models.TextField()
    category = models.TextField()
    icon = models.TextField()
    photo_instructions = models.TextField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sot_locations'


class SotPhotoMetadata(models.Model):
    id = models.IntegerField(primary_key=True)
    photo_id = models.IntegerField()
    metadata_key = models.TextField()
    metadata_value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sot_photo_metadata'


class SotPhotos(models.Model):
    id = models.IntegerField(primary_key=True)
    location_id = models.IntegerField()
    user_ip = models.TextField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    filename = models.TextField()
    original_filename = models.TextField()
    file_size = models.IntegerField()
    compressed_file_size = models.IntegerField(blank=True, null=True)
    mime_type = models.TextField()
    photo_latitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    photo_longitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    photo_timestamp = models.DateTimeField()
    photo_date = models.DateField()
    photo_time = models.TextField()
    gps_accuracy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    distance_from_spot = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    original_file_path = models.TextField(blank=True, null=True)
    compressed_file_path = models.TextField(blank=True, null=True)
    is_approved = models.IntegerField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    rejection_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sot_photos'


class ThingLocations(models.Model):
    pk = models.CompositePrimaryKey('thing_id', 'location_id')
    thing = models.ForeignKey('Things', models.DO_NOTHING)
    location = models.ForeignKey(Locations, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'thing_locations'
        unique_together = (('thing', 'location'),)


class Things(models.Model):
    thing_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'things'


class Users(models.Model):
    uname = models.TextField()
    password = models.TextField()
    salt = models.TextField()
    random = models.TextField()
    uid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'users'
