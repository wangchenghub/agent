import time
from settings.config import Config
from logs.log import get_logger
from script.Services import Service

LOG = get_logger(name=__name__)


def main():
    zenap_msb_sdclient_ip = Config.ZENAP_MSB_SDCLIENT_IP
    zenap_msb_sdclient_port = Config.ZENAP_MSB_SDCLIENT_PORT
    ser = Service(zenap_msb_sdclient_ip, zenap_msb_sdclient_port)

    LOG.info("========================-UnRegister-========================")
    ser.request_delete(services=f"dsmagent-{Config.POD_ID}", version="v1")
    ser.request_delete(services=f"dsmagent-internal-{Config.POD_ID}", version="v1")
    ser.request_delete(services=f"dsmagent-data-{Config.POD_ID}", version="v1")


if __name__ == "__main__":
    main()
