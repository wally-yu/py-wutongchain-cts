# 梧桐链CTS的Python封装 SDK

官方文档：https://lgb.wutongchain.com/file/ctsdec.pdf

### 背景 (Backgrounds)
CTS是梧桐链（同济区块链）的轻量级独立服务，主要应用场景为存证，可以说是为存证领域而特制的，便于使用的API和服务。方便对区块链本身不熟悉、但适合使用区块链做存证的场景进行方便、高效对接现有业务；

### 区块链浏览器
官方区块链浏览器：https://cts.wutongchain.com/ 

### Python 环境
受限于时间，仅在Python 3.6.9 Mac上调试，并通过100%测试覆盖率

### 安装
```pip3 install wutongchain-cts```

### 使用
1. 初始化对象

```
from wutongchain-cts import CTSAPI
cts_instance = CTSAPI(app_id="your_app_id", secret_key="your_secret_key")
```
++*注：存证平台服务会对每个访问请求进行身份验证，通过 appid 和 secretkey（用户密钥）来验证请求的发送者身份。appid 和 secretkey 由存证平台颁发给访问者。*++

2. 调用类方法实现不同功能，可以通过 [详细示例代码.py](https://github.com/wally-yu/py-wutongchain-cts/blob/main/test.py) 参考

示例：

---

#### 查询目前链的区块高度
- 调用方法：

```
cts_instance.get_height()
```
- 输入参数：无
- 返回：目前链的区块高度
 
- 预期返回示例：
```
{'code': 200, 'data': {'height': 80}, 'msg': ''}
```
---

#### 按区块高度获取区块详情
- 说明：

通过区块高度来查询获取到区块的详细信息，如区块哈希，前一区块哈希，交易哈希等内容。

- 调用方法：

```
cts_instance.get_block_detail_by_height(<height>)
```
- 输入参数：

height: 所需查找的区块高度

- 预期返回：

```
{
  "code": 200,
  "data": {
    "data": {
      "header": {
        "version": 1,
        "height": 2,
        "timestamp": 1601450330,
        "blockHash": "pl+yAjHm9YRo4/rG9+qSOx+IzM2wImNlm8+/rLQ99xw=",
        "previousHash": "Ep7j7pDgg2/Brnvjcv5vQ8+NFuN40GeK1UQK1gqwUJA=",
        "worldStateRoot": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
        "transactionRoot": "fArdOmAKt7jygo4dKrrnrkPuMxW4cwP1Goqfwzg/D30="
      },
      "txs": [
        "veN+LAbEXz6P3GE2ldYtTbFRZE0KtKo4jylc+CuJudg="
      ],
      "extra": "eyJtaW5lciI6IlFtYTlMNU42ZW5Kck5GYmRGQnhXaURhWHBUUnhSRlVRWUxnMWt6NEhMRnRlZW8ifQ==",
      "raw": "AQAAAAIAAAAAAAAA9srg3XQBAAAgAAAAEp7j7pDgg2/Brnvjcv5vQ8+NFuN40GeK1UQK1gqwUJAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAfArdOmAKt7jygo4dKrrnrkPuMxW4cwP1Goqfwzg/D306AAAAeyJtaW5lciI6IlFtYTlMNU42ZW5Kck5GYmRGQnhXaURhWHBUUnhSRlVRWUxnMWt6NEhMRnRlZW8ifQ=="
    }
  },
  "msg": ""
}
```
![image](http://static.hoopsign.com/cts_chain_getDetailByHeight.png)

---

#### 按区块哈希获取区块详情

- 说明：

通过区块哈希来查询获取到区块的详细信息，如区块哈希，前一区块哈希，交易哈希等内容
- 调用方法：

```
cts_instance.get_block_detail_by_hash(<hash>)
```
- 输入参数：

hash: 区块哈希

- 预期返回：(同上返回)

---

#### 创建存证

- 说明：

创建存证内容，并返回哈希值和是否成功创建
- 调用方法：

```
data = 'test/ 测试内容 _by_wally'
business_id = '12345678'
print(cts_instance.put_data(data=data, business_id=business_id).json())
```

- 输入参数：

data: 存证内容

businessId: 用户应用中的业务 id，长度不超过 64

- 预期返回：

```
{'code': 200, 'data': {'Figure': 'KZXP53J1Pp9N8xbEelGJ99GnVYSy3rynJKtXKer1AaU=', 'OK': True}, 'msg': ''}
```

![image](http://static.hoopsign.com/cts_chain_create.png)

注：偶尔会发生如下情况：

```
{'code': 500, 'data': '', 'msg': {'requestId': '4158a50d-f0ef-4f13-9e10-00d52376ee6c', 'code': 'ETIMEDOUT', 'message': 'Internal Server Error'}}
```
或：

```
{'code': 500, 'data': '', 'msg': {'requestId': '002792c0-18f4-461e-bb32-d92ef878f7f9', 'code': 'ECONNREFUSED', 'message': '服务器开小差了，请稍后再试'}}
```
以上情况需要开发者做好容错处理

---

#### 获取存证

- 说明：

通过创建存证交易返回的哈希值来获取到该存证交易所在区块的高度和存证内容

- 调用方法：

```
cts_instance.get_data('KZXP53J1Pp9N8xbEelGJ99GnVYSy3rynJKtXKer1AaU=')
```
- 输入参数：

hash: 通过创建存证交易返回的哈希

- 预期返回：

```
{'code': 200, 'data': {'data': 'test/ 测试内容 _by_wally', 'businessId': '12345678', 'blockHeight': 90, 'timestamp': 1603097791}, 'msg': ''}
```
![image](http://static.hoopsign.com/cts_chain_query1.png)
![image](http://static.hoopsign.com/cts_chain_query2.png)
---

### 技术交流
![image](http://static.hoopsign.com/wally_wechat_qr_code.jpeg?imageslim&imageView2/3/w/100)

### 开源许可
本代码永久遵循MIT License许可，允许个人和商业用途

