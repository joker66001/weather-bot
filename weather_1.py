import requests

# 配置API Key和城市输入
API_KEY = "cf4202e738012af1ad5175429f0d02e8"  # 替换为你的实际Key
city = input("请输入城市名（英文或拼音，如Beijing/London）: ")

# 构建API请求URL（使用metric单位获取摄氏度温度）
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=zh_cn"

try:
    # 发送请求并解析JSON响应
    response = requests.get(url).json()
    
    # 检查是否请求成功
    if response["cod"] == 200:
        weather_desc = response["weather"][0]["description"]
        temperature = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        print(f"\n{city}的当前天气：")
        print(f"- 温度：{temperature}℃")
        print(f"- 天气状况：{weather_desc}")
        print(f"- 湿度：{humidity}%")
    else:
        print(f"错误：{response['message']}（代码：{response['cod']}）")

except Exception as e:
    print(f"请求失败：{e}")