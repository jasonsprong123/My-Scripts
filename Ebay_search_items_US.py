"""
Hello. This code is written Python -3.6 using EbaySDK .
Author: Jason Sprong
Date: Aug15 2017
I'm working on incorporating a GUI to wrap this into, next.
MUST HAVE ebaysdk installed! 
MUST have an ebay APP_ID to run.
"""
try:
    from ebaysdk.finding import Connection as finding
except ImportError:
    raise (ImportError,"The ebaysdk module is required to run this program.")

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
api = finding(siteid='EBAY-US', appid='<MY ebay APP_ID>')
api.execute('findItemsAdvanced', {
    'keywords': input1+","+input2,                    ##I want to find a way to make it user-input from the GUI
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
