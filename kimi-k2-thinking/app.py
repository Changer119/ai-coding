#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
历史上的今天 - Flask Web应用
前端使用日期选择器，后端调用API获取历史事件
"""

from flask import Flask, render_template, jsonify, request
from history_api import HistoryAPI
from datetime import datetime
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 确保JSON正确显示中文

# 初始化历史事件API
history_api = HistoryAPI()


@app.route('/')
def index():
    """
    主页路由
    渲染前端页面
    """
    # 获取当天的历史事件作为初始数据
    today_events = history_api.get_today_events()

    return render_template('index.html', events=today_events)


@app.route('/api/events', methods=['GET'])
def get_events():
    """
    API路由：获取指定日期的历史事件

    请求参数：
        - month: 月份 (1-12)
        - day: 日期 (1-31)

    返回：
        JSON格式的历史事件列表
    """
    try:
        month = request.args.get('month', type=int)
        day = request.args.get('day', type=int)

        # 参数验证
        if not month or not day:
            return jsonify({'error': '请提供月份和日期参数'}), 400

        if not (1 <= month <= 12):
            return jsonify({'error': '月份必须在1-12之间'}), 400

        if not (1 <= day <= 31):
            return jsonify({'error': '日期必须在1-31之间'}), 400

        # 获取历史事件
        events = history_api.get_events(month, day)

        if events is None:
            return jsonify({'error': '获取历史事件失败，请稍后重试'}), 500

        return jsonify({
            'success': True,
            'data': events,
            'date': f"{month}月{day}日"
        })

    except Exception as e:
        print(f"API错误: {e}")
        return jsonify({'error': '服务器内部错误'}), 500


@app.route('/api/today')
def get_today():
    """
    API路由：获取当天的历史事件

    返回：
        JSON格式的历史事件列表
    """
    try:
        events = history_api.get_today_events()

        if events is None:
            return jsonify({'error': '获取历史事件失败'}), 500

        today = datetime.now()

        return jsonify({
            'success': True,
            'data': events,
            'date': f"{today.month}月{today.day}日"
        })

    except Exception as e:
        print(f"API错误: {e}")
        return jsonify({'error': '服务器内部错误'}), 500


# 错误处理
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': '页面不存在'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': '服务器内部错误'}), 500


if __name__ == '__main__':
    # 开发环境配置
    import os
    port = int(os.environ.get('PORT', 5001))  # 默认使用5001端口
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True
    )
