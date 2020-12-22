# Download Papers With [Helium](https://github.com/mherrmann/selenium-python-helium)

Download PDFs of papers with links, DOIs, or PMIDs:
1. Download from a file containing links to papers with "-f" option;
2. Download from a file containing DOIs of papers with "-d" option;
3. Download from a file containing PMIDs of papers with "-p" option; 
4. Download from a link of the paper.

This is a Python3 based-program which runs a headless Firefox to download. It is a quick and dirty wrap-up, but might be easy for editing and expand. Not debugged much, and it might crash due to connection problem. 
## Usage
1. Change the "pdf_loc = " line of getpdf.py to the folder you want to use to save the PDF
2. run the program with the correct options chosen 
````
  getpdf.py -f the_link_file
  getpdf.py -d the_DOI_file
  getpdf.py -p the_PMID_file
  getpdf.py the_link
```` 
3. Take a look at line 28 - 35 of getpdf.py to get which websites this support and modify it to your needs. In doing so, it might help to change the headless option to False.

## Install and Requirement
Requires Python3, Firefox, and [Helium](https://github.com/mherrmann/selenium-python-helium)

To install Helium
````
  pip install helium
```` 
