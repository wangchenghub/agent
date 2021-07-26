from flask import jsonify

from app.agent.manager import init

app = init()


@app.route('/')
def route_map():
    """
    定义根路由: 获取所有路由规则
    """
    return jsonify({rule.endpoint: rule.rule for rule in app.url_map.iter_rules()})
