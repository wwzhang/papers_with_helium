#!/usr/bin/env python
import sys
import os
import time
from helium import *
from selenium.webdriver import FirefoxOptions
#set the folder to save pdfs
pdf_loc = "The_Folder_TO_Save_PDFs"
options = FirefoxOptions()
options.set_preference("browser.download.useDownloadDir", True)
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", (pdf_loc))
options.set_preference("browser.download.viewableInternally.enabledTypes", "")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
options.set_preference("pdfjs.disabled", True)

def wait_for_downloads():
    print("Downloading", end="")
    while any([filename.endswith(".part") for filename in
               os.listdir((pdf_loc))]):
        time.sleep(1)
        print(".", end="")
    print("done!")

def download_w_firefox():
	start_firefox((line), options=options, headless=True)

	link = get_driver().current_url	
	elife = "elifesciences.org"
	nature = "nature.com"
	sc = "sciencedirect.com"
	cell = "cell.com"
	pnas = "pnas.org"
	brx = "biorxiv.org"
	oup = "oup.com"
	aaas = "sciencemag.org"
	if elife in link:
	    click(Image(alt="Download icon"))
	    click(Link('Article PDF'))
	elif nature in link or brx in link:
	    click('Download PDF')
	elif sc in link:
	    time.sleep(10)
	    wait_until(Text("Article Metrics").exists)
	    click('Download PDF')
	    if Text('Download this article').exists(): 
	    	click('Download this article')
	elif cell in link or pnas in link or oup in link or aaas in link:
	    click('PDF')
	    if Text('Standard PDF').exists(): click('Standard PDF')
	    elif Text('Download PDF').exists(): click('Download PDF')
	    
	#start check download finish 15s later
	time.sleep(5)
	wait_for_downloads()
	kill_browser()	

input1 = (sys.argv[1])
if input1 == '-f':
	with open((sys.argv[2]), 'r') as fp:
		for line in fp:
			if line.strip():
				#print(line)
				download_w_firefox()
elif input1 == '-d':
	with open((sys.argv[2]), 'r') as fp:
		for line in fp:
			if line.strip():
				line = 'https://doi.org/' + line
				download_w_firefox()
elif input1 == '-p':
	with open((sys.argv[2]), 'r') as fp:
		for line in fp:
			if line.strip():
				line = 'https://pubmed.ncbi.nlm.nih.gov/' + line
				download_w_firefox()
else:
	line = input1
	download_w_firefox()

