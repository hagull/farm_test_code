from django.contrib import admin
from .models import Record, VegiType, Gcg, Anode, Snode, CctvInside, CctvOutside, Emergency, Operating,OprAnode, OprSnode
from .models import TestAnode, TestGcg, TestSnode, TestHouse
# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
@admin.register(VegiType)
class VegiTypeAdmin(admin.ModelAdmin):
    pass
# 가상의 농장주 설치환경을 등록할 모델을 admin에 등록
@admin.register(Gcg)
class GcgAdmin(admin.ModelAdmin):
    pass
@admin.register(Anode)
class AnodeAdmin(admin.ModelAdmin):
    pass
@admin.register(Snode)
class SnodeAdmin(admin.ModelAdmin):
    pass
@admin.register(CctvInside)
class CctvInsideAdmin(admin.ModelAdmin):
    pass
@admin.register(CctvOutside)
class CctvOutsideAdmin(admin.ModelAdmin):
    pass
@admin.register(Emergency)
class EmergencyAdmin(admin.ModelAdmin):
    pass
@admin.register(Operating)
class OperatingAdmin(admin.ModelAdmin):
    pass
@admin.register(OprAnode)
class OprAnodeAdmin(admin.ModelAdmin):
    pass
@admin.register(OprSnode)
class OprSnodeAdmin(admin.ModelAdmin):
    pass
@admin.register(TestSnode)
class TestSnodeAdmin(admin.ModelAdmin):
    pass
@admin.register(TestGcg)
class TestGcgAdmin(admin.ModelAdmin):
    pass
@admin.register(TestAnode)
class TestAnodeAdmin(admin.ModelAdmin):
    pass
@admin.register(TestHouse)
class TestHouseAdmin(admin.ModelAdmin):
    pass
