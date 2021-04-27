# encoding: utf-8
"""
@author: linvaux(80320949)
@contact: wutao@yeahzee.com
@time: 2020/12/7 5:36 下午
@desc: 获取token
"""

import collections
import time
from hashlib import md5
from urllib.parse import urljoin
import requests


def sso_login(username: str, password: str) -> str:
    """
    pim登陆接口，接口文档：https://doc.myoas.com/pages/viewpage.action?pageId=19076116
    Args:
        username:
        password:

    Returns:

    """
    sso_host = "https://t-ssov2.myoas.com"
    sso_api_path = "/api/user/login"
    # appid = ""
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {
        "appid": appid,
        "password": password,
        "time": int(round(time.time())),
        "username": username,
    }
    payload.update({
        "sign": __sign(sso_api_path, payload)
    })
    # print(urljoin(sso_host, sso_api_path))
    # print(headers)
    # print(payload)
    resp = requests.post(url=urljoin(sso_host, sso_api_path), headers=headers, data=payload)
    if resp.status_code == requests.codes.ok:
        # print(resp.json())
        return resp.json()['data']['sessionKey']
    else:
        raise Exception(f"{username} 获取token失败...")


def sso_ping(sessionKey: str) -> str:
    """
    token续期接口，接口文档：https://doc.myoas.com/pages/viewpage.action?pageId=19791889
    Args:
        sessionKey:
    Returns:

    """
    sso_host = "https://t-ssov2.myoas.com"
    sso_api_path = "/api/user/ping"
    # appid = "appid"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {
        "appid": appid,
        "time": int(round(time.time())),
        "sessionKey": sessionKey
    }
    payload.update({
        "sign": __sign(sso_api_path, payload)
    })

    resp = requests.post(url=urljoin(sso_host, sso_api_path), headers=headers, data=payload)
    if resp.status_code == requests.codes.ok:
        return resp.json()['data']['sessionKey']
    else:
        raise Exception(f"{sessionKey} 续期token失败...")


def sso_logout(sessionKey: str) -> int:
    """
    注销接口，接口文档：https://doc.myoas.com/pages/viewpage.action?pageId=20021331
    Args:
        sessionKey:
    Returns:

    """
    sso_host = "https://t-ssov2.myoas.com"
    sso_api_path = "/api/user/logout"
    # appid = "appid"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {
        "appid": appid,
        "time": int(round(time.time())),
        "sessionKey": sessionKey
    }
    payload.update({
        "sign": __sign(sso_api_path, payload)
    })

    resp = requests.post(url=urljoin(sso_host, sso_api_path), headers=headers, data=payload)
    if resp.status_code == requests.codes.ok:
        return resp.json()['no']
    else:
        raise Exception(f"{sessionKey} 注销token失败...")


def sso_exchange(sessionKey: str) -> str:
    """
    兑换一次性token，接口文档：https://doc.myoas.com/pages/viewpage.action?pageId=136702486
    Args:
        sessionKey:
    Returns:

    """
    sso_host = "https://t-ssov2.myoas.com"
    sso_api_path = "/api/user/token/exchange"
    # appid = "appid"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {
        "appid": appid,
        "time": int(round(time.time())),
        "sessionKey": sessionKey
    }
    payload.update({
        "sign": __sign(sso_api_path, payload)
    })

    resp = requests.post(url=urljoin(sso_host, sso_api_path), headers=headers, data=payload)
    if resp.status_code == requests.codes.ok:
        return resp.json()['data']
    else:
        raise Exception(f"{sessionKey} 兑换一次性token失败...")


def __sign(path: str, payload: dict) -> str:
    """
    请求签名，参考文档：https://doc.myoas.com/pages/viewpage.action?pageId=119426895
    Args:
        path: 请求路径
        payload: 请求参数

    Returns:

    """
    # secret = ""
    flag = "\n"
    params_list = [path]
    # 参数按照参数名升序排序
    payload_sorted = collections.OrderedDict(sorted(payload.items()))
    # 拼接参数
    list(map(lambda x: params_list.append(x[0] + "=" + str(x[1])), payload_sorted.items()))
    params_list.append(secret)
    result = f"{flag}".join(params_list)
    # print(f"待签名字符串: {result}")
    return md5(result.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    appid = "oppo-healthlab-data-center"
    secret = "1dc1431d1f6748eeabaceaaee76cd0c5"
    data = {
        "username": r"80301815",
        "password": r"Test=911"
    }
    token = sso_login(**data)
    token_ping = sso_ping(token)
    token_exchange = sso_exchange(token_ping)
    print(f"token: {token}")
    logout = sso_logout(token_exchange)
    print(f"code:{logout}")
String accessKey = "3REgcFTraVZWp5JStmUr1bESMVoZFCaDW_hlAa39";
String secretKey = "-36Si3hT5VptlFHEQy78ZkKgYlStzcwuY1m5Goz0";

AWSCredentials credentials = new BasicAWSCredentials(accessKey, secretKey);
AmazonS3Client client = new AmazonS3Client(credentials, opts);
String bucketName = "bucket-test";
String endpoint = "https://ocs-cn-south1.heytapcs.com";