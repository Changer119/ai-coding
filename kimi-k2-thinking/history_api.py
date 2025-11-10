#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
历史上的今天API模块
调用百度百科API获取历史事件数据
"""

import requests
import json
from datetime import datetime
from typing import List, Dict, Optional


class HistoryAPI:
    """历史事件API接口类"""

    def __init__(self):
        self.base_url = "https://baike.baidu.com/cms/home/eventsOnHistory"

    def get_events(self, month: int, day: int) -> Optional[List[Dict]]:
        """
        获取指定日期的历史事件

        Args:
            month: 月份 (1-12)
            day: 日期 (1-31)

        Returns:
            历史事件列表，按重要性排序
        """
        try:
            # 格式化月份为两位数
            month_str = f"{month:02d}"

            # 请求API获取整月数据
            url = f"{self.base_url}/{month_str}.json"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            # 解析指定日期的数据
            # API返回的日期键格式是 "MMDD"（如 "1130" 表示11月30日）
            day_key = f"{month:02d}{day:02d}"
            if month_str in data and day_key in data[month_str]:
                events_data = data[month_str][day_key]
                return self._process_events(events_data)
            else:
                return []

        except Exception as e:
            print(f"获取历史事件失败: {e}")
            return None

    def _process_events(self, events_data: List[Dict]) -> List[Dict]:
        """
        处理原始事件数据，提取重要信息并排序

        Args:
            events_data: 原始事件数据

        Returns:
            按重要性排序的事件列表（取前5个）
        """
        processed_events = []

        for event in events_data:
            # 提取关键信息
            year = event.get('year', '')
            title = event.get('title', '')
            desc = event.get('desc', '')

            if year and title:
                # 计算重要性分数
                importance_score = self._calculate_importance(year, title, desc)

                processed_events.append({
                    'year': int(year) if year.isdigit() else 0,
                    'title': self._clean_text(title),
                    'desc': self._clean_text(desc),
                    'importance_score': importance_score
                })

        # 按重要性分数排序（取前5个）
        processed_events.sort(key=lambda x: x['importance_score'], reverse=True)

        return processed_events[:5]

    def _calculate_importance(self, year: str, title: str, desc: str) -> float:
        """
        计算事件重要性分数

        评分标准：
        - 年份：年份越近，分数越高（近代史更重要）
        - 标题长度：标题越长，可能包含更多信息
        - 描述长度：描述越长，事件越详细

        Args:
            year: 年份
            title: 标题
            desc: 描述

        Returns:
            重要性分数
        """
        score = 0.0

        # 年份权重（近代史权重更高）
        if year.isdigit():
            year_num = int(year)
            if year_num >= 1900:
                score += 100  # 1900年以后的事件权重高
            elif year_num >= 1800:
                score += 80
            elif year_num >= 1500:
                score += 60
            else:
                score += 40
        else:
            score += 30

        # 标题长度权重（控制在合理范围）
        title_len = len(title)
        if 10 <= title_len <= 50:
            score += 20
        elif title_len > 50:
            score += 15
        else:
            score += 10

        # 描述长度权重
        desc_len = len(desc)
        if desc_len > 100:
            score += 25
        elif desc_len > 50:
            score += 20
        else:
            score += 15

        return score

    def _clean_text(self, text: str) -> str:
        """
        清理文本中的HTML标签和特殊字符

        Args:
            text: 原始文本

        Returns:
            清理后的文本
        """
        if not text:
            return ""

        # 移除HTML标签
        import re
        clean_text = re.sub(r'<[^>]+>', '', text)

        # 移除多余空格
        clean_text = re.sub(r'\s+', ' ', clean_text)

        # 移除首尾空格
        return clean_text.strip()

    def get_today_events(self) -> Optional[List[Dict]]:
        """
        获取当天的历史事件

        Returns:
            当天的历史事件列表
        """
        today = datetime.now()
        return self.get_events(today.month, today.day)


def main():
    """测试函数"""
    api = HistoryAPI()

    # 测试获取今天的历史事件
    print("获取今天的历史事件...")
    events = api.get_today_events()

    if events:
        print(f"\n找到 {len(events)} 个重要事件：")
        for i, event in enumerate(events, 1):
            print(f"\n{i}. {event['year']}年 - {event['title']}")
            print(f"   {event['desc']}")
            print(f"   重要性分数: {event['importance_score']}")
    else:
        print("未能获取历史事件数据")

    # 测试指定日期
    print("\n\n测试指定日期 (7月1日)...")
    events = api.get_events(7, 1)

    if events:
        print(f"\n找到 {len(events)} 个重要事件：")
        for i, event in enumerate(events, 1):
            print(f"\n{i}. {event['year']}年 - {event['title']}")
            print(f"   {event['desc']}")
    else:
        print("未能获取历史事件数据")


if __name__ == '__main__':
    main()
