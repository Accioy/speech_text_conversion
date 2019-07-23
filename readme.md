# 说明

一个简单的语音文字互转的demo

使用了百度AI开放平台的免费在线API（需要百度AI平台账号，可免费注册或使用百度帐号直接登录

## 1. 关于云端接口

本语音控制工具调用了百度语音的云服务的语音识别与合成python免费接口：

https://ai.baidu.com/docs#/ASR-Online-Python-SDK/top

https://ai.baidu.com/docs#/TTS-Online-Python-SDK/top



## 2. 环境要求

windows，python3.5

安装百度语音API，见上述[链接](https://ai.baidu.com/docs#/ASR-Online-Python-SDK/top)

在[这里](https://console.bce.baidu.com/ai/?fromai=1#/ai/speech/overview/index)创建应用，复制AppID，API Key，Secret Key并填入代码对应位置中

第三方库：pyaudio，playsound。在python环境使用pip install命令安装即可。

注意：需要对playsound库的源码line34-43进行修改，添加`winCommand('close', alias)`：

```python
alias = 'playsound_' + str(random())
winCommand('open "' + sound + '" alias', alias)
winCommand('set', alias, 'time format milliseconds')
durationInMS = winCommand('status', alias, 'length')
winCommand('play', alias, 'from 0 to', durationInMS.decode())
if block:
	sleep(float(durationInMS) / 1000.0)
#此处添加
winCommand('close', alias)
```



