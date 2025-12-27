#!/bin/bash
# 1. 进入项目目录 (路径一定要对！)
cd /Users/zhang/PycharmProjects/PythonProject/课程作业-代码文件

echo "=================================================="
echo "正在启动舆情分析后端..."
echo "请不要关闭此窗口！"
echo "如果出现 ModuleNotFoundError，说明Python路径不对。"
echo "=================================================="

# 2. 在后台静默打开浏览器 (延迟3秒，给服务器一点启动时间)
(sleep 4 && open http://127.0.0.1:8080) &

# 3. 启动服务器 (使用绝对路径！)
# 将下面的 /Users/.../python 换成你刚才在 PyCharm 里 'which python' 查到的那个路径
/Users/zhang/PycharmProjects/PythonProject/.venv/bin/python server.py