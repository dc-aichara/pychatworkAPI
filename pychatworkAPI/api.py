import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests import Response
from typing import List, Union


class Chatwork(object):
    """
    Chatwork rest API
    """

    __API_URL_BASE = "https://api.chatwork.com/v2"

    def __init__(
        self, api_token: str, api_base_url: str = __API_URL_BASE
    ) -> None:
        """
        Initiate with base url and api token
        Args:
            api_token (str): Your Chatwork API token
            api_base_url (str): Chatwork rest API base url
        """
        self.api_base_url = api_base_url
        self.api_key = api_token
        self.endpoint = api_base_url
        self.headers = {"X-ChatWorkToken": self.api_key}
        self.request_timeout = 120
        self.session = requests.Session()
        retries = Retry(
            total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504]
        )
        self.session.mount("http://", HTTPAdapter(max_retries=retries))

    def get_me(self) -> dict:
        """
        Get your account information.
        Return:
            dict: Your account information (json)
        """
        get_url = "{}/me".format(self.endpoint)
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def get_my_status(self) -> dict:
        """
        Get the number of: unread messages, unread To messages, and unfinished tasks.
        Return:
             dict: The number of: unread messages, unfinished tasks etc.
        """
        get_url = "{}/my/status".format(self.endpoint)
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def get_my_tasks(self) -> Union[str, list]:
        """
        Get list of all your unfinished tasks.
        Return:
             list: list of task if there is any otherwise a json error
        """
        get_url = "{}/my/tasks?".format(self.endpoint)
        response = requests.get(get_url, headers=self.headers)
        if response.status_code != 204:
            return response.json()
        return "You don't have tasks!"

    def get_contacts(self) -> List[dict]:
        """
        Get the list of your contacts.
        Return:
             list: list of your contacts
        """
        get_url = "{}/contacts".format(self.endpoint)
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def get_rooms(self) -> List[dict]:
        """
        Get the list of all chats on your account.
        Return:
             tuple: list of all rooms
        """
        get_url = "{}/rooms".format(self.endpoint)
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def send_message(self, room_id: int, message: str) -> Response:
        """
        Send message to a chat.
        Args:
            room_id (int): Room id
            message (str): Your message text
        Returns:
            Response 200

       """
        post_message_url = "{}/rooms/{}/messages".format(
            self.endpoint, room_id, message
        )
        params = {"body": message}
        response = requests.post(
            post_message_url, headers=self.headers, params=params
        )
        return response

    def send_file(
        self, room_id: int, file_path: str, file_name: str, message: str
    ) -> Response:
        """
        Send a file with message to a chat.
        Args:
            room_id (int): Room id
            file_path (str): File path
            file_name (str): File name
            message (str): Text message

        Returns:
            Response 200
        """
        message_url = "{}/rooms/{}/files".format(self.endpoint, room_id)
        files = {
            "file": (file_name, open(file_path, "rb")),
            "message": (None, message),
        }
        response = requests.post(message_url, headers=self.headers, files=files)
        return response

    def get_rooms_by_id(self, room_id: int) -> dict:
        """
        Get chat name, icon, and Type (my, direct, or group)
        Args:
            room_id (int): Room id

        Returns:
            dict: Room details

        """
        get_url = "{}/rooms/{}".format(self.endpoint, room_id)
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def delete_rooms_by_id(self, room_id: int, action: str) -> Response:
        """
        Leave or delete a group chat.
        Args:
            room_id (int): Room id
            action (str): action (leave or delete)

        Returns:
            Response

        """
        data = {"action_type": action}
        get_url = "{}/rooms/{}".format(self.endpoint, room_id)
        response = requests.delete(get_url, data=data, headers=self.headers)
        return response

    def get_rooms_members(self, room_id: int) -> List[dict]:
        """
        Change associated members of group chat at once.
        Args:
            room_id (int): Room id

        Returns:
            list: All members information

        """
        try:
            get_url = "{}/rooms/{}/members".format(self.endpoint, room_id)
            response = requests.get(get_url, headers=self.headers)
            return response.json()
        except Exception as ex:
            print("Get rooms members error - {}".format(ex))

    def get_rooms_messages(self, room_id: int) -> List[dict]:
        """
        Get all messages associated with the specified chat (returns up to 100 entries).
        Args:
            room_id (int): Room id

        Returns:
            list: list of 100 entries

        """
        get_url = "{}/rooms/{}/messages".format(self.endpoint, room_id)
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def get_rooms_message_information(
        self, room_id: int, message_id: int
    ) -> dict:
        """
        Get information of a specified message.
        Args:
            room_id (int): Target chat's room id
            message_id (int): Message id of message which information is needed

        Returns:
            dict: Information of specific message

        """
        get_url = "{}/rooms/{}/messages/{}".format(
            self.endpoint, room_id, message_id
        )
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def add_rooms_task(
        self,
        room_id: int,
        task_name: str,
        time_limit: int,
        account_ids: List[int],
    ) -> dict:
        """
        Add a new task to the chat.
        Args:
            room_id (int): Target room id / chat id
            task_name (str): Task name
            time_limit (int): ime limit ( Use Unix time as input)
            account_ids (List[int]]): list of account ids

        Returns:
            dict: dictionary of list of tasks ids

        """
        params = {"body": task_name, "limit": time_limit, "to_ids": account_ids}

        get_url = "{}/rooms/{}/tasks".format(self.endpoint, room_id)
        response = requests.post(get_url, data=params, headers=self.headers)
        return response.json()

    def get_rooms_tasks(self, room_id: int) -> List[dict]:
        """
        Get the list of task of a chat
        Args:
            room_id (int): Target chat's room id
        Return:
             list: list of the tasks' details
        """
        get_url = "{}/rooms/{}/tasks".format(self.endpoint, room_id)
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def get_rooms_task_information(self, room_id: int, task_id: int) -> dict:
        """
        Get information about the specified task.
        Args:
            room_id (int): Target chat's room id
            task_id (int): Task id which information is needed
        Return:
             dict: Returns task information
        """
        get_url = "{}/rooms/{}/tasks/{}".format(self.endpoint, room_id, task_id)
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def get_rooms_files(self, room_id: int) -> List[dict]:
        """
        Get the list of files associated with the specified chat.
        Args:
            room_id (int): Target chat's room id
        Return:
             list: Returns up to 100 entries of files
             
        """
        get_url = "{}/rooms/{}/files".format(self.endpoint, room_id)
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def get_rooms_file_information(self, room_id: int, file_id: int) -> dict:
        """
        Get information about the specified file.
        Args:
            room_id (int) : Target chat's room id
            file_id (int): file id which information is needed
            
           Return:
                dict: Returns file's information with a file download link
                
        """
        get_url = "{}/rooms/{}/files/{}?create_download_url=1".format(
            self.endpoint, room_id, file_id
        )
        response = requests.get(get_url, headers=self.headers)
        return response.json()

    def create_new_room(
        self,
        description: str,
        members_member_ids: List[int],
        icon_preset: str,
        members_readonly_ids: List[int],
        members_admin_ids: List[int],
        name: str,
    ) -> Response:
        """
        Create a new group chat
        Args: 
            description (str): Group description
            members_member_ids (list): List member ids of group members
            icon_preset (str): group icon
                            [group, check, document, meeting, event, project, business, study,
                             security, star, idea, heart, magcup, beer, music, sports, travel]
            members_readonly_ids (list) : List of read only ids
            members_admin_ids (list): List of admin ids
            name (str): Group name
        Return:
             Response
        """

        params = {
            "description": description,
            "members_member_ids": members_member_ids,
            "icon_preset": icon_preset,
            "members_readonly_ids": members_readonly_ids,
            "members_admin_ids": members_admin_ids,
            "name": name,
        }

        post_url = "{}/rooms".format(self.endpoint)
        response = requests.post(post_url, data=params, headers=self.headers)
        return response

    def change_room_info(
        self, room_id: int, description: str, name: str, icon_preset: str
    ) -> Response:
        """
        Change the title and icon type of the specified chat
        Args:
            room_id (int): Target chat's room id
            description (str):  chat description to be updated
            name: (str) Name of chat room
            icon_preset (str): group icon
                                    [group, check, document, meeting, event, project, business, study,
                                     security, star, idea, heart, magcup, beer, music, sports, travel]

        Return:
            Response

        """
        params = {
            "description": description,
            "name": name,
            "icon_preset": icon_preset,
        }
        put_url = "{}/rooms/{}".format(self.endpoint, room_id)
        response = requests.put(put_url, data=params, headers=self.headers)
        return response

    def change_rooms_members(
        self,
        room_id: int,
        members_admin_ids: List[int],
        members_member_ids: List[int],
        members_readonly_ids: List[int],
    ) -> Response:
        """
        Change associated members of group chat at once
        Args:
            room_id (int): Target chat's ID
            members_admin_ids (list): list of ids [Required]
            members_member_ids (list): list of ids
            members_readonly_ids (list): list of ids

        Return:
             Response
        """

        params = {
            "members_admin_ids": members_admin_ids,
            "members_member_ids": members_member_ids,
            "members_readonly_ids": members_readonly_ids,
        }
        put_url = "{}/rooms/{}/members".format(self.endpoint, room_id)
        response = requests.put(put_url, data=params, headers=self.headers)
        return response

    def get_incoming_requests(self) -> Union[str, list]:
        """
        You can get the list of contact approval request you received.

        Return:
             list/str: List of of contact approval request
        """
        get_url = "{}/incoming_requests".format(self.endpoint)
        response = requests.get(get_url, headers=self.headers)
        if response.status_code != 204:
            return response.json()
        return "No requests found!"

    def approve_incoming_requests(self, request_id: int) -> dict:
        """
        You can approve a contact approval request you received.
        Args:
            request_id (int): Request id to be approved 
        Return:
             dict: request ids information
        """
        get_url = "{}/incoming_requests/{}".format(self.endpoint, request_id)
        response = requests.put(get_url, headers=self.headers)
        return response.json()

    def delete_incoming_requests(self, request_id: int) -> Response:
        """
        You can delete a contact approval request you received.
        Args:
            request_id (int): Request id to be deleted

        Return:
            Response
        """
        get_url = "{}/incoming_requests/{}".format(self.endpoint, request_id)
        response = requests.delete(get_url, headers=self.headers)
        return response
