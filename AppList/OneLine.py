from urllib import urlopen, unquote
from urlparse import parse_qs, urlparse
youtube_watchurl="http://www.youtube.com/watch?v=NeSuirvA6UE&playnext_from=TL&videos=MS3Hq4oBj08"
video_id = "qi7Yh16dA0w"
open(video_id+'.mp4', 'wb').write(urlopen("http://www.youtube.com/get_video?video_id=%s&t=%s&fmt=18"%(video_id, parse_qs(unquote(urlopen('http://www.youtube.com/get_video_info?&video_id=' + video_id).read().decode('utf-8')))['token'][0])).read())