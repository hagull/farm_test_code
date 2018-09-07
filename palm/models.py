from django.db import models
from django.conf import settings
from django.urls import reverse
import datetime, time

class Owner(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.PROTECT)
    house_num = models.IntegerField()
    joined_at = models.DateTimeField(auto_now_add = True)
    pass
class CctvOutside(models.Model):
    gcg = models.ForeignKey('Gcg', on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
    def __str__(self):
        return 'cctv_outside of {}'.format(self.gcg)
# cctv 외부와 내부를 나누어 각각의 URL 혹은 IP주소를 저장한다. 이렇게 하는게 GCG 에서 접근하기가 편하게 할수있다.
class CctvInside(models.Model):
    gcg = models.ForeignKey('Gcg', on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
    def __str__(self):
        return 'cctv_inside of {}'.format(self.gcg)
class Gcg(models.Model):
    gcg_id = models.IntegerField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='gcg_set', on_delete=models.PROTECT)
    # owner = models.ForeignKey('Owner', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    snode_num = models.IntegerField()
    anode_num = models.IntegerField()
    cctv_outside_num = models.IntegerField()
    cctv_inside_num = models.IntegerField()
    def __str__(self):
        return '[user : ({}) / gcg_id : ({})]'.format(self.user, self.gcg_id)
    pass
# 사실상 gcg 모델과 gcginfo모델을 합쳐도 상관없음
class GcgInfo(models.Model):
    gcg = models.OneToOneField('Gcg', on_delete=models.CASCADE)
    snode_num = models.IntegerField()
    data_period = models.DateTimeField()
    anode_num = models.IntegerField()
    cctv_num = models.IntegerField()
    ipv4 = models.CharField(max_length=100)
    ipv6 = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    mcu = models.CharField(max_length=50)   # choice
    os = models.CharField(max_length=50)    # choice
    updated_at = models.DateTimeField(auto_now=True)
    pass

class Snode(models.Model):
    gcg = models.ForeignKey('Gcg', on_delete=models.PROTECT)
    snode_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    snode_value = models.IntegerField(default=None)
    def __str__(self):
        return 'Gcg : ({}) / Snode_id : ({})'.format(self.gcg, self.snode_id)
    pass

class Anode(models.Model):
    gcg = models.ForeignKey('Gcg', on_delete=models.PROTECT)
    anode_id = models.IntegerField(unique=True)
    anode_value = models.BooleanField(default=None)
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Gcg : ({}) / Anode_id : ({})'.format(self.gcg, self.anode_id)
    pass

class SnodeInfo(models.Model):
    snode = models.OneToOneField('Snode', on_delete=models.CASCADE)
    sw_version = models.CharField(max_length=50)
    register_id = models.IntegerField()     # unique 물어보기
    register_date = models.DateTimeField(auto_now_add=True)
    node_status = models.CharField(max_length=50)
    monitor = models.CharField(max_length=50)   #choice
    set_vlaue = models.CharField(max_length=100, blank=True)
    comm_err_num = models.IntegerField()
    service_err_num = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    pass

class AnodeInfo(models.Model):
    anode = models.OneToOneField('Anode', on_delete=models.CASCADE)
    sw_version = models.CharField(max_length=50)
    register_id = models.IntegerField()  # unique 물어보기
    register_date = models.DateTimeField(auto_now_add=True)
    node_status = models.CharField(max_length=50)
    opr_status = models.CharField(max_length=100)
    monitor = models.CharField(max_length=50)  # choice
    set_vlaue = models.CharField(max_length=100, blank=True)
    emergency_id = models.ForeignKey('Snode', on_delete=models.CASCADE)
    comm_err_num = models.IntegerField()
    service_err_num = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    pass

class Address(models.Model):
    pass


class VegiType(models.Model):
    VEGI_TYPE = (
        ('a', '오이'),
        ('b', '딸기'),
        ('c', '더덕'),  # 이는 나중에 가나다 순으로 정렬하는게 가독성을 높일수 있을듯 ?
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='daily_set', on_delete=models.PROTECT)
    # owner = models.ForeignKey('Owner', on_delete=models.PROTECT) 아직 유저모델을 만들지 않아 보류
    vegi_type = models.CharField(max_length=1, choices=VEGI_TYPE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.get_vegi_type_display()
    def get_absolute_url(self):
        return reverse('palm:vegi_category')

class Record(models.Model):
    VEGI_DATE = (
        ('s', '재배 시작'),  # start
        ('i', '재배중'),  # ing
        ('e', '재배 종료'),  # end
    )
    # owner = models.ForeignKey('Owner', on_delete=models.PROTECT) 아직 유저모델을 만들지 않아 보류
    vegi_type = models.ForeignKey(VegiType, on_delete=models.PROTECT)
    vegi_size = models.FloatField()
    vegi_condition = models.CharField(max_length=50)     # choice
    vegi_cultivation = models.CharField(max_length=1, choices=VEGI_DATE)      # choice
    vegi_shipment = models.FloatField()
    vegi_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse('palm:record_detail', args=[self.vegi_type_id, self.id])

class Emergency(models.Model):
    gcg = models.ForeignKey('Gcg', on_delete=models.CASCADE)
    emergency_id = models.ForeignKey('Snode', on_delete=models.CASCADE)
    u_value = models.FloatField()
    r_value = models.FloatField()
    l_value = models.FloatField()
    anode = models.ForeignKey('Anode', on_delete= models.CASCADE)
    priority = models.IntegerField()
    # 나중에 우선순위에 gcg별로 우선순위를 부여하여야함
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return 'Emergency mode for Gcg : ({})'.format(self.gcg)
class Operating(models.Model):
    gcg = models.ForeignKey('Gcg', on_delete=models.CASCADE)
    opr_type = models.CharField(max_length=100)
    opr_comment = models.TextField()
    snode_num = models.IntegerField()
    anode_num = models.IntegerField()
    u_value = models.FloatField()
    r_value = models.FloatField()
    l_value = models.FloatField()
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return 'Operating Type : ({}) / gcg_id : ({})'.format(self.opr_type, self.gcg)
class OprSnode(models.Model):
    operating = models.ForeignKey('Operating', on_delete=models.CASCADE)
    snode = models.ForeignKey('Snode', on_delete=models.CASCADE)
    def __str__(self):
        return 'Operating Snode : ({}) / Snode : ({})'.format(self.operating, self.snode)
class OprAnode(models.Model):
    operating = models.ForeignKey('Operating', on_delete=models.CASCADE)
    anode = models.ForeignKey('Anode', on_delete= models.CASCADE)
    priority = models.IntegerField()
    def __str__(self):
        return 'id : ({}) / Operating Anode : ({}) . priority : ({})'.format(self.id, self.operating, self.priority)
class TestSnode(models.Model):
    gcg = models.ForeignKey('TestGcg', on_delete= models.CASCADE)
    snode_id = models.IntegerField()
    snode_value_temp = models.IntegerField(default=0, blank=True)
    snode_value_humd = models.IntegerField(default=0, blank=True)
    # value 테이블을 만들질 말지 생각 중간평가 이후
    house = models.ForeignKey('TestHouse', on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} / house : {} / snode_id : {}'.format(self.gcg, self.house, self.snode_id)
class TestAnode(models.Model):
    gcg = models.ForeignKey('TestGcg', on_delete=models.CASCADE)
    anode_id = models.IntegerField()
    anode_value = models.BooleanField(default=False)
    house = models.ForeignKey('TestHouse', on_delete=models.CASCADE, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} / house : {} / anode_id : {}'.format(self.gcg, self.house, self.anode_id)
class TestGcg(models.Model):
    gcg_id = models.IntegerField()
    def __str__(self):
        return 'Gcg_id : {}'.format(self.gcg_id)
class TestHouse(models.Model):
    gcg = models.ForeignKey('TestGcg', on_delete=models.CASCADE)
    def __str__(self):
        return '{} 동'.format(self.id)
class Test1(models.Model):
    first_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
class TestN(models.Model):
    test1_id = models.ForeignKey('Test1', on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)