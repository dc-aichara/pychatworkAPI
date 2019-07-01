# Chatwork API V2 Wrapper
***
pychatworkAPI is a python package to access chatwork offline.  It is based on [Chatwork API V2](http://download.chatwork.com/ChatWork_API_Documentation.pdf). 

***
## Installation 

### PyPI
```
pip install pychatworkAPI
```
### From Source (Github)

git clone https://github.com/dc-aichara/pychatworkAPI.git

cd pychatworkAPI

python3 setup.py install
***
## Usages

```python
from pychatworkAPI import Chatwork

api = Chatwork('Your Chatwork API Token')
```
### basic usages
```python

>>> api.get_me() # get your account information
{'account_id': xxxxx, 'room_id': 1xxxxxxx, 'name': 'Dayal Chand Aichara', 'chatwork_id': '', 'organization_id': xxxxx, 'organization_name': 'ABC Inc.', 
'department': '', 'title': '', 'url': '', 'intron': '', 'mail': '', 'tel_organization': '', 'tel_extension': '', 'tel_mobile': '', 'skype': '', 'facebook': '', 'twitter': '', 'avatar_image_url': 'https://appdata.chatwork.com/avatar/xxxxx.rsz.jpg', 'login_mail': 'name@gmail.com'}


>>> api.get_my_status() # get your status
{'unread_room_num': 0, 'mention_room_num': 0, 'mytask_room_num': 0, 'unread_num': 0, 'mention_num': 0, 'mytask_num': 0}


>>> api.get_my_tasks() # get list of taskd assigned to you
[{'task_id': 139296044, 'room': {'room_id': 1xxxxx7, 'name': 'Group Name', 'icon_path': 'https://appdata.chatwork.com/icon/ico_xxx.png'},
 'assigned_by_account': {'account_id': xxxxx, 'name': 'Dayal Chand Aichara', 'avatar_image_url': 'https://appdata.chatwork.com/avatar/xxxx/xxxx.rsz.jpg'}, 'message_id': '119629631860408724', 'body': 'Update Server', 'limit_time': 1685996399, 'status': 'open', 'limit_type': 'date'}]


>>> api.get_contacts() # get contacts list


>>> api.get_rooms() # get chat rooms list


# api.send_message(self, room_id, message)
>>> api.send_message(1987672538, 'test') # send message to a chat
<Response [200]>


# api.send_file(self, room_id, file_path, file_name,  message)
>>> api.send_file(1987672538,'a.jpg', 'a.jpg', 'test')  # send a file with message to a chat
<Response [200]>

````

### Chat Rooms
```python

>>> api.get_rooms_by_id(self, room_id) # get room details by room id


# api.get_rooms_memebers(self, room_id)
>>> api.get_rooms_memebers(15xxxx38)  # get room members information
[{'account_id': xxxxxx, 'role': 'admin', 'name': 'Dayal Chand Aichara', 'chatwork_id': '', 
'organization_id': xxxxx, 'organization_name': 'ABC Inc.', 'department': 'Data Analytics', 
'avatar_image_url': 'https://appdatwork.com/avatar//xxxxxx.rsz.jpg'}]


# api.get_rooms_messages(room_id)
>>> api.get_rooms_messages(15xxxx38) # get messages of a room
[{'message_id': '11963102598912', 'account': {'account_id': xxxxx, 'name': 'Dayal Chand Aichara', 'avatar_image_url': 'https://appdata.chatwork.com/avatar/xxx.rsz.jpg'}, 
'body': '[info][title][dtext:chatroom_groupchat_created][/title][dtext:chatroom_chatname_is]test[dtext:chatroom_set]\n\n[dtext:chatroom_member_is][piconname:367][dtext:chatroom_added][/info]', 'send_time': 1561697609, 'update_time': 0}]


>>> api.get_rooms_message_information(room_id, message_id) # get specific message information from a chat room


# api.add_rooms_task(self, room_id, task_name, time_limit, account_ids)
>>> api.add_rooms_task(15xxx34, 'Update Server1',1685996399,123456)  # assign a task to member of room
{'task_ids': [139298115]}


# get_rooms_task_information(self, room_id, task_id)
>>> api.get_rooms_task_information(1xxxxx7,139296044) # get task information by task id
{'task_id': 139296044, 'account': {'account_id': 3xxxxxx, 'name': 'Dayal Chand Aichara', 'avatar_image_url': 'https://appdata.chatwork.com/avatar/xxxx/xxxxx.rsz.jpg'}, 'assigned_by_account': {'account_id': xxxxxx, 'name': 'Dayal Chand Aichara', 'avatar_image_url': 'https://appdata.chatwork.com/avatar/xxxx/xxxx.rsz.jpg'},
 'message_id': '119629638789764', 'body': 'Update Server', 'limit_time': 1685996399, 'status': 'open', 'limit_type': 'date'}


# api.get_rooms_files(self, room_id)
>>> api.get_rooms_files(1543544441325) # get information of files in a chat room
[{'file_id': 456xx, 'message_id': '11876358888392320', 'filesize': 91571, 'filename': 'abc.png', 'upload_time': 1559627849, 
'account': {'account_id': xxxx, 'name': 'Dayal Chand Aichara', 'avatar_image_url': 'https://appdata.chatwork.com/avatar/xxxx.rsz.jpg'}}, {'file_id': 37xxxx, 'message_id': '118763998741469696', 'filesize': 202409, 'filename': '2019-06-03.png', 'upload_time': 1559629010, 'account':
 {'account_id': xxxx, 'name': 'Dayal Chand Aichara', 'avatar_image_url': 'https://appdata.chatwork.com/avatar/xxxx.rsz.jpg'}}]


# api.get_rooms_file_information(self, room_id, file_id)
>>> api.get_rooms_file_information(1543544441325,3851450 ) # get details of a file by file id in a chat room
{'file_id': 3851450, 'message_id': '1193811580355072', 'filesize': 177560, 'filename': 'data.png', 'upload_time': 1561100416, 'account':
 {'account_id': xxxx, 'name': 'Dayal Chand Aichara', 'avatar_image_url': 'https://appdata.chatwork.com/avatar/xxxx.rsz.jpg'}, 
 'download_url': 'https://appdata.chatwork.com/uploadfile/xxxx/xxxxxx/1633a41e6e6f5f0ff95d7299ff5beabf.dat?response-content-type=&response-content-disposition=attachment%3Bfilename%2A%3DUTF-8%27%27price.png&Expires=1561699134&Signature=YzyVHZaO-ZKZDjCQTYpI7JhPd8OSMZaPIMhof25aTZOdCXI-AtkJiXP1KjfcWzAnx1A-hqy08NgdfoCjjpJJlu-IWtuAn3dbrEdbklPR-udQO4i9kFiy-fTF2yUcchbuwg7mpxrYlcobTA4FZ-ojt74gv8up3HOcqJw3EcVh1RTH8rpqYqQXxklpM0-G4aPlyJ3mNqvWOvZhB4ym0daiXXqw8lmm~cAw-ai~BQ7TRgxXj~E5kWuhxJpEiBT61odILnlwSNMVODRnr76UCjljl2OEaFnpPl5fKW3J2lo9Hmq15aK-wf7OfnfIrs~5zKCbfTmetlTL-fOy-kHacC6dCg__&Key-Pair-Id=XXXXXXXXXX'}


# api.create_new_room(self,description, memebers_memeber_ids, icon_preset, members_readonly_ids, members_admin_ids, name)
>>> api.create_new_room('Test', [12, 187, 78],'group',[12, 78],[187] , 'test1') # create a new chat room
<Response [200]>

# api.delete_rooms_by_id(self, room_id, action)
>>> api.delete_rooms_by_id(1xxxx96, 'leave') # leave or delete a chat room
<Response [204]>

```
### Handling incoming requests
```python

>>> api.get_incoming_requests() # get incoming requests to join chat rooms


>>> api.approve_incoming_requests(self, request_id) # approve incoming request by request id
 

>>> api.delete_incoming_requests(self, request_id) # delete incoming request by request it


```
***
## *Responses*

> <Response [200]> Successful

> <Response [204]> No content 

> <Response [401]> Unauthorized

> <Response [403]> Unsuccessful (Check your inputs)

> <Response [429] > Too many requests (Request limit is 300/5 minutes)


***
## License 
[MIT](https://choosealicense.com/licenses/mit/) © [Dayal Chand Aichara](https://github.com/dc-aichara)

***

Note: Read [Chatwork API V2](http://download.chatwork.com/ChatWork_API_Documentation.pdf) documentation to learn more. 