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

        from lxml import etree

        root = etree.Element('schedule')

        for item in data['tabs'][0]['departures']:
            busElement = etree.Element('bus', time=item['time'])
            serviceElement = etree.Element('service')
            serviceElement.text = item['service']
            destinationElement = etree.Element('destination')
            destinationElement.text = item['destinationName']
            stateElement = etree.Element('state')
            stateElement.text = item['realtimeText']
            operatorElement = etree.Element('operator')
            operatorElement.text = item['operatorName']
            busElement.append(serviceElement)
            busElement.append(destinationElement)
            busElement.append(stateElement)
            busElement.append(operatorElement)
            root.append(busElement)

        s = etree.tostring(root, pretty_print=True)
        print s

        f = open('schedule.xml', 'w')
        f.write(s)
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
