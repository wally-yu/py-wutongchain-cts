app_id = "your_app_id"
secret_key = 'your_secret_key'

from wutongchain_cts.api import CTSAPI
cts_instance = CTSAPI(app_id=app_id, secret_key=secret_key)

# 查询目前链的区块高度
# print(cts_instance.get_height().json())

# 按区块高度获取区块详情
# print(cts_instance.get_block_detail_by_height(height=2).json())

# 按区块哈希获取区块详情
# print(cts_instance.get_block_detail_by_hash(hash_code='pl+yAjHm9YRo4/rG9+qSOx+IzM2wImNlm8+/rLQ99xw=').json())

# 创建存证
# data = 'test/ 测试内容'
# business_id = '12345678'
# print(cts_instance.put_data(data=data, business_id=business_id).json())

# 获取存证
# print(cts_instance.get_data('j59tp5gCuXh2HZqFyKYGFat7I3VZYKwAxeUC132l9yk=').json())
