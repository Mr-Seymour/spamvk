import vk_api
import time
import random

vk = vk_api.VkApi(login = '<phone number>',password = '<anypassword>')
vk.auth()

values = {'out':0 , 'count':100 , 'time_offset':60}
response = vk.method('messages.get', values)

def send_msg(user_id, text_m):
    vk.method('messages.send', {'user_id': user_id , 'message':text_m})

bad_ans = ("Егор скинь 8-ую лабу x37","Егор скинь 8-ую лабу x68","Егор скинь 8-ую лабу x69","Егор скинь 8-ую лабу x70","Егор скинь 8-ую лабу x71","Егор скинь 8-ую лабу x72","Егор скинь 8-ую лабу x73","Егор скинь 8-ую лабу x74","Егор скинь 8-ую лабу x75","Егор скинь 8-ую лабу x76","Егор скинь 8-ую лабу x77","Егор скинь 8-ую лабу x78","Егор скинь 8-ую лабу x79","Егор скинь 8-ую лабу x80","Егор скинь 8-ую лабу x81","Егор скинь 8-ую лабу x82","Егор скинь 8-ую лабу x83","Егор скинь 8-ую лабу x84","Егор скинь 8-ую лабу x85","Егор скинь 8-ую лабу x86","Егор скинь 8-ую лабу x87","Егор скинь 8-ую лабу x88","Егор скинь 8-ую лабу x89","Егор скинь 8-ую лабу x90","Егор скинь 8-ую лабу x91","Егор скинь 8-ую лабу x92","Егор скинь 8-ую лабу x93","Егор скинь 8-ую лабу x94","Егор скинь 8-ую лабу x95","Егор скинь 8-ую лабу x96","Егор скинь 8-ую лабу x97","Егор скинь 8-ую лабу x98","Егор скинь 8-ую лабу x99","Егор скинь 8-ую лабу x100","Егор скинь 8-ую лабу x101","Егор скинь 8-ую лабу x102","Егор скинь 8-ую лабу x103","Егор скинь 8-ую лабу x104","Егор скинь 8-ую лабу x105","Егор скинь 8-ую лабу x106","Егор скинь 8-ую лабу x107","Егор скинь 8-ую лабу x108","Егор скинь 8-ую лабу x109","Егор скинь 8-ую лабу x110","Егор скинь 8-ую лабу x111","Егор скинь 8-ую лабу x112","Егор скинь 8-ую лабу x113","Егор скинь 8-ую лабу x114","Егор скинь 8-ую лабу x115","Егор скинь 8-ую лабу x116","Егор скинь 8-ую лабу x117","Егор скинь 8-ую лабу x118","Егор скинь 8-ую лабу x119","Егор скинь 8-ую лабу x120","Егор скинь 8-ую лабу x121","Егор скинь 8-ую лабу x122","Егор скинь 8-ую лабу x123","Егор скинь 8-ую лабу x124","Егор скинь 8-ую лабу x125","Егор скинь 8-ую лабу x126","Егор скинь 8-ую лабу x127","Егор скинь 8-ую лабу x128","Егор скинь 8-ую лабу x129","Егор скинь 8-ую лабу x130","Егор скинь 8-ую лабу x131","Егор скинь 8-ую лабу x132","Егор скинь 8-ую лабу x133","Егор скинь 8-ую лабу x134","Егор скинь 8-ую лабу x135","Егор скинь 8-ую лабу x136")
learn = 'Ничего не делать, забить на все, заниматься тем, что хочешь. Ой, это же твои мечты. А на завтра 1000 страниц литературы Назарова'
l = ('учить','задали','нам по')

bo = False

while True:

    response = vk.method('messages.get', values)

    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
        #print (response)
    for item in response['items']:
        if response == 'а':
            for i in range(1000):
                send_msg(item['user_id'], bad_ans[random.randint(0, 1000)])
                time.sleep(2)

    time.sleep(5)
