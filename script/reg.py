
from settings.config import Config
from logs.log import get_logger
from script.Services import Service


LOG = get_logger(name=__name__)


def main():
    ser = Service(Config.ZENAP_MSB_SDCLIENT_IP, Config.ZENAP_MSB_SDCLIENT_PORT)
    LOG.info("=========================-Register-=========================")

    # agent http
    kwargs = {
        "serviceName": "dsmagent" + "-" + Config.POD_ID,
        "version": "v1",
        "url": "/dsmagent/v1",
        "publish_port": None,                                                 # 如果只写一个端口就是 https ，隔开就是一个https 和 http
        "protocol": "HTTP",                                                   # 协议（REST、UI、HTTP、TCP、UDP
        "nodes": [{"ip": Config.LOCAL_IP, "port": Config.AGENT_HTTP_PORT}],   # 服务实例列表 List
        "visualRange": "1"                                                    # 可见范围: 系统间:0，系统内:1，全部:0|1(默认)
    }
    code, _ = ser.reg_http(**kwargs)
    LOG.info(f"Register [Service Name:{kwargs['serviceName']}, url: {kwargs['url']}, protocol:{kwargs['protocol']}] OK:: code:{code}")

# agent internal http
    kwargs = {
        "serviceName": "dsmagent-internal" + "-" + Config.POD_ID,
        "version": "v1",
        "url": "/dsmagent/v1",
        "publish_port": f"{Config.AGENT_INTERNAL_HTTPS_PORT}|{Config.AGENT_INTERNAL_HTTP_PORT}",
        "protocol": "HTTP",                 # 协议（REST、UI、HTTP、TCP、UDP
        "nodes": [{"ip": Config.LOCAL_IP, "port": Config.AGENT_HTTP_PORT}],
        "visualRange": "0"
    }
    code, _ = ser.reg_http(**kwargs)
    LOG.info(f"Register [Service Name:{kwargs['serviceName']}, url: {kwargs['url']}, protocol:{kwargs['protocol']}] OK:: code:{code}")

# reg agent tcp
    kwargs = {
        "serviceName": "dsmagent-data" + "-" + Config.POD_ID,
        "version": "v1",
        "url": None,
        "publish_port": Config.AGENT_PUBLISH_DATA_PORT,
        "protocol": "TCP",                                                    # 协议（REST、UI、HTTP、TCP、UDP）
        "nodes": [{"ip": Config.LOCAL_IP, "port": Config.AGENT_DATA_PORT}],   # 服务实例列表 List
        "visualRange": "0"                                                    # 可见范围。系统间:0，系统内:1，全部:0|1(默认)
    }
    code, _ = ser.reg_tcp(**kwargs)
    LOG.info(f"Register [Service Name:{kwargs['serviceName']}, url: {kwargs['url']}, protocol:{kwargs['protocol']}] OK:: code:{code}")


if __name__ == "__main__":
    main()
