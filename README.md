# 说明
* speedtest.cn申请的收费提速服务和当前IP是绑定的，如果IP变更，需要重新访问speedtest.cn来绑定当前新IP来获得提速体验。
* 本脚本将实现自动判断当前外网IP是否变更，如果变更就重新调用speedtest.cn的API来对新的IP绑定提速服务。
* 使用时需要定时调用该脚本，如果是linux的话可以放在crontab中定时调用。

# 环境
* Python3+requests
