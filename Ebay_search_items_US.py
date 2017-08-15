"""
Hello. This code is written Python -3.6 using EbaySDK .
User enters search parameters, app returns 25 matching items with price and description.
Author: Jason Sprong
Date: Aug15 2017
I'm working on incorporating a GUI to wrap this into, next.
"""
from ebaysdk.finding import Connection as finding

input1 = input("give one search term: \n")
input2 = input("give one more search term: \n")
mincost = input("give minimum cost:\n")
maxcost = input("give max cost: \n")
itemcond = input("Condition: 'New' or 'Used'? \n:").upper()
itemcond2=itemcond
if itemcond == "USED":
    itemcond2 = "Used"
else:
    itemcond2 = "New"
api = finding(siteid='EBAY-US', appid='<MY APP ID>')
api.execute('findItemsAdvanced', {
    'keywords': input1+","+input2,                    ##I want to find a way to make it user-input from the GUI
    # 'categoryId' : ['177', '111422'],                ## category necessary??
    'itemFilter': [
        {'name': 'Condition', 'value': itemcond2},
        {'name': 'MinPrice', 'value': mincost, 'paramName': 'Currency', 'paramValue': 'GBP'}, ## min price make it a user variable
        {'name': 'MaxPrice', 'value': maxcost, 'paramName': 'Currency', 'paramValue': 'GBP'}  ## max price make it a user variable
    ],
    'paginationInput': {
        'entriesPerPage': '25',                     ##scale-back for GUI?
        'pageNumber': '1'
    },
    'sortOrder': 'CurrentPriceHighest'
})


dictstr = api.response.dict()
# print (dictstr)
# quit()

for item in dictstr['searchResult']['item']:
    print ("\nItemID: %s" % item['itemId'])
    print ("Title: %s" % item['title'])
    print (">>the Current price of item is $%s" %item['sellingStatus']['currentPrice']['value'])
    print ("Item Url: %s\n" % item['viewItemURL'])

###################################################################################################

        ## Try beautiful Soup for output options?? 
