from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import csv
#import _thread as thread
import threading


def files():
	with open('Odoo Partners.csv' , 'a+') as o:
		filewritero = csv.writer(o , delimiter=';')
		filewritero.writerow(['Type','Name','Address','Telephone','Website','E-mail'])
		o.close()
	'''
	with open('Gold Odoo Partners.csv' , 'a+') as g:
		filewriterg = csv.writer(g , delimiter=';')
		filewriterg.writerow(['Name','Address','Telephone','Website','E-mail'])
		g.close()

	with open('Silver Odoo Partners.csv' , 'a+') as s:
		filewriters = csv.writer(s , delimiter=';')
		filewriters.writerow(['Name','Address','Telephone','Website','E-mail'])
		s.close()

	with open('Ready Odoo Partners.csv' , 'a+') as r:
		filewriterr = csv.writer(r , delimiter=';')
		filewriterr.writerow(['Name','Address','Telephone','Website','E-mail'])
		r.close()
	'''
class myThread (threading.Thread):
	def __init__(self,partner):
		threading.Thread.__init__(self)
		self.partner = partner  
	def run(self):
		#threadLock.acquire()
		det = []
		p_url = uReq(self.partner)
		p_soup = soup(p_url.read(),'html.parser')
		p_url.close()
		#threadLock.release()
		p_type = p_soup.find('h3' , {"class" : "col-lg-12 text-center text-muted"}).getText()
		p_type = p_type[1:]
		det.append(p_type)
		p_name = p_soup.find('h1' , {"id" : "partner_name"}).getText()
		det.append(p_name)
		p_add = p_soup.find('span' , {"itemprop" : "streetAddress"}).getText()
		det.append(p_add)
		try:
			p_tele = p_soup.find('span' , {"itemprop" : "telephone"}).getText()
		except:
			p_tele = ' '
		det.append(p_tele)
		try:
			p_website = p_soup.find('span' , {"itemprop" : "website"}).getText()
		except:
			p_website = ' '
		det.append(p_website)
		try:
			p_email = p_soup.find('span' , {"itemprop" : "email"}).getText()
		except:
			p_email = ' '
		det.append(p_email)
		with open('Odoo Partners.csv' , 'a+') as g:
			filewriterg = csv.writer(g , delimiter=';')
			filewriterg.writerow(det)
			g.close()

def parse(partner):	
	
	det = []
	p_url = uReq(partner)
	p_soup = soup(p_url.read(),'html.parser')
	p_url.close()	
	p_type = p_soup.find('h3' , {"class" : "col-lg-12 text-center text-muted"}).getText()
	p_type = p_type[1:]
	det.append(p_type)
	p_name = p_soup.find('h1' , {"id" : "partner_name"}).getText()
	det.append(p_name)
	p_add = p_soup.find('span' , {"itemprop" : "streetAddress"}).getText()
	det.append(p_add)
	try:
		p_tele = p_soup.find('span' , {"itemprop" : "telephone"}).getText()
	except:
		p_tele = ' '
	det.append(p_tele)
	try:
		p_website = p_soup.find('span' , {"itemprop" : "website"}).getText()
	except:
		p_website = ' '
	det.append(p_website)		
	try:
		p_email = p_soup.find('span' , {"itemprop" : "email"}).getText()
	except:
		p_email = ' '
	det.append(p_email)
	with open('Odoo Partners.csv' , 'a+') as g:
		filewriterg = csv.writer(g , delimiter=';')
		filewriterg.writerow(det)
		g.close()
	'''
	if 'Gold' in p_type:
		with open('Gold Odoo Partners.csv' , 'a+') as g:
			filewriterg = csv.writer(g , delimiter=';')
			filewriterg.writerow(det)
			g.close()
		
	elif 'Silver' in p_type:
		with open('Silver Odoo Partners.csv' , 'a+') as s:
			filewriters = csv.writer(s , delimiter=';')
			filewriters.writerow(det)
			s.close()
		
	elif 'Ready' in p_type:
		with open('Ready Odoo Partners.csv' , 'a+') as r:
			filewriterr = csv.writer(r , delimiter=';')
			filewriterr.writerow(det)
			r.close()
		'''
	#print(len(lst))

if __name__ == '__main__':
	temp = "https://www.odoo.com/partners"
	#threadLock = threading.Lock()
	#threads = []

	files()

	url = uReq(temp)
	site_soup = soup(url.read(),'html.parser')
	url.close()

	partners = []
	prefix = 'https://www.odoo.com'
	for all_sites in site_soup.findAll('div' , {"class" : "media-body o_partner_body"}):
		site = all_sites.find('a')
		st = prefix + site.get('href')
		thread1 = myThread(st)
		thread1.start()
	#	threads.append(thread1)
	#parse(partners)
	#for item in threads:
	#	item.join()