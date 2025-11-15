from datetime import datetime
ip_version_priority = "ipv4"

source_urls = [
   "https://tmxk.pp.ua/smart-cn.m3u",
   "https://raw.githubusercontent.com/Guovin/iptv-api/refs/heads/master/output/result.txt"
    #"https://raw.githubusercontent.com/xmbjm/IPTV/refs/heads/master/output/user_result.txt",
    #"http://156.238.251.122:7000",
    #"https://live.zbds.top/tv/iptv4.txt"
    #"https://live.zhoujie218.top/tv/iptv4.m3u", #ADDED BY lee  ON 2025/2/19
     #"http://156.238.251.122:888/live/live_Lite.txt",
    #"https://raw.githubusercontent.com/n3rddd/CTVLive/master/live.m3u",
    #"https://raw.githubusercontent.com/zwc456baby/iptv_alive/master/live.m3u", 
    #"https://raw.githubusercontent.com/hero1898/tv/refs/heads/main/IPTV.m3u"
   




]

url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn"
]

announcements = [
    {
        "channel": "ipv4直播",
        "entries": [
        #    {"name":"free for yourself","url":"","logo":""},
            {"name":"更新日期{placeholder}","url":"","logo":""},          
        ]
    }
]
# 获取当前日期，并格式化为YYYYMMDD

current_date = datetime.now().strftime('%Y%m%d')

 

# 替换announcements中的日期占位符

for announcement in announcements:

    for entry in announcement['entries']:

        if '更新日期{placeholder}' in entry['name']:

            entry['name'] = entry['name'].replace('{placeholder}', current_date)
            
epg_urls = [
    "https://live.fanmingming.com/e.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "http://epg.aptvapp.com/xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
