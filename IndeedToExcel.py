# 10/22/21
# Indeed Web Scraping Program that extracts four pages of job data and writes it to a formated excel file 

from bs4 import BeautifulSoup
import requests
import pandas as pd
import pandas.io.formats.excel

# extracts Indeed html given a page number 
def extract(page):
    url = f'https://www.indeed.com/jobs?q=intern&l=North%20Carolina&start={page}' #page is passed so multiple pages can be extracted
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'} # dictionary containing my computer's user agent 
    
    r = requests.get(url, headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    return soup

def transform(soup): # extracts job data and creates a dictionary for each job, appends each to a list
    divs = soup.find_all('div', class_="slider_container") # creates list containing job cards

    for div in divs: # extracts information from each card
        jobTitle = div.find('span').text
        if jobTitle == "new":
            jobTitle = div.find_next("span").find_next("span").text
        company = div.find('span', class_='companyName').text
        try:
            salary = div.find("div", class_="salary-snippet").text
        except AttributeError:
            salary = 'none listed'
        summary = div.find("div", class_ = "job-snippet").text.replace('\n', '') # replaces new lines in summary with nothing
        try:
            companyLink = "https://www.indeed.com" + div.a['href']   
        except:
            companyLink = "No Link Found"     
        
       
        job = {
            'Title' : jobTitle, 
            'Company' : company,  
            'Salary' : salary, 
            'Summary' : summary,
            'Company Link' : companyLink,
            

        }
        jobList.append(job) # appends job dictionary to empty list 
    return

# creates pandas dataframe using job dictionaries, exports data to excel file, formats excel  
def exportToExcel():
    pandas.io.formats.excel.ExcelFormatter.header_style = None #resets pandas default header style to none so it can be formated

    df = pd.DataFrame(jobList) # creates a pandas dataframe 
    writer = pd.ExcelWriter('internships.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name = "Indeed Internships", index = False)
    workbook = writer.book
    worksheet = writer.sheets['Indeed Internships']
    
    format = workbook.add_format({'text_wrap': 'True', 'font_size' : 15})

    formatHeaderRow = workbook.add_format({'text_wrap': 'True', 'font_size' : 20, 'bold': 'True'}) 

    # sets column formatting 
    worksheet.set_column('A:C', 20, format) 

    worksheet.set_column('D:E', 40, format)
    worksheet.set_column('E:E', 50, format)


    # sets header row formatting 
    worksheet.set_row(0, None, formatHeaderRow) #set header row formatting

    writer.save(); 
    

    return

jobList = [] #jobList global variable

for i in range(0,40,10): #extracts four pages of Indeed job listings 
    print(f'Getting Page, {i}')
    c = extract(i)
    transform(c)

exportToExcel()
