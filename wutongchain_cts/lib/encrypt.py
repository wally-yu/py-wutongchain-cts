import datetime
import hmac
import base64
import requests
import hashlib
from urllib.parse import quote

# ---------------- Configuration Area ---------------------
API_HOST = 'https://cts-api.wutongchain.com'
# ---------------- END OF Configuration Area --------------

def _hmac_sha1(key, msg):
    raw = msg.encode("utf-8")
    key = key.encode('utf-8')
    hashed = hmac.new(key, raw, hashlib.sha1)
    return base64.encodebytes(hashed.digest()).decode('utf-8')


def wutong_requests(app_id, end_point_uri, request_method, args_dict, secret_key):
    """ compose wutong CTS API communication as per offical doc """

    # generate time stamp
    now = datetime.datetime.now()
    current_time_stamp = round(now.timestamp()*1000)  # precise to micro sec

    # compose header as per official doc
    headers = {'Content-type': 'application/json',
               'charset': 'UTF-8',
               'timestamp': str(current_time_stamp)}

    # calculate token
    sorted_vals_li = [args_dict[elem] for elem in sorted(args_dict.keys())]
    combined_msg = ''.join(sorted_vals_li) + str(current_time_stamp)
    token = _hmac_sha1(key=secret_key, msg=combined_msg).strip()
    token = quote(token, safe='')

    # compose url
    uri_paras = 'appid=%s&token=%s' % (app_id, token)
    for key, val in args_dict.items():
        uri_paras += '&%s=%s' % (key, val)

    uri = '%s%s?%s' % (API_HOST, end_point_uri, uri_paras)

    # send request
    if request_method == 'get':
        ret = requests.get(url=uri, headers=headers)
    elif request_method == 'post':
        ret = requests.post(url=uri, headers=headers)
    else:
        raise Exception('request method not correct')
    return ret
