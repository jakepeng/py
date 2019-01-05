#-*- coding:utf-8 -*-
import sys, requests, json

def main(argv):
    apiKey = '1a739d42f96658378a0ac7804fefdb2ebd649182e4971c99a3eddle949277270'
	apiKey_avlb = 'd9eaa63c9008987381860a36e0d8c2aa2c641bf35e42bbe11e97bd452ea'
	
	try:
	    s = requests.Session()
		s.verify = False
		
	    # Open URL
		resp = s.get('https://booking.hkexpress.com/zh-TW/select/',
		             params={'SearchType': 'RETURN',
					         'OriginStation': 'HKG',
							 'DestinationStation': 'KIX',
							 'DepartureDate': '01/01/2019',
							 'ReturnDat': '05/01/2019',
							 'Adults': '1',
							 'LowFareFinderSelected': 'false'
							 }
				     )
		
		# Session
		resp = s.get('https://booking-api.hkexpress.com/api/v1.0/session',
		             header={'apiKey': apiKey}
				     )
		
	    # Query availability
		resp = s.post('https://availability-api.hkexpress.com/api/v1.0/availability/lowfareavailability',
		             header={'apiKey': apiKey_avlb, 'Content-Type': 'application/json; charset=utf-8'}
		             data=json.dump({"outboundDepartureStation":"HKG",
					                 "outboundArrivalStation":"KIX",
							         "outboundStartDate":"2018-12-29",
							         "outboundEndDate":"2019-01-04",
							         "returnDepartureStation":"KIX",
							         "returnArrivalStation":"HKG",
							         "returnStartDate":"2019-01-02",
									 "returnEndDate":"2019-01-08",
									 "tripType":"Return",
									 "cultureCode":"zh-TW",
									 "adultsNumber":1,
									 "currency":""
							         }
								   )
				     )
		print(resp.text)
		
	    # Query available flights
		resp = s.get('https://availability-api.hkexpress.com/api/v1.0/availability/dayavailability',
		             header={'apiKey': apiKey_avlb}
		             params={'outboundDate': '2019-01-01',
							 'returnDate': '2019-01-05'
							 }
				     )
		print(resp.text)
		
	except Exception as err:
	    print(err)
		sys.exit(2)
	
if __name__ == '__main__':
    main(sys.argv)
	