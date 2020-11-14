import requests

class CLIHelper():
    """Helper class for demo_cli.py with static methods"""

    @staticmethod
    def send_order(order_dict):
        """Take order in dict format and send POST request
        Returns dict = {
            "url": api_url,
            "body": request_body,
            "status_code": status_code,
            "response": response_json_dict
        }
        """
        url = 'http://127.0.0.1:5000/v1/orders'
        request = requests.post(url, json=order_dict)
        if request.status_code == 200:
            response = request.json()
        else:
            response = None
        return {
            "url": url,
            "body": order_dict,
            "status_code": request.status_code,
            "response": response
        }

    @staticmethod
    def get_order(order_number):
        """Send GET request with order_number
        Returns dict = {
            "url": api_url,
            "body": request_body,
            "status_code": status_code,
            "response": response_json_dict
        }
        """
        url = 'http://127.0.0.1:5000/v1/orders/' + str(order_number)
        request = requests.get(url)
        if request.status_code == 200:
            response = request.json()
        else:
            response = None
        return {
            "url": url,
            "body": None,
            "status_code": request.status_code,
            "response": response
        }

    @staticmethod
    def update_order(order_dict, order_number):
        """Take order in dict format and send PUT request to update
        Returns dict = {
            "url": api_url,
            "body": request_body,
            "status_code": status_code,
            "response": response_json_dict
        }
        """
        url = 'http://127.0.0.1:5000/v1/orders/' + str(order_number)
        request = requests.put(url, json=order_dict)
        if request.status_code == 200:
            response = request.json()
        else:
            response = None
        return {
            "url": url,
            "body": order_dict,
            "status_code": request.status_code,
            "response": response
        }

    @staticmethod
    def delete_order(order_number):
        """Send DELETE request with order_number
        Returns dict = {
            "url": api_url,
            "body": request_body,
            "status_code": status_code,
            "response": response_json_dict
        }
        """
        url = 'http://127.0.0.1:5000/v1/orders/' + str(order_number)
        request = requests.delete(url)
        if request.status_code == 200:
            response = request.json()
        else:
            response = None
        return {
            "url": url,
            "body": None,
            "status_code": request.status_code,
            "response": response
        }

    @staticmethod
    def pickup_order(order_number):
        """Send POST request with order_number to update to pickup
        Returns dict = {
            "url": api_url,
            "body": request_body,
            "status_code": status_code,
            "response": response_json_dict
        }
        """
        url = 'http://127.0.0.1:5000/v1/orders/pickup'
        body_json = {"order_number": order_number}
        request = requests.post(url, json=body_json)
        if request.status_code == 200:
            response = request.json()
        else:
            response = None
        return {
            "url": url,
            "body": body_json,
            "status_code": request.status_code,
            "response": response
        }

    @staticmethod
    def deliver_order_json(order_dict, method):
        """Send POST request with order in json format to change
        to the specified delivery method

        Returns dict = {
            "url": api_url,
            "body": request_body,
            "status_code": status_code,
            "response": response_json_dict
        }
        """
        if method == "inhouse":
            url = 'http://127.0.0.1:5000/v1/orders/inhouse'
        elif method == "ubereats":
            url = 'http://127.0.0.1:5000/v1/orders/ubereats'
        else:
            raise KeyError("Must be 'inhouse' or 'ubereats'")
        request = requests.post(url, json=order_dict)
        if request.status_code == 200:
            response = request.json()
        else:
            response = None
        return {
            "url": url,
            "body": order_dict,
            "status_code": request.status_code,
            "response": response
        }

    @staticmethod
    def deliver_order_csv(order_csv):
        """Send POST request with order in csv format to change
        to the specified delivery method

        Returns dict = {
            "url": api_url,
            "body": request_body,
            "status_code": status_code,
            "response": response_json_dict
        }
        """
        url = 'http://127.0.0.1:5000/v1/orders/foodora'
        request = requests.post(url, data=order_csv)
        if request.status_code == 200:
            response = request.json()
        else:
            response = None
        return {
            "url": url,
            "body": order_csv,
            "status_code": request.status_code,
            "response": response
        }

    @staticmethod
    def get_menu(item=None):
        """Send GET request for menu
        Returns dict = {
            "url": api_url,
            "body": request_body,
            "status_code": status_code,
            "response": response_json_dict
        }
        """
        if item is None:
            url = 'http://127.0.0.1:5000/v1/resources/menu/all'
        elif item["itype"] == "topping":
            url = 'http://127.0.0.1:5000/v1/resources/menu?itype=topping&item=' \
                + item["item"]
        else:
            url = 'http://127.0.0.1:5000/v1/resources/menu?itype=' + item["itype"] \
                + '&item=' + item["item"] + '&size=' + item["size"]
        request = requests.get(url)
        if request.status_code == 200:
            response = request.json()
        else:
            response = None
        return {
            "url": url,
            "body": None,
            "status_code": request.status_code,
            "response": response
        }
