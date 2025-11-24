import aster.lib.utils
from aster.lib.utils import check_required_parameter


def new_listen_key(self):
    """
    Creates a new ListenKey (USER_STREAM).

    :API endpoint: ``POST /fapi/v1/listenKey``
    :API doc: https://github.com/asterdex/api-docs/blob/master/aster-finance-api.md#start-user-data-stream-user_stream
    :returns: API response containing the new listenKey.
    """

    url_path = "/fapi/v1/listenKey"
    # The POST request is typically empty for creating a new key.
    return self.send_request("POST", url_path)


def renew_listen_key(self, listenKey: str):
    """
    Pings the server to keep a ListenKey alive (USER_STREAM).

    :API endpoint: ``PUT /fapi/v1/listenKey``
    :API doc: https://github.com/asterdex/api-docs/blob/master/-finance-api.md#keepalive-user-data-stream-user_stream
    :param listenKey: The ListenKey to renew.
    :returns: API response indicating success.
    """
    
    # Ensure the key is provided before making the request
    check_required_parameter(listenKey, "listenKey")
    
    url_path = "/fapi/v1/listenKey"
    # The PUT request requires the listenKey as a parameter.
    return self.send_request("PUT", url_path, {"listenKey": listenKey})


def close_listen_key(self, listenKey: str):
    """
    Closes and invalidates a ListenKey (USER_STREAM).

    :API endpoint: ``DELETE /fapi/v1/listenKey``
    :API doc: https://github.com/asterdex/api-docs/blob/master/aster-finance-api.md#close-user-data-stream-user_stream
    :param listenKey: The ListenKey to close.
    :returns: API response indicating success.
    """
    
    # [FIX] Added parameter check for consistency and robustness
    check_required_parameter(listenKey, "listenKey")
    
    url_path = "/fapi/v1/listenKey"
    # [FIX] The DELETE request requires the listenKey to specify which stream to close.
    return self.send_request("DELETE", url_path, {"listenKey": listenKey})
