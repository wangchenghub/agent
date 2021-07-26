import json
import time
import requests
from logs.log import get_logger

LOG = get_logger(name=__name__)


class Service(object):
    def __init__(self, ip_addr, port):
        self.port = port
        self.ip_addr = ip_addr
        self.reg_url = f"http://%s:%s/api/microservices/v1/services"
        self.unreg_url = f"http://%s:%s/api/microservices/v1/services/%s/version/%s?namespace=%s"

    def request_post(self, data):
        url = self.reg_url % (self.ip_addr, self.port)
        LOG.info(f"Request:type->POST, url:{url}")
        count = 0
        resp = ""
        code = 500
        while True:  # 10秒重试一次，一直到成功
            try:
                resp = requests.post(url, json=data)
                code = resp.status_code
                body = json.loads(resp.text)
                if str(code).startswith("20"):
                    break
                count += 1
                LOG.error(f"ReTry register Count:{count}, error code:{code}")
                time.sleep(10)
            except Exception as e:
                count += 1
                LOG.error(f"ReTry register Count:{count}, error:{e}")
                time.sleep(10)
        LOG.info(f"Response: url:{self.reg_url}, code:{code}")
        return code, body

    def request_delete(self, services, version, namespace="default"):
        url = self.unreg_url % (self.ip_addr, self.port, services, version, namespace)
        LOG.info(f"Request:type->DELETE, url:{url}")
        count = 0
        while True:  # 10秒重试一次，一直到成功
            try:
                resp = requests.delete(url)
                code = resp.status_code
                LOG.info(f"Response: url:{url}, code:{code}")
                if str(code).startswith("20"):
                    break
                count += 1
                LOG.error(f"ReTry unregister Count:{count}, error code:{code}")
                time.sleep(10)
            except Exception as e:
                count += 1
                LOG.error(f"ReTry unregister Count:{count}, error:{e}")
                time.sleep(10)
        return code

    def reg_http(self, **kwargs):
        data = {
            "serviceName": kwargs.get("serviceName"),
            "version": kwargs.get("version"),
            "url": kwargs.get("url"),
            "publish_port": kwargs.get("publish_port"),
            "protocol": kwargs.get("TCP"),
            "nodes": kwargs.get("nodes"),
            "visualRange": kwargs.get("visualRange")
        }
        return self.request_post(data=data)

    def reg_tcp(self, **kwargs):
        data = {
            "serviceName": kwargs.get("serviceName"),
            "version": kwargs.get("version"),
            "url": kwargs.get("url"),
            "publish_port": kwargs.get("publish_port"),
            "protocol": kwargs.get("TCP"),
            "nodes": kwargs.get("nodes"),
            "visualRange": kwargs.get("visualRange")
        }
        return self.request_post(data=data)
