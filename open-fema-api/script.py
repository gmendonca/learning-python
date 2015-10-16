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

result = urllib2.urlopen(request_s).read()
req_dict = eval(result)
disaster_list = eval(str(req_dict[req_dict.keys()[0]]))

csvfile = open("fematest.csv", "w")

for item in dict(disaster_list[0]):
    csvfile.write(item + ",")

csvfile.write("\n")

for disaster in disaster_list:
    disaster_dict = dict(disaster)
    for key in disaster_dict:
        csvfile.write(str(disaster_dict[key]) + ",")
    csvfile.write("\n")

csvfile.close()
