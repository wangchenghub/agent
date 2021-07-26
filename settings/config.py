import os
import socket
import logging
ENVIRON = os.environ


class DefaultConfig:
    """
    默认配置
    """
    pass


class Config(DefaultConfig):
    """
    server conf
    """
    # log输出等级：
    LOG_PRINT_HANDLER = logging.DEBUG
    LOG_PRINT_CONSOLE = logging.DEBUG

    # dsm sync 配置文件：
    DSM_SYNC_CONF_PATH = "/var/dsmagent/"

    # log 日志存放路径
    LOG_PATH = ENVIRON.get("LOG_PATH", "/var/log/")

    # pod id
    POD_ID = ENVIRON.get("POD_ID", socket.gethostname())

    # 本地 ip
    LOCAL_IP = ENVIRON.get("LOCAL_IP", "0.0.0.0")

    # 服务发现 host
    ZENAP_MSB_SDCLIENT_IP = ENVIRON.get("ZENAP_MSB_SDCLIENT_IP", "172.16.200.43")

    # 服务发现 端口
    ZENAP_MSB_SDCLIENT_PORT = ENVIRON.get("ZENAP_MSB_SDCLIENT_PORT", 8082)

    # 系统内：信令 端口
    AGENT_HTTP_PORT = ENVIRON.get("AGENT_HTTP_PORT", 8900)

    # 系统内：数据 端口
    AGENT_DATA_PORT = ENVIRON.get("AGENT_DATA_PORT", None)

    # 系统间：数据 端口
    AGENT_PUBLISH_DATA_PORT = ENVIRON.get("AGENT_PUBLISH_DATA_PORT", None)

    # 系统间：信令 端口
    AGENT_INTERNAL_HTTP_PORT = ENVIRON.get("AGENT_INTERNAL_HTTP_PORT", None)

    # 系统间：信令 https 端口
    AGENT_INTERNAL_HTTPS_PORT = ENVIRON.get("AGENT_INTERNAL_HTTPS_PORT", None)


config_dict = {
    "Default": DefaultConfig,
    "UserConfig": Config,
}