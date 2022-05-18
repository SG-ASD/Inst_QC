from django.db import models

# Create your models here.

class AccesorieKit(models.Model):
    Instrument_SN = models.CharField(primary_key=True, max_length=30, unique=True),
    Unpack_Instructions = models.CharField(max_length=20, blank=True),
    Installation_Qualification = models.CharField(max_length=20, blank=True),
    Final_Configuation = models.CharField(max_length=20, blank=True),
    Measurement_Protocol = models.CharField(max_length=20, blank=True),
    DeclarationSTARlet = models.CharField(max_length=20, blank=True),
    MeasurementProtocolSTARlet = models.CharField(max_length=20, blank=True),
    EU_Declaration = models.CharField(max_length=20, blank=True),
    Declaration_Quality = models.CharField(max_length=20, blank=True),
    Packing_Checklist = models.CharField(max_length=20, blank=True),
    Maintenance = models.CharField(max_length=20, blank=True),
    Channel_Adjust = models.CharField(max_length=20, blank=True),
    Loading_Table = models.CharField(max_length=30, blank=True),
    Side_Cover_right = models.CharField(max_length=20, blank=True),
    Side_Cover_left = models.CharField(max_length=20, blank=True),
    Rear_Piexiglas = models.CharField(max_length=20, blank=True),
    Top_Plexiglas = models.CharField(max_length=20, blank=True),
    Left_Plexiglas = models.CharField(max_length=20, blank=True),
    Right_Plexiglas = models.CharField(max_length=20, blank=True),
    Sensor_4L = models.CharField(max_length=20, blank=True),
    USB_Liquid = models.CharField(max_length=20, blank=True),
    USB_Solid_Liquid = models.CharField(max_length=20, blank=True),
    USB_Venus = models.CharField(max_length=20, blank=True),
    Eppendof = models.CharField(max_length=20, blank=True),
    Core_Gripper = models.CharField(max_length=20, blank=True),
    Needle_Check = models.CharField(max_length=20, blank=True),
    Needle_Lot = models.CharField(max_length=20, blank=True),
    Separator = models.CharField(max_length=20, blank=True),
    Tip_Eject = models.CharField(max_length=20, blank=True),
    Power_Cord7 = models.CharField(max_length=20, blank=True),
    Power_CordP = models.CharField(max_length=20, blank=True),


    def __str__(self):
        return self.AccesorieKit
