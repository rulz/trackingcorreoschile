import urllib
import json
from BeautifulSoup import BeautifulSoup

__author__ = 'Raul Sepulveda'
__version__ = '0.0.3'

def get_info(row):
	status = str(row[0]).replace('<td>&nbsp;&nbsp;','').replace('&nbsp;</td>','').replace("  ","")
	date = str(row[1]).replace('<td align="center">','').replace('&nbsp;</td>','').replace("  ","")
	office = str(row[2]).replace('<td>&nbsp;&nbsp;','').replace('&nbsp;</td>','').replace("  ","")

	return status, date, office

def get_data_tracking(code):
	dict = {}
	data = urllib.urlencode({"ctl00$ContentPlaceHolder1$stxt":code})
	result = urllib.urlopen("http://courier.correos.cl/seguimientoweb/Resumen.aspx", data).read()
	soup = BeautifulSoup(result)
	table = soup.find('table', {'class': 'tracking'}).findAll('tr')

	for i,row in enumerate(table):
		if i==1: 
			status, date, office = get_info(row.findAll('td'))
			dict['code'] = code
			dict['status'] = status
			dict['date'] = date
			dict['office'] = office

	return dict

def code_list(list_code):
	response = []
	for code in list_code:
		response.append(get_data_tracking(code))
	
	return json.loads(json.dumps(response, ensure_ascii=True))

