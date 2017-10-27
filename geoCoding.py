
import httplib2
import json


def getGeocoderLocation(inputString):
	googleApiKey = "AIzaSyAIrQBRrd5Xrfb_ngtYv4aOWs5zCf8CnWI"
	locationString = inputString.replace(" ","+")
	url =  "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}".format(locationString,googleApiKey)
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	return result

def printLatLong(result):
	lat =  result['results'][0]['geometry']['location']['lat']
	lng =  result['results'][0]['geometry']['location']['lng']
	formatedAddress = result['results'][0]['formatted_address']
	return (lat,lng,formatedAddress)

if __name__ == '__main__':
	

	#print printLatLong(getGeocoderLocation("Tokyo Japan"))
	listPlaces = ["Tokyo Japan", "Jakarta, Indonesia", "Maputo Mozambique", " Geneva, Switzerland", "Los Angeles California Usa"]
	print [printLatLong(getGeocoderLocation(x)) for x in listPlaces ]
