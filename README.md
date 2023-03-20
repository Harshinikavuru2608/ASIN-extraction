# ASIN-extraction
"Extracting the ASINs of different products present on the given webpage"
### The final output of the assesment consists of a python code which:

1) Finds the number of ASINs in the given webpage

2) Finds all the ASINs in the webpage

3) Implements multiprocessing to speed up the process of finding al the ASINs

## Scrape Product Details from Product Page

 1) Add the required urls to a final names "urls.txt"
 
 2) Run  "asins.py"
 
 3) Get the output data in the file "output1.txt"

## Usage

From a terminal:

1) Clone this project git clone https://github.com/Harshinikavuru2608/ASIN-extraction

2) Add a Virtual Environment python3 -m venv .venv (Optional)

3) Activate the Virtual Environment source .venv/bin/activate (Optional)

4) Install Requirements pip3 install -r requirements.txt

## Input Data

The input is a text file which consists of all the webpage links given in the excel sheet.
Snapshot of the txt file: 

   <img width="447" alt="Screenshot 2023-03-19 at 16 20 49" src="https://user-images.githubusercontent.com/125713954/226366829-57f632a9-0b10-486e-8930-10eb3d35f839.png">


## Procedure

1) Open the "urls.txt" file in read mode.

    2) Go through each of the links one by one.

    3) For each link complete the following steps:

        1) Go through the enire webpage and scrape out all the amazon product links available in it.
    
        2) Store these links in a "output.txt" file.
    
        3) For each amazon link in the "output.txt" file find the ASIN number.
    
        4) Open a new "output1.txt" file in append format and append all the ASINs found in each page to this txt document.
    
    4) This process takes a long time if each webpage is searched one after the other. Hence lets implement multiprocessing.

    5) For implementing multiprocessing "n" number of threads are taken and ecah thread is assigned to one link in the "urls.txt" file. That is, the threads run parallelly for each of the links and get the ASINs for the products present in the webpage.

### Snapshot of example webpage:

<img width="1093" alt="Screenshot 2023-03-19 at 16 39 18" src="https://user-images.githubusercontent.com/125713954/226365583-8540378a-26fc-4906-86d6-f51ded3b16ce.png">

    1) we can observe from the above screenshot that the website consists of amazon products with their respective links. 
     
    2) Hence, we need to scrape out these amazon links of the products to get the ASINs of the products. 
    
    3) For the process of scraping we will use the "BeautifulSoup" library.
    
### Snapshot of "Output.txt":

<img width="583" alt="Screenshot 2023-03-19 at 16 36 45" src="https://user-images.githubusercontent.com/125713954/226365338-dbb1f010-57ac-46fa-ac9e-2dcec43ab2a3.png">


 The output.txt consists of all the amazon product links present in the website.
 
 ### Snapshot of "Output1.txt" :
 
 ![image](https://user-images.githubusercontent.com/125713954/226366040-7fee51be-2f7e-448a-8aba-b2afb2f1c403.png)

 In the snapshot of output1.txt file we can see all the different ASINs present in the given website. There are twenty different products with different ASIN number present on the webpage.
