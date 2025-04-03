from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Company(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    stir = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    current_sequence = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Connection(models.Model):
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    dmtt = models.ForeignKey('Dmtt', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connection'


class Contracts(models.Model):
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    dmtt = models.ForeignKey('Dmtt', models.DO_NOTHING, blank=True, null=True)
    excel_url = models.CharField(max_length=255, blank=True, null=True)
    active_sheet_name = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contracts'


class Dmtt(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=127, blank=True, null=True)
    stir = models.CharField(max_length=10, blank=True, null=True)
    child_count = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmtt'


class HistoryStore(models.Model):
    pk = models.CompositePrimaryKey('table_name', 'pk_date_dest')
    timemark = models.DateTimeField()
    table_name = models.CharField(max_length=50)
    pk_date_src = models.CharField(max_length=400)
    pk_date_dest = models.CharField(max_length=400)
    record_state = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'history_store'
        unique_together = (('table_name', 'pk_date_dest'),)


class Limit(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    dmtt = models.ForeignKey(Dmtt, models.DO_NOTHING, blank=True, null=True)
    period = models.ForeignKey('Period', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit'


class LimitItem(models.Model):
    count = models.FloatField(blank=True, null=True)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    limit = models.FloatField(blank=True, null=True)
    contract = models.ForeignKey(Contracts, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit_item'


class OrderItems(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    product_name = models.CharField(max_length=127)
    count = models.FloatField()
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_items'


class Orders(models.Model):
    company = models.ForeignKey(Company, models.DO_NOTHING)
    dmtt = models.ForeignKey(Dmtt, models.DO_NOTHING)
    datetime = models.DateTimeField(blank=True, null=True)
    order_status = models.CharField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    sequence_number = models.IntegerField()
    drive_document_id = models.CharField(max_length=63, blank=True, null=True)
    message_id = models.CharField(max_length=63, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OtpCodes(models.Model):
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_codes'


class Period(models.Model):
    start_date = models.IntegerField(blank=True, null=True)
    end_date = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'period'


class PriceDocuments(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    excel_url = models.CharField(max_length=255, blank=True, null=True)
    active_sheet_name = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_documents'


class Products(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True)
    measure = models.CharField(max_length=15, blank=True, null=True)
    code = models.CharField(max_length=31, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    sertificate_url = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Securityjtis(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    jti = models.CharField(max_length=63, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'securityjtis'


class Users(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    new_password = models.CharField(max_length=63, blank=True, null=True)
    tg_user_id = models.CharField(max_length=16, blank=True, null=True)
    role = models.CharField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
