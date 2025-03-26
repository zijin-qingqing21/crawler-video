import requests

url="https://upos-sz-estgoss.bilivideo.com/upgcxcode/53/50/28715715053/28715715053-1-30120.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742969746&gen=playurlv2&os=upos&oi=0&trid=5565f523e3fc449eb041afee3a74aee9u&mid=536693128&platform=pc&og=cos&upsig=7f43daf569e99527bee55b4affaa84c5&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=7865C5AB-7DA7-9C94-6ED8-B157779E6B8059555infoc&build=0&f=u_0_0&agrr=0&bw=1365421&logo=80000000"

mc={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",'referer':"https://www.bilibili.com/video/BV1rA9jYWEv1/?spm_id_from=333.1007.tianma.23-3-89.click&vd_source=eae4d9eda0521373262af52bd3eec43a"}

res=requests.get(url,headers = mc)

open("视频.mp4","wb").write(res.content)

url="https://upos-sz-mirror08c.bilivideo.com/upgcxcode/53/50/28715715053/28715715053-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742969746&gen=playurlv2&os=08cbv&oi=0&trid=5565f523e3fc449eb041afee3a74aee9u&mid=536693128&platform=pc&og=hw&upsig=a1b6a58190d5fc26073967992401ce47&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=7865C5AB-7DA7-9C94-6ED8-B157779E6B8059555infoc&build=0&f=u_0_0&agrr=0&bw=26366&logo=80000000"

mc={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",'referer':"https://www.bilibili.com/video/BV1rA9jYWEv1/?spm_id_from=333.1007.tianma.23-3-89.click&vd_source=eae4d9eda0521373262af52bd3eec43a"}

res=requests.get(url,headers = mc)

open("音频.mp3", "wb").write(res.content)

from moviepy.editor import  *

video = VideoFileClip('视频.mp4')
audio = AudioFileClip('音频.mp3')

hc = video.set_audio(audio)
hc .write_videofile("完整.mp4")

print (res.status_code)