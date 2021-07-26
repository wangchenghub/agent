from app import FlaskApp

from script import reg
from script import unreg


class AgentService(FlaskApp):
    def __init__(self, flask_conf):
        super().__init__(flask_conf=flask_conf, log_name="agent.log")

    def register_bp(self):
        """
        注册蓝图:
        """
        from app.agent import agent_bp
        self.app.register_blueprint(agent_bp)


service = AgentService('UserConfig')


def init():
    unreg.main()
    reg.main()
    service.create_app()
    app = service.app
    return app
