import Functions
import blinkts
import os

BASESPEED = 10
weatherAPI = "f0ecf01eae9884d6fa621352cb187b36"

blinkt.set_clear_on_exit(False)
speedtest = Functions.speedTest()
if speedtest == False:
	blinkt.set_pixel(6, 0, 0, 255)
	blinkt.set_pixel(7, 0, 0, 255)
else
	for i in range(len(speedtest)):
		green = speedtest[i]/BASESPEED*255

		if green > 255:
			green = 255
		red = 255-green

		blinkt.set_pixel(6+i, red, green, 0)
		
weather = Functions.weather("Kirkby", "UK", weatherAPI)
weatherMain = weather["weather"]["main"]

if weatherMain == "Clear":
	r, g, b, w = 255, 25, 0, .5
elif weatherMain == "Clouds" or weatherMain == "Atmosphere":
	r, g, b, w = 5, 5, 5, 1
elif weatherMain == "Snow":
	r, g, b, w = 255, 255, 255, .5
elif weatherMain == "Rain":
	r, g, b, w = 0, 0, 355, .5
elif weatherMain == "Drizzle":
	r, g, b, w = 0, 128, 255, .5
elif weatherMain == "Thunderstorms":
	r, g, b, w = 32, 0, 196, .5
else:
	r, g, b, w = 0, 0, 0, 0
	f = open("Uncaught.txt","w+")
	f.writelines(weatherMain)
	f.close()

blinkt.set_pixel(r, g, b, w)
	
ckplWebsite = Functions.websiteChecker("www.cpope.uk")
if ckplWebsite == False:
    blinkt.set_pixel(5, 0, 0, 255)
    blinkt.show()
else:
    green = ckplWebsite/100*255
    if green > 255:
        green = 255
    red = 255-green

    blinkt.set_pixel(5, red, green, 0)

blinkt.show()