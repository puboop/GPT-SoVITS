# 声音克隆
项目地址：https://github.com/RVC-Boss/GPT-SoVITS

使用方法：[查看视频](course/使用方法.mp4)

官方文档地址：https://www.yuque.com/baicaigongchang1145haoyuangong/ib3g1e

整合包0217：https://www.icloud.com.cn/iclouddrive/061bfkcVJcBfsMfLF5R2XKdTQ#GPT-SoVITS-beta0217
 
整合包0306fix2：https://www.icloud.com.cn/iclouddrive/09aaTLf96aa92dbLe0fPNM5CQ#GPT-SoVITS-beta0306fix2

安装依赖需要c++编译环境：https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/

# 依赖模型

达摩院语音团队中文标点模型：https://github.com/alibaba-damo-academy/FunASR

FRCRN语音降噪模型是基于频率循环 CRN (FRCRN) 新框架开发出来的

# 报错
含有zipfile.BadZipFile: File is not a zip或者LookupError：以及红色 >>> import nltk:
```text
#下载 "https://www.icloud.com/iclouddrive/0b9blkIrl2rOabOqyksasY2dQ#nltk_data"
#文件，解压替换本地nltk_data文件夹，若无此文件夹，放到用户名根目录下~/
或则在: `依赖/nltk_data.zip`也是有的。
```
