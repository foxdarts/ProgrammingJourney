#this is a program for seeing my spending and hopefully making my spending go down


import csv
import gspread
import time



MONTH = 'August' #this will be the month name that you will need to change every month.

file = f"WF_{MONTH}.csv" #this is the filename that you download from your financial institute.

transactions = [] #empty list for holding transactions while you categorize them

Sustenance = ["example1", "example2"] #all of these variables you must fill with the names from the name coloum during splitout

Bills = [] #see sustenance note

Subscriptions = [] #see sustenance note

TandT = [] #see sustenance note

def WF_FIN(file): 
    
    with open(file, mode = 'r') as csv_file: 
    
        csv_reader = csv.reader(csv_file)
    
        for row in csv_reader:
        
            date = row[0]
        
            name = row[4]
        
            amount = float(row[1])
        
            category = "other"
            
            stringcheck = 0
        
            if name == "": #put the EXACT name for any savings transfer within the quotes.
        
                category = "Savings Transfer"
            
            for i in Sustenance: #add any sustance to this variable.
                
                if (name.find(i) != -1):
                    
                    stringcheck += 1
                    
            if stringcheck == 1:
                
                category = "Food"
                
            for i in Bills: #add bills to variable
                
                if (name.find(i) != -1):
                    
                    stringcheck += 2
                
            if stringcheck == 2:
                
                category = "Rent & Bills"
                
            for i in Subscriptions: #add any recurring payments to variable
                
                if (name.find(i) != -1):
                    
                    stringcheck += 3
                    
            if stringcheck == 3:
                
                category = "Subscription"
            
            for i in TandT: #transport and travel aka gas
                
                if (name.find(i) != -1):
                    
                    stringcheck += 4
                    
            if stringcheck == 4:
                
                category = "Transport & Travel"
                
                
            if "WAY2SAVE" in name:
                
                category = "Salary"
                
            
            transaction = ((date, name, amount, category))
        
            print(transaction)
        
            transactions.append(transaction)
            
        return transactions


        
        
#for uploading to google sheet

sa = gspread.service_account() #must set up a service account on google to work.

sh = sa.open("Personal Finances") #file name for the google sheet

worksheet = sh.worksheet(f"{MONTH}") #subsheet within google sheet for actual month breakdown

rows = WF_FIN(file)

for row in rows:
    
    worksheet.insert_row([row[0], row[1], row[3], row[2]], 8)
    
    time.sleep(2) #adds in a timestop as google sheets can only refresh 60 times a minute