__author__ = 'Matthijs'

import sys, getopt
import urllib, json

class BusTime:

    def __init__(self, city, busstop):
        self.city = city
        self.busstop = busstop


    def Run(self):

        url = "https://api.9292.nl/0.1/locations/" + self.city + "/bushalte-" + self.busstop + "/departure-times" + "?lang=nl-NL"
        #/0.1/locations/hendrik-ido-ambacht/bushalte-appelgaarde/departure-times
        print url
        response = urllib.urlopen(url);
        data = json.loads(response.read())



        for item in data['tabs'][0]['departures']:
            print item['service'] + ' Richting: ' + item['destinationName'] + ', Tijd: ' + item['time'] + ' (' + item['realtimeState'] + ') '

        print 'Terminated'



def main(argv):
    city = ''
    busStop = ''

    try:
        opts, args = getopt.getopt(argv,"hc:b:",["city=","busstop="])
    except getopt.GetoptError:
        print 'BusTime.py -c <city> -b <busstop>'
        sys.exit(2)
    for opt, arg in opts:
        if opt ==  '-h':
            print 'BusTime.py -c <city> -b <busstop>'
        elif opt in ("-c", "--city"):
            city = arg
        elif opt in ("-b", "--busstop"):
            busStop = arg


    busTime = BusTime(city, busStop)
    busTime.Run();

if __name__ == "__main__":
   main(sys.argv[1:])
