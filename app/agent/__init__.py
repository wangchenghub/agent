from flask import Blueprint
from flask_restful import Api

from app.agent.api.api import CommResource

# 创建蓝图对象:
agent_bp = Blueprint('agent', __name__)

# 创建Api对象:
agent_api = Api(agent_bp)

# 设置json包装格式:
# agent_api.representation('application/json')(output_json)

prefix = "/api/v1"

# agent server Interface:
agent_api.add_resource(CommResource, f"{prefix}/pass/")
