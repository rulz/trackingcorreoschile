import urllib
import json
from BeautifulSoup import BeautifulSoup

def get_data_tracking(code):
	dict = {}
	data = urllib.urlencode({"ctl00$ContentPlaceHolder1$stxt":code})
	result = urllib.urlopen("http://courier.correos.cl/seguimientoweb/Resumen.aspx", data).read()
	soup = BeautifulSoup(result)

	table = soup.find('table', {'class': 'tracking'}).findAll('tr')

	for i,row in enumerate(table):
		if i==1: 
			dict['State'] = str(row.findAll('td')[0]).replace('<td>&nbsp;&nbsp;','').replace('&nbsp;</td>','').replace("  ","")
			dict['Date'] = str(row.findAll('td')[1]).replace('<td align="center">','').replace('&nbsp;</td>','').replace("  ","")
			dict['Oficina'] = str(row.findAll('td')[2]).replace('<td>&nbsp;&nbsp;','').replace('&nbsp;</td>','').replace("  ","")

	return dict

def code_list(list_code):
	response = []
	for code in list_code:
		response.append(get_data_tracking(code))
	
	return json.dumps(response)

