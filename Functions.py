import speedtest
import requests

def speedTest():
	try:
		st = speedtest.Speedtest()
		st.get_best_server()
		return [st.download()/1000000, st.upload()/1000000]
	except speedtest.ConfigRetrievalError:
		return False
		
def weather(city, country, api):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&APPID={}'.format(city, country, api)
    j = requests.get(url).json()
    return j

def websiteChecker(website):
	rawPingFile = os.popen('ping -c 1 %s' % website)
	rawPingData = rawPingFile.readlines()
	rawPingFile.close()

	if len(rawPingData) < 2:
		return False
		latency = 0
	else:
		index = rawPingData[1].find('time=')
		if index == -1:
			return False
		else:
			latency = rawPingData[1][index + 5:]
			latency = latency[:latency.find(' ')]
			return float(latency)