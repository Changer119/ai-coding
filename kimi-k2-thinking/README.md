# 历史上的今天

一个优雅、现代化的Web应用，帮助您探索历史上每一天发生的重要事件。

<div align="center">

![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

</div>

![Demo Screenshot](https://via.placeholder.com/800x600.png?text=历史上的今天 - Web应用截图)

## 🌟 功能特点

- 📅 **日期选择器**：默认显示当前日期，支持自定义选择任意日期
- 📚 **历史事件展示**：自动获取并展示历史上的今天发生的重大事件
- 🎯 **智能筛选**：基于重要性算法自动筛选Top 5重要事件
- 🎨 **现代化UI**：美观的渐变设计、卡片式布局、流畅动画效果
- 📱 **响应式设计**：完美适配桌面端和移动端设备
- ⚡ **无需API密钥**：使用免费的百度百科API，开箱即用
- 🌍 **中文内容**：展示中文历史事件，适合中文用户

## 🚀 快速开始

### 前置要求

- Python 3.7 或更高版本
- pip 包管理工具

### 安装步骤

1. **克隆项目到本地**

```bash
cd kimi-k2-thinking
```

2. **创建虚拟环境（推荐）**

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **安装依赖**

```bash
pip install -r requirements.txt
```

4. **启动应用**

```bash
# 方式1：使用Flask命令
flask run

# 方式2：直接运行Python脚本
python app.py
```

5. **访问应用**

打开浏览器，访问：

```
http://127.0.0.1:5000
```

您将看到「历史上的今天」Web应用界面！

## 📖 使用说明

### 基本功能

1. **查看今天的历史事件**
   - 打开应用后，默认显示当天（今日）的历史事件
   - 页面会自动加载并展示Top 5重要事件

2. **查看指定日期的历史事件**
   - 点击日期选择器
   - 选择您想要查询的日期
   - 页面将自动加载该日期的历史事件

3. **快速返回今天**
   - 点击「今天」按钮，快速跳转到当前日期

### 界面说明

- **头部区域**：显示应用标题和简介
- **日期选择区域**：包含日期选择器和「今天」按钮
- **当前日期显示**：展示当前选中的日期
- **事件展示区域**：以卡片形式展示历史事件（最多5个）

## 🛠️ 项目结构

```
kimi-k2-thinking/
├── app.py                  # Flask主应用入口
├── history_api.py          # 历史事件API模块
├── requirements.txt        # Python依赖包列表
├── templates/
│   └── index.html          # 前端页面模板
├── static/
│   ├── css/
│   │   └── style.css       # 样式文件
│   └── js/
│       └── main.js         # 前端交互逻辑（待实现）
└── README.md               # 项目说明文档
```

## 🔧 技术栈

### 后端
- **Flask** (2.3.3) - 轻量级Web框架
- **Requests** (2.31.0) - HTTP客户端库

### 前端
- HTML5 + CSS3 + JavaScript (ES6)
- Font Awesome 图标库
- Google Fonts 字体
- 响应式设计

### API
- 百度百科「历史上的今天」API（免费、无需密钥）

## ⚙️ 配置说明

### 应用配置

应用使用默认配置即可运行，无需额外配置。

如需修改，可以编辑 `app.py` 中的配置参数：

```python
# 修改端口
app.run(port=8000)

# 修改主机地址
app.run(host='0.0.0.0', port=5000)

# 关闭调试模式（生产环境）
app.run(debug=False)
```

### 生产环境部署

推荐使用 `gunicorn` 或 `uwsgi` 部署到生产环境：

```bash
# 安装gunicorn
pip install gunicorn

# 启动应用
gunicorn app:app -b 0.0.0.0:5000
```

## 🎨 自定义样式

应用采用模块化CSS设计，您可以通过修改 `static/css/style.css` 自定义样式：

- **颜色主题**：修改CSS变量（:root选择器中的变量）
- **布局样式**：修改各个组件的样式规则
- **动画效果**：修改transition和animation属性

### 示例：自定义主题色

```css
:root {
    --primary-color: #3b82f6;    /* 蓝色 */
    --secondary-color: #8b5cf6;  /* 紫色 */
    --accent-color: #ec4899;     /* 粉色 */
}
```

## 📊 事件重要性算法

应用使用智能算法筛选Top 5重要事件，评分标准如下：

| 评分维度 | 权重规则 |
|---------|---------|
| **年份** | 1900年以后：100分<br>1800-1900年：80分<br>1500-1800年：60分<br>1500年以前：40分 |
| **标题长度** | 10-50字：20分<br>50字以上：15分<br>10字以下：10分 |
| **描述长度** | 100字以上：25分<br>50-100字：20分<br>50字以下：15分 |

算法自动按照总分排序，选择前5个事件展示。

## 🐛 故障排查

### 常见问题

**问题1：无法启动应用**
- 检查Python版本是否≥3.7
- 检查是否安装了所有依赖：`pip install -r requirements.txt`
- 检查端口5000是否被占用

**问题2：无法获取历史事件**
- 检查网络连接是否正常
- 确认能否访问 `baike.baidu.com`
- 查看终端错误日志

**问题3：页面样式错乱**
- 清除浏览器缓存
- 检查浏览器控制台是否有错误
- 确认静态文件路径正确

### 日志查看

应用运行时的日志会输出到终端，可以通过日志信息排查问题：

```bash
# 启动应用时查看日志
python app.py
```

## 📝 开发计划

### 已实现功能
- ✅ 基础Web应用框架
- ✅ 历史事件API接口
- ✅ 日期选择器
- ✅ 事件展示卡片
- ✅ 响应式设计
- ✅ 美观的UI样式

### 待实现功能
- ⏳ 前端JavaScript交互逻辑
- ⏳ 加载动画优化
- ⏳ 事件搜索功能
- ⏳ 事件详情页
- ⏳ 收藏功能
- ⏳ 分享功能
- ⏳ 更多数据源API

如您有兴趣参与开发，欢迎提交PR！

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📄 许可证

本项目基于MIT许可证开源，详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- [Flask](https://flask.palletsprojects.com/) - 优秀的Python Web框架
- [百度百科](https://baike.baidu.com/) - 提供历史事件数据
- [Font Awesome](https://fontawesome.com/) - 提供精美的图标
- [Google Fonts](https://fonts.google.com/) - 提供优雅的中文字体

## 📧 联系信息

如有问题或建议，请通过以下方式联系：

- 提交Issue到GitHub仓库
- 发送邮件至：your-email@example.com

## 🌐 相关链接

- [项目主页](https://github.com/your-username/kimi-k2-thinking)
- [在线演示](https://your-demo-url.com)（如有）
- [API文档](https://github.com/your-username/kimi-k2-thinking/wiki)（开发中）

---

<div align="center">

**感谢您的使用！** ⭐

如果您觉得这个项目有用，请给个Star吧！

</div>
