# paml/urls.py
from django.urls import path, re_path
from . import views
app_name = 'palm'
urlpatterns = [

    # index
    # index end

    # control
    path('cctv/', views.cctv, name = 'cctv'),
    path('cctv/<int:id>/', views.cctv_n_house, name = 'cctv_house'),
    path("cctv/control/", views.control, name = "control"),
    path('cctv/control/<int:id>', views.control_n, name = 'control_house'),
    path('cctv/control/temp', views.control_temp, name='control_temp'),
    # 이 url은 아마 데이터 통신을 담당할 것 즉 리다이렉트 되는 url 주소가 된다 (명령어처리)
    # control end

    # setting
    path('setting/', views.setting, name = 'setting'),
    path('setting/<int:id>/', views.setting_n, name = 'setting_house'),
    path('setting/<int:id>/emergency/', views.emergency, name = 'emergency'),
    path('setting/<int:id>/operating/', views.operating, name = 'operating'),
    path('setting/<int:id>/emergency/edit', views.emergency_edit, name = 'emergency_edit'),
    # edit을 하기위해선 그 테이블에 user와 gcg_id의 외래키를 가진 row가 존재해야한다 따라서 user을 등록하는 과정에서 이를 같이 등록하는것이 유연할거같음
    # 더정확히 묘사하자면 user 을 등록할때 새로운 row를 만들어주는데 외래키는 user와 gcg_id의 외래키를 가지고, value는 default(쉽게 수정이가능한 값) 으로 설정해둠(동적으로)
    path('setting/<int:gcg_id>/operating/<int:opr_id>/edit/', views.operating_edit, name = 'operating_edit'),
    path('setting/temp', views.setting_temp, name = 'temp'),
    # 마찬가지로 데이터 통신을 담당하는 url(리다이렉트시킬)
    # setting end

    # record
    path('vegi/', views.vegi_category, name = 'vegi_category'),
    path('vegi/<int:vegi_id>/', views.record_list, name = 'record_list'),
    path('vegi/<int:vegi_id>/<int:record_id>/', views.record_detail, name = 'record_detail'),
    # record/record_vegi_new
    path('vegi/new/', views.vegi_category_new, name = 'record_vegi_new'),
    # record/record_vegi_record_new
    path('vegi/<int:vegi_id>/new/', views.record_new, name = 'record_new'),
    path('vegi/<int:vegi_id>/<int:record_id>/edit/', views.record_edit, name = 'record_edit'),
    # record_end
    path('test/', views.test, name = 'test'),
    path('test_display/', views.test_display, name = 'test_display'),
    # path('test/<str:response>/', views.test_response, name = 'test_response'),
    path('test/<int:anode_id>/', views.request_to_GCG, name = 'request_GCG'),
    # test url

]