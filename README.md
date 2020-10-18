# 梧桐链CTS的Python封装

官方文档：https://lgb.wutongchain.com/file/ctsdec.pdf

### 背景 (Backgrounds)
CTS是梧桐链（同济区块链）的具象和落地应用，主要应用场景为存证，可以说是为存证领域而特制的服务。

本Python SDK属非官方SDK，但是会尽量多的保留官方SDK的哲学和思路。写本SDK因为本人非常认同梧桐链对于目前区块链落地应用的定位。本人认为在现阶段市面上大多数的区块链应用都可以用中心化的数据库解决，区块链应用场景不具有普适性，而适合用区块链解决的场景仅适用于：1. 数字货币作为价值转移工具；2.存证（利用技术手段将自证-->他证）

### 区块链浏览器
官方区块链浏览器：https://cts.wutongchain.com/ 

### Python 环境
目前受限于时间，仅在Python 3.6.9 Mac上调试，并通过100%测试覆盖率

### 安装
1. 下载本SDK
2. 

### 使用
1. 初始化对象

```
from api import CTSAPI
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

