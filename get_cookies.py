import time
import pickle
from selenium import webdriver
# 导入 Service 对象
from selenium.webdriver.chrome.service import Service

# 你的 ChromeDriver 路径
driver_path = '/Users/zhang/Documents/项目工具/chromedriver-mac-arm64/chromedriver'

# 1. 创建一个 Service 对象，传入路径
service = Service(executable_path=driver_path)

# 2. 将 service 对象传递给 webdriver.Chrome
#    注意：不再使用 executable_path=...
try:
    driver = webdriver.Chrome(service=service)
except Exception as e:
    print(f"启动 WebDriver 时出错: {e}")
    print("--- 常见错误排查 ---")
    print("1. 请确保你的 chromedriver 版本与 Chrome 浏览器版本一致。")
    print("2. [macOS用户] 请检查是否已允许执行 chromedriver (见下方说明)。")
    exit()


driver.get("https://weibo.com")
print("请在 60 秒内手动登录微博...")
time.sleep(60) # 给你充足的时间扫码或输入账号密码

# 登录成功后，获取 cookies
cookies = driver.get_cookies()

# 保存 cookies 到文件
with open("weibo_cookies.pkl", "wb") as f:
    pickle.dump(cookies, f)

print("Cookies 已成功保存到 weibo_cookies.pkl")
print("Cookies为:",cookies)
driver.quit()