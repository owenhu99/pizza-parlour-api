import requests

class CLIHelper(object):
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