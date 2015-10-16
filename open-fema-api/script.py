import urllib2

host = "http://www.fema.gov"
path = "/api/open"
version = "/v1"
entity = "/DisasterDeclarationsSummaries"

request_s = host + path + version + entity + "?"

"""
For disasterNumber, incidentEndDate, incidentBeginDate
"""
request_s += "$select=title,disasterNumber,incidentEndDate,incidentBeginDate"

"""
For 5000 disaster records
"""
request_s += "&$top=5000"

"""print(request_s)"""

print urllib2.urlopen(request_s).read()
