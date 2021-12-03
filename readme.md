# 项目描述
appium自动化测试框架

# 配置环境准备
- python  3.8.3
- appium   v1.21.1
- nodejs  v14.17.3  
- jdk      v"1.8.0_05"
- sdk      1.0.41  

# 依赖包
-appium服务端
>npm install -g appium@1.21.1(可以去网上找镜像地址，
> 源地址下载较慢。注意！！服务端版本需要和客户端版本匹配) 

-appium client包下载
>pip install appium-python-client

-发送邮件库文件下载
>直接网上下载，BSTestRunner.py，完成后把文件放入python3
> 目录的lib文件中

-yaml文件库下载
>pip install pyyaml

-日志文件在config文件中，如果需要改动日志存放位置和读取模式更改，更改一下配置就好。
图片在文件中

#执行用例
1.首先启动批处理文件appium_start.bat，打开appium服务
2.cmd进入工程目录下的test_run目录中，输入命令python run.py执行全部test_case用例

#注意事项

