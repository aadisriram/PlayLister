'''
Created on Sep 20, 2012

@author: aadityasriram
'''
import json,urllib2,socket

youtubeBaseUrl = "http://gdata.youtube.com/feeds/api/videos?alt=json&q="
downloadBaseUrl = "http://projects-sushilkumar.rhcloud.com/YTGrabber?url="

def getYoutubeLink(search):
    searchMod = search.replace(" ","%20")
    searchUrl = youtubeBaseUrl + searchMod
    jsonData = urllib2.urlopen(searchUrl)
    tmp = jsonData.read()
    jsonObject = json.loads(tmp)
    return jsonObject["feed"]["entry"][0]["link"][0]["href"],jsonObject["feed"]["entry"][0]["title"]["$t"]

def getDownloadLink(youtubeLink):
    downloadUrl = downloadBaseUrl + youtubeLink
    jsonData = urllib2.urlopen(downloadUrl,None,1000000000)
    tmp = jsonData.read()
    jsonObject = json.loads(tmp)
    return jsonObject["links"][9]["link"],jsonObject["links"][9]["type"].split(" ")[0]
    
def downloadVideo(file_name,file_mode,url):
    print " Reached the download phase "
    u = urllib2.urlopen(url)
    localFile = open(file_name, 'w')
    localFile.write(u.read())
    localFile.close()

youtubeLink,songTitle = getYoutubeLink("love to love you like a love song")
print youtubeLink
print songTitle
downloadLink,fileType = getDownloadLink(youtubeLink)
print downloadLink
print fileType
downloadVideo(songTitle+"."+fileType,"",downloadLink)
