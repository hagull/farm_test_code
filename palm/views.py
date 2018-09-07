from django.shortcuts import render, get_object_or_404, redirect
from .models import Record, VegiType, Gcg, Anode, Snode, Emergency, Operating, TestAnode, TestSnode, TestGcg, TestHouse
from .forms import RecordForm, VegiTypeForm, EmergencyForm, OperatingForm
from .data_test import data_co2, data_TH, description_co2, description_TH
import gviz_api
from django.http import HttpResponse
from urllib.request import urlopen

# Control view함수 - START
# 전체 CCTV화면을 보여주는 view함수
def cctv(request):
    gcg = Gcg.objects.all()
    return render(request, 'control/cctv.html', {
        'gcg' : gcg,
    })
# 특정 동의 하우스의 CCTV화면을 보여주는 view함수
def cctv_n_house(request, id):
    gcg_n = get_object_or_404(Gcg, gcg_id = id)
    gcg = Gcg.objects.all()
    # 나중에 id가 아닌 primary key값으로 대체하는게 좀더 접근할때 유연성을 제공하고 코드가독성을 높일수 있을듯함
    return render(request, 'control/cctv_n_house.html', {
        'gcg_n' : gcg_n,
        'gcg' : gcg,
    })
    # 특정 동의 하우스의 제어를 위한 view함수
def control(request):
    gcg = Gcg.objects.all()
    snode = Snode.objects.all()
    anode = Anode.objects.all()
    return render(request, 'control/control.html', {
        'gcg' : gcg,
        'snode' : snode,
        'andoe' : anode,
    })
def control_n(request, id):
    gcg = Gcg.objects.all()
    snode = Snode.objects.filter(gcg_id = id)
    # gcg 만 정의되면 나머지 snode나 anode에 접근하는것이 가능하기 때문에 나중에 빼도 상관없을거 같기는 함
    anode = Anode.objects.filter(gcg_id = id)
    gcg_n = get_object_or_404(Gcg, gcg_id = id)
    return render(request, 'control/control_n.html', {
        'gcg_n' : gcg_n,
        'snode' : snode,
        'anode' : anode,
        'gcg' : gcg,
    })
# 임시로 처리 view함수는 프로토타입 개발이후 상황에 따라 수정할 예정
def control_temp(request):
    # 데이터 처리 및 데이터 통신에 관여하는 view함수
    pass
# Control view함수 - END
# Setting view함수 - START
# 동 전체의 설정값들을 한눈에 보여주는 view함수
def setting(request):
    gcg = Gcg.objects.all()
    return render(request, 'setting/setting.html', {
        'gcg' : gcg,
    })

# 한개 동의 설정값들을 한눈에 보여주는 view함수
def setting_n(request, id):
    gcg = Gcg.objects.all()
    gcg_n = get_object_or_404(Gcg, gcg_id = id)
    return render(request, 'setting/setting_n.html', {
        'gcg_n' : gcg_n,
        'gcg' : gcg,
    })

# 한개 동의 emergency 설정값들을 보여주는 view함수
def emergency(request, id):
    gcg = Gcg.objects.all()
    gcg_n = get_object_or_404(Gcg, gcg_id = id)
    return render(request, 'setting/emergency.html', {
        'gcg_n' : gcg_n,
        'gcg' : gcg,
    })
# 한개 동의 operating 설정값들을 보여주는 view함수
def operating(request, id):
    gcg = Gcg.objects.all()
    gcg_n = get_object_or_404(Gcg, gcg_id = id)
    return render(request, 'setting/operating.html', {
        'gcg_n' : gcg_n,
        'gcg' : gcg,
    })
# 한개 동의 emergency 설정값들을 수정하는 view함수
def emergency_edit(request, id):
    emergency = get_object_or_404(Emergency, gcg_id=id)
    if request.method == 'POST':
        form = EmergencyForm(request.POST, request.FILES, instance=emergency)
        if form.is_valid():  # 유효성 검사가 수행됨
            record = form.save()
            return redirect(emergency)
    else:
        form = EmergencyForm(instance=emergency)
    return render(request, 'setting/setting_form.html', {
        'form': form,
    })
# 한개 동의 operating 설정값들을 수정하는 view함수
def operating_edit(request, gcg_id, opr_id):
    operating = get_object_or_404(Operating, gcg_id = gcg_id, id = opr_id)
    if request.method == 'POST':
        form = OperatingForm(request.POST, request.FILES, instance=operating)
        if form.is_valid():  # 유효성 검사가 수행됨
            record = form.save()
            return redirect(operating)
    else:
        form = OperatingForm(instance=operating)
    return render(request, 'setting/setting_form.html', {
        'form': form,
    })
# 임시 url (주 목적은 redirect로 데이터를 gcg 쪽으로 전달하는 역할을할 url)
def setting_temp(request):
    pass
# Setting view함수 - END


# NewRecord view함수 - START
# owner가 키우는 작물들을 표현하는 view함수

def vegi_category(request):
    all_vegi = VegiType.objects.all()
    return render(request, 'record/vegi_category.html',{
        'vegi_category' : all_vegi,
    })

# owner가 키우는 작물들의 일지를 표현하는 view함수
def record_list(request, vegi_id):
    record_qurry = Record.objects.filter(vegi_type_id = vegi_id)
    return render(request, 'record/record_list.html', {
        'record_qurry' : record_qurry,
        'vegi_type_id' : vegi_id,
    })
# owner가 키우는 작물들의 일지의 상세내용을 표현하는 view함수
def record_detail(request, vegi_id, record_id):
    record = get_object_or_404(Record, vegi_type_id= vegi_id, id = record_id)
    return render(request, 'record/record_detail.html', {
        'record' : record,
    })
# -> new & edit 등을 표현하는 함수들 <-
# owner가 새로 키우는 작물을 추가하는 작업의 view함수
def vegi_category_new(request):
    if request.method =='POST':
        form = VegiTypeForm(request.POST, request.FILES)
        if form.is_valid():
            vegi_type = form.save()
            return redirect(vegi_type)
    else:
        form = VegiTypeForm()
    return render(request, 'record/record_form.html', {
        'form': form,
    })
    # form 으로 구현 owner로부터 데이터를 입력받는 값

# owner가 작물에 대해 작물일지를 추가할때의 view함수
def record_new(request,vegi_id):
    if request.method =='POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.vegi_type_id = vegi_id
            record.save()
            return redirect(record)
    else:
        form = RecordForm()
    return render(request, 'record/record_form.html', {
        'form': form,
    })

# owner가 작성한 작물일지에 대한 수정작업을 수행하는 view함수
def record_edit(request, vegi_id, record_id):
    # form 으로 구현 owner으로 부터 수정할 데이터를 입력 받는 값
    record = get_object_or_404(Record, vegi_type_id = vegi_id, id = record_id)
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():  # 유효성 검사가 수행됨
            record = form.save(commit=False)
            record.vegi_type_id = vegi_id
            record.save()
            return redirect(record)
    else:
        form = RecordForm(instance=record)
    return render(request, 'record/record_form.html', {
        'form': form,
    })

# NewRecord view함수 - END
def test(request):
    data_table_TH = gviz_api.DataTable(description_TH)
    data_table_TH.LoadData(data_TH)
    data_table_co2 = gviz_api.DataTable(description_co2)
    data_table_co2.LoadData(data_co2)
    json_th = data_table_TH.ToJSon(columns_order = ("time", "temperature", "humidity"),
                                   order_by = "time")
    #jscode_th = data_table_TH.ToJSCode("jscode_data_th",
    #                                   columns_order=("time", "co2concentration"),
    #                                   order_by="time")
    json_co2 = data_table_co2.ToJSon(columns_order = ("time", "co2concentration"),
                                     order_by = "time")
    #jscode_co2 = data_table_co2.ToJSCode("jscode_data_co2",
    #                             columns_order = ("time", "temperature", "humidity"),
    #                             order_by = "time")
    return render(request, 'record/test.html', {
        'json_th' : json_th,
        #'jscode_th' : jscode_th,
        'json_co2' : json_co2,
        #'jscode_co2' : jscode_co2,
    })

def test_display(request):
    snode_house1 = TestSnode.objects.filter(house=1)
    snode_house2 = TestSnode.objects.filter(house=2)
    anode_house = TestAnode.objects.all()
    anode_house1_state = TestAnode.objects.filter(house=1).last().anode_value
    anode_house2_state = TestAnode.objects.filter(house=2).last().anode_value
    if anode_house1_state == True:
        anode_house1_state = 'on'
    elif anode_house1_state == False:
        anode_house1_state = 'off'
    if anode_house2_state == True:
        anode_house2_state = 'on'
    elif anode_house2_state == False:
        anode_house2_state = 'off'
    snode_display1_temp = snode_house1.values('snode_value_temp', 'created_at')
    snode_display2_temp = snode_house2.values('snode_value_temp', 'created_at')
    snode_display1_temp_480 = snode_display1_temp[len(snode_display1_temp)-480:len(snode_display1_temp)]
    snode_display2_temp_480 = snode_display2_temp[len(snode_display2_temp)-480:len(snode_display2_temp)]
    description_temp = {"time" : ("datetime", "Time"),
                        "1house": ("number", "1House"),
                        "2house": ("number", "2House")}
    data_temp = snode_display1_temp_480
    for i in range(len(data_temp)):
        data_temp[i]['created_at'] = data_temp[i]['created_at'].replace(microsecond = 0)
        data_temp[i]['time'] = data_temp[i].pop('created_at')
        data_temp[i]['1house'] = data_temp[i].pop('snode_value_temp')
        data_temp[i]['2house'] = snode_display2_temp_480[i].pop('snode_value_temp')
        data_temp[i]['1house'] = (data_temp[i]['1house'], '{}℃'.format(data_temp[i]['1house']))
        data_temp[i]['2house'] = (data_temp[i]['2house'], '{}℃'.format(data_temp[i]['2house']))
        # data_temp생성
    data_temp_table = gviz_api.DataTable(description_temp)
    data_temp_table.LoadData(data_temp)
    json_temp = data_temp_table.ToJSon(columns_order=("time", "1house", "2house"), order_by="time")
    # json_temp 데이터 생성
    snode_display1_humd = snode_house1.values('snode_value_humd', 'created_at')
    snode_display2_humd = snode_house2.values('snode_value_humd', 'created_at')
    snode_display1_humd_480 = snode_display1_humd[len(snode_display1_humd)-480:len(snode_display1_humd)]
    snode_display2_humd_480 = snode_display2_humd[len(snode_display2_humd)-480:len(snode_display2_humd)]
    description_humd = {"time": ("datetime", "Time"),
                        "1house": ("number", "1House"),
                        "2house": ("number", "2House")}
    data_humd = snode_display1_humd_480
    for i in range(len(data_humd)):
        data_humd[i]['created_at'] = data_humd[i]['created_at'].replace(microsecond = 0)
        data_humd[i]['time'] = data_humd[i].pop('created_at')
        data_humd[i]['1house'] = data_humd[i].pop('snode_value_humd')
        data_humd[i]['2house'] = snode_display2_humd_480[i].pop('snode_value_humd')
        data_humd[i]['1house'] = (data_humd[i]['1house'], '{}'.format(data_humd[i]['1house']))
        data_humd[i]['2house'] = (data_humd[i]['2house'], '{}'.format(data_humd[i]['2house']))
        # data_humd생성
    data_humd_table = gviz_api.DataTable(description_humd)
    data_humd_table.LoadData(data_humd)
    json_humd = data_humd_table.ToJSon(columns_order=("time", "1house", "2house"), order_by="time")
    return render(request, 'test/test_display.html', {
        'json_temp' : json_humd,
        'json_humd' : json_temp,
        'anode_house1_state': anode_house1_state,
        # hi
        'anode_house2_state': anode_house2_state,
        'anode_house' : anode_house,
    })

def request_to_GCG(request, anode_id):
    anode_house_control = TestAnode.objects.filter(anode_id = anode_id).last().anode_value
    if anode_house_control == True:
        anode_house_control = '02'
        TestAnode.objects.filter(anode_id = anode_id).update(anode_value = False)
    elif anode_house_control == False:
        anode_house_control = '01'
        TestAnode.objects.filter(anode_id=anode_id).update(anode_value=True)
    GCG_url = "http://211.205.5.125:2000/0x01{}{}".format(hex(anode_id)[2:], anode_house_control)
    urlopen(GCG_url)
    anode_house1_state = TestAnode.objects.filter(house=1).last().anode_value
    anode_house2_state = TestAnode.objects.filter(house=2).last().anode_value
    if anode_house1_state == True:
        anode_house1_state = 'on'
    elif anode_house1_state == False:
        anode_house1_state = 'off'
    if anode_house2_state == True:
        anode_house2_state = 'on'
    elif anode_house2_state == False:
        anode_house2_state = 'off'
    snode_house1 = TestSnode.objects.filter(house=1)
    snode_house2 = TestSnode.objects.filter(house=2)
    anode_house = TestAnode.objects.all()
    snode_display1_temp = snode_house1.values('snode_value_temp', 'created_at')
    snode_display2_temp = snode_house2.values('snode_value_temp', 'created_at')
    snode_display1_temp_480 = snode_display1_temp[len(snode_display1_temp)-480:len(snode_display1_temp)]
    snode_display2_temp_480 = snode_display2_temp[len(snode_display2_temp)-480:len(snode_display2_temp)]
    description_temp = {"time" : ("datetime", "Time"),
                        "1house": ("number", "1House"),
                        "2house": ("number", "2House")}
    data_temp = snode_display1_temp_480
    for i in range(len(data_temp)):
        data_temp[i]['created_at'] = data_temp[i]['created_at'].replace(microsecond = 0)
        data_temp[i]['time'] = data_temp[i].pop('created_at')
        data_temp[i]['1house'] = data_temp[i].pop('snode_value_temp')
        data_temp[i]['2house'] = snode_display2_temp_480[i].pop('snode_value_temp')
        data_temp[i]['1house'] = (data_temp[i]['1house'], '{}℃'.format(data_temp[i]['1house']))
        data_temp[i]['2house'] = (data_temp[i]['2house'], '{}℃'.format(data_temp[i]['2house']))
        # data_temp생성
    data_temp_table = gviz_api.DataTable(description_temp)
    data_temp_table.LoadData(data_temp)
    json_temp = data_temp_table.ToJSon(columns_order=("time", "1house", "2house"), order_by="time")
    # json_temp 데이터 생성
    snode_display1_humd = snode_house1.values('snode_value_humd', 'created_at')
    snode_display2_humd = snode_house2.values('snode_value_humd', 'created_at')
    snode_display1_humd_480 = snode_display1_humd[len(snode_display1_humd)-480:len(snode_display1_humd)]
    snode_display2_humd_480 = snode_display2_humd[len(snode_display2_humd)-480:len(snode_display2_humd)]
    description_humd = {"time": ("datetime", "Time"),
                        "1house": ("number", "1House"),
                        "2house": ("number", "2House")}
    data_humd = snode_display1_humd_480
    for i in range(len(data_humd)):
        data_humd[i]['created_at'] = data_humd[i]['created_at'].replace(microsecond = 0)
        data_humd[i]['time'] = data_humd[i].pop('created_at')
        data_humd[i]['1house'] = data_humd[i].pop('snode_value_humd')
        data_humd[i]['2house'] = snode_display2_humd_480[i].pop('snode_value_humd')
        data_humd[i]['1house'] = (data_humd[i]['1house'], '{}'.format(data_humd[i]['1house']))
        data_humd[i]['2house'] = (data_humd[i]['2house'], '{}'.format(data_humd[i]['2house']))
        # data_humd생성
    data_humd_table = gviz_api.DataTable(description_humd)
    data_humd_table.LoadData(data_humd)
    json_humd = data_humd_table.ToJSon(columns_order=("time", "1house", "2house"), order_by="time")
    return render(request, 'test/test_display.html', {
        'json_temp': json_humd,
        'json_humd': json_temp,
        'anode_house1_state': anode_house1_state,
        'anode_house2_state': anode_house2_state,
        'anode_house' : anode_house,
    })
    