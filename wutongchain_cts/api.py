from wutongchain_cts.lib.encrypt import wutong_requests

REQUEST_METHOD_GET = 'get'
REQUEST_METHOD_POST = 'post'

class CTSAPI():
    def __init__(self, app_id, secret_key):
        """
        存证平台服务会对每个访问请求进行身份验证，通过 appid 和 secretkey（用户密钥）来验证请求的发送者身份。appid 和 secretkey 由存证平台颁发给访问者。
        """
        self.app_id = app_id
        self.secret_key = secret_key


    def get_height(self):
        endpoint_uri = '/chain/getHeight'
        response = self._send_request(end_point_uri=endpoint_uri,
                                      request_method=REQUEST_METHOD_GET,
                                      args_dict={},)
        return response

    def get_block_detail_by_height(self, height):
        endpoint_uri = '/block/getDetailByHeight'
        response = self._send_request(end_point_uri=endpoint_uri,
                                      request_method=REQUEST_METHOD_GET,
                                      args_dict={'height': str(height)})
        return response

    def get_block_detail_by_hash(self, hash_code):
        endpoint_uri = '/block/getDetailByHash'
        # hash_code = quote(hash_code, safe='')
        response = self._send_request(end_point_uri=endpoint_uri,
                                      request_method=REQUEST_METHOD_GET,
                                      args_dict={'hash': hash_code})
        return response

    def put_data(self, data, business_id):
        endpoint_uri = '/store/create'
        # data = quote(data, safe='')
        response = self._send_request(end_point_uri=endpoint_uri,
                                      request_method=REQUEST_METHOD_POST,
                                      args_dict={'data': data,
                                                 'businessId': business_id})
        return response

    def get_data(self, hash_code):
        endpoint_uri = '/store/get'
        # hash_code = quote(hash_code, safe='')
        response = self._send_request(end_point_uri=endpoint_uri,
                                      request_method=REQUEST_METHOD_GET,
                                      args_dict={'hash': hash_code})
        return response

    def _send_request(self, end_point_uri, request_method, args_dict):
        ret = wutong_requests(app_id=self.app_id,
                              secret_key=self.secret_key,
                              end_point_uri=end_point_uri,
                              request_method=request_method,
                              args_dict=args_dict,
                              )
        return ret  # return a response obj
