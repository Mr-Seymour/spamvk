import vk_api
import time
import random


values = {'out':0 , 'count':100 , 'time_offset':60}
response = vk.method('messages.get', values)

def send_msg(user_id, text_m):
    vk.method('messages.send', {'user_id': user_id , 'message':text_m})

bad_ans = ("���� ����� 8-�� ���� x37","���� ����� 8-�� ���� x68","���� ����� 8-�� ���� x69","���� ����� 8-�� ���� x70","���� ����� 8-�� ���� x71","���� ����� 8-�� ���� x72","���� ����� 8-�� ���� x73","���� ����� 8-�� ���� x74","���� ����� 8-�� ���� x75","���� ����� 8-�� ���� x76","���� ����� 8-�� ���� x77","���� ����� 8-�� ���� x78","���� ����� 8-�� ���� x79","���� ����� 8-�� ���� x80","���� ����� 8-�� ���� x81","���� ����� 8-�� ���� x82","���� ����� 8-�� ���� x83","���� ����� 8-�� ���� x84","���� ����� 8-�� ���� x85","���� ����� 8-�� ���� x86","���� ����� 8-�� ���� x87","���� ����� 8-�� ���� x88","���� ����� 8-�� ���� x89","���� ����� 8-�� ���� x90","���� ����� 8-�� ���� x91","���� ����� 8-�� ���� x92","���� ����� 8-�� ���� x93","���� ����� 8-�� ���� x94","���� ����� 8-�� ���� x95","���� ����� 8-�� ���� x96","���� ����� 8-�� ���� x97","���� ����� 8-�� ���� x98","���� ����� 8-�� ���� x99","���� ����� 8-�� ���� x100","���� ����� 8-�� ���� x101","���� ����� 8-�� ���� x102","���� ����� 8-�� ���� x103","���� ����� 8-�� ���� x104","���� ����� 8-�� ���� x105","���� ����� 8-�� ���� x106","���� ����� 8-�� ���� x107","���� ����� 8-�� ���� x108","���� ����� 8-�� ���� x109","���� ����� 8-�� ���� x110","���� ����� 8-�� ���� x111","���� ����� 8-�� ���� x112","���� ����� 8-�� ���� x113","���� ����� 8-�� ���� x114","���� ����� 8-�� ���� x115","���� ����� 8-�� ���� x116","���� ����� 8-�� ���� x117","���� ����� 8-�� ���� x118","���� ����� 8-�� ���� x119","���� ����� 8-�� ���� x120","���� ����� 8-�� ���� x121","���� ����� 8-�� ���� x122","���� ����� 8-�� ���� x123","���� ����� 8-�� ���� x124","���� ����� 8-�� ���� x125","���� ����� 8-�� ���� x126","���� ����� 8-�� ���� x127","���� ����� 8-�� ���� x128","���� ����� 8-�� ���� x129","���� ����� 8-�� ���� x130","���� ����� 8-�� ���� x131","���� ����� 8-�� ���� x132","���� ����� 8-�� ���� x133","���� ����� 8-�� ���� x134","���� ����� 8-�� ���� x135","���� ����� 8-�� ���� x136")
learn = '������ �� ������, ������ �� ���, ���������� ���, ��� ������. ��, ��� �� ���� �����. � �� ������ 1000 ������� ���������� ��������'
l = ('�����','������','��� ��')

bo = False

while True:

    response = vk.method('messages.get', values)

    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
        #print (response)
    for item in response['items']:
        if response == '�':
            for i in range(1000):
                send_msg(item['user_id'], bad_ans[random.randint(0, 1000)])
                time.sleep(2)

    time.sleep(5)