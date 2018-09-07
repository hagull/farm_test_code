from urllib import request
from .models import TestSnode
import datetime, time

while 1:
    date_now = datetime.datetime.now()
    date_S = date_now.strftime('%S')
    if (int(date_S) % 5) == 0:
        url_response = request.urlopen('url')
        url_text = url_response.read().decode('utf8')
        url_list = url_text[4:-5].split('/')
        gcg_id = url_list[0]
        snode_id = url_list[1]
        snode_value1 = url_list[2]
        snode_value2 = url_list[3]
        TestSnode.objects.create(gcg_id=1, snode_id=snode_id, snode_value_temp = snode_value1, snode_value_humd = snode_value2, house_id = 1)
        print('response from GCG : {}'.format(url_text))
        time.sleep(1.5)