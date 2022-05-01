#### Step 1 - Imports

import requests 
import pandas as pd 


#### Step 2 - Requests & CURL

headers = {
    'authority': 'api2.realtor.ca',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
    'accept': '*/*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.realtor.ca',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.realtor.ca/',
    'accept-language': 'en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7',
    'cookie': 'visid_incap_2269415=pjB3DImWSy2DSncBmJhxAdFrDWEAAAAAQUIPAAAAAABjsqrQxZ4W1Wnwofq2RdhC; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; visid_incap_2271082=AcUYRjx+RSySjRa8AwANG+RrDWEAAAAAQUIPAAAAAABz1Fko5zVbdsXy74RazGys; nlbi_2269415=sQ3FGkf/tEmEWQgzkG5lugAAAAAFMffS0zejJiUWk0zf9bPa; incap_ses_259_2269415=5xvDGelCA1fVQR9jLCeYA51oD2EAAAAA9rhuUKdQGbjkUON9E3IjaQ==; ASP.NET_SessionId=24h1wcl0hpfksrnwenmtnvc2; nlbi_2271082=X8w3O3RA+wgyUh5zcbDG1QAAAAAXy9nLAU3f+hps/3dErKgI; incap_ses_259_2271082=7KPhTmwNclfoRB9jLCeYA6ZoD2EAAAAAPGGuZXT12qBYJonPwQNtkg==; nlbi_2269415_2147483646=pe3INHrRyQUhvi6qkG5lugAAAADzBsGSQ5f/qTtuon11CFB2; reese84=3:rmjwp/+XL4VvwGTMRmqZKg==:Y/gxtGy7j1ea6qEXdh6UKt0rwpGMJLxEHeQSHve97oRtozHA5TtJsRU+nqJ8AVLfmsjTthTMcuIME0YMfR6Skb3utndAPH0eD+RVwRlS54KqxvQ1+2C95rnRPUjNiRAN8oNAmTYLnqly5W5lbVry227s3FSOGWDtqSUA68blq55uWxLUFBWy/eZIOys1b95paQh/xbGfTaMVMK/z7SOTlDCFCbP0XoT7KpN9cZlb8fI7JKk686uH1iSyzsS12iAMlmwdoA86MN1h/SMcVF4LRhutUhx4pzPygCxeOm5C9vM2Sfec8Ljb65GyAsy5BbtBqOwyeF047rxdJxg8ptFWgNL0lPPah+V5HSlM8fI0mIHPO6No2VEiXh2XgwKRCCzfYbD2PlqF6jOxoZ8gvtUQvughoUmJIVp/ScQzW8gNPIY=:z7PtjNQieiTUs7f51Opmgwt+YxwjloRsoxEVvmV6OOM=',
}

data = {
  'ZoomLevel': '9',
  'LatitudeMax': '45.77958',
  'LongitudeMax': '-74.50768',
  'LatitudeMin': '44.71609',
  'LongitudeMin': '-77.09222',
  'Sort': '6-D',
  'PropertyTypeGroupID': '1',
  'PropertySearchTypeId': '1',
  'TransactionTypeId': '2',
  'Currency': 'CAD',
  'RecordsPerPage': '12',
  'ApplicationId': '1',
  'CultureId': '1',
  'Version': '7.0',
  'CurrentPage': '1'
}

response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)




#### Step 3 - Check Status Code

response

#### Step 4 - Create Json Object

result_json = response.json()

#### Step 5 - Output Keys

result_json.keys()

#### Step 6 - Find your Data

# - Address
# - Bedrooms
# - Bathrooms
# - Agent Name
# - Area Code
# - Phone Number
# - Price

# starting point
result_items = result_json['Results']

len(result_items)

# address
result_items[0]['Property']['Address']['AddressText']

# bedrooms
result_items[0]['Building']['Bedrooms']

# bathrooms
result_items[0]['Building']['BathroomTotal']

# agent name
result_items[0]['Individual'][0]['Name']

# area code
result_items[0]['Individual'][0]['Phones'][0]['AreaCode']

# telephone
result_items[0]['Individual'][0]['Phones'][0]['PhoneNumber']

# price
result_items[0]['Property']['Price']

#### Step 7 - Put everything together - Loop through results and append data inside a list

address = []
bedrooms = []
bathrooms = []
agent_name = []
area_code = []
phone_number = []
price = []

for result in result_items:
    
    # address
    try:
        address.append(result['Property']['Address']['AddressText'])
    except:
        address.append('')
    
    
    # bedrooms
    try:
        bedrooms.append(result['Building']['Bedrooms'])
    except:
        bedrooms.append('')
        
    
    # bathrooms
    try:
        bathrooms.append(result['Building']['BathroomTotal'])
    except:
        bathrooms.append('')
    
    # agent name
    try:
        agent_name.append(result['Individual'][0]['Name'])
    except:
        agent_name.append('')
    
    # area code
    try:
        area_code.append(result['Individual'][0]['Phones'][0]['AreaCode'])
    except:
        area_code.append('')
    
    # phone number
    try:
        phone_number.append(result['Individual'][0]['Phones'][0]['PhoneNumber'])
    except:
        phone_number.append('')
    
    # price
    try:
        price.append(result['Property']['Price'])
    except:
        price.append('')



#### Step 8 - Pandas Dataframe

df_realtor = pd.DataFrame({'Address': address, 'Bedrooms': bedrooms, 'Bathrooms':bathrooms,
                          'Agent Name': agent_name, 'Area Code': area_code, 'Telephone': phone_number, 'Price': price})

df_realtor

#### Step 9 - Multiple Pages

address = []
bedrooms = []
bathrooms = []
agent_name = []
area_code = []
phone_number = []
price = []

for i in range(1,51):

    headers = {
        'authority': 'api2.realtor.ca',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
        'accept': '*/*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.realtor.ca',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.realtor.ca/',
        'accept-language': 'en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7',
        'cookie': 'visid_incap_2269415=pjB3DImWSy2DSncBmJhxAdFrDWEAAAAAQUIPAAAAAABjsqrQxZ4W1Wnwofq2RdhC; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; visid_incap_2271082=AcUYRjx+RSySjRa8AwANG+RrDWEAAAAAQUIPAAAAAABz1Fko5zVbdsXy74RazGys; nlbi_2269415=sQ3FGkf/tEmEWQgzkG5lugAAAAAFMffS0zejJiUWk0zf9bPa; incap_ses_259_2269415=5xvDGelCA1fVQR9jLCeYA51oD2EAAAAA9rhuUKdQGbjkUON9E3IjaQ==; ASP.NET_SessionId=24h1wcl0hpfksrnwenmtnvc2; nlbi_2271082=X8w3O3RA+wgyUh5zcbDG1QAAAAAXy9nLAU3f+hps/3dErKgI; incap_ses_259_2271082=7KPhTmwNclfoRB9jLCeYA6ZoD2EAAAAAPGGuZXT12qBYJonPwQNtkg==; nlbi_2269415_2147483646=pe3INHrRyQUhvi6qkG5lugAAAADzBsGSQ5f/qTtuon11CFB2; reese84=3:rmjwp/+XL4VvwGTMRmqZKg==:Y/gxtGy7j1ea6qEXdh6UKt0rwpGMJLxEHeQSHve97oRtozHA5TtJsRU+nqJ8AVLfmsjTthTMcuIME0YMfR6Skb3utndAPH0eD+RVwRlS54KqxvQ1+2C95rnRPUjNiRAN8oNAmTYLnqly5W5lbVry227s3FSOGWDtqSUA68blq55uWxLUFBWy/eZIOys1b95paQh/xbGfTaMVMK/z7SOTlDCFCbP0XoT7KpN9cZlb8fI7JKk686uH1iSyzsS12iAMlmwdoA86MN1h/SMcVF4LRhutUhx4pzPygCxeOm5C9vM2Sfec8Ljb65GyAsy5BbtBqOwyeF047rxdJxg8ptFWgNL0lPPah+V5HSlM8fI0mIHPO6No2VEiXh2XgwKRCCzfYbD2PlqF6jOxoZ8gvtUQvughoUmJIVp/ScQzW8gNPIY=:z7PtjNQieiTUs7f51Opmgwt+YxwjloRsoxEVvmV6OOM=',
    }

    data = {
      'ZoomLevel': '9',
      'LatitudeMax': '45.77958',
      'LongitudeMax': '-74.50768',
      'LatitudeMin': '44.71609',
      'LongitudeMin': '-77.09222',
      'Sort': '6-D',
      'PropertyTypeGroupID': '1',
      'PropertySearchTypeId': '1',
      'TransactionTypeId': '2',
      'Currency': 'CAD',
      'RecordsPerPage': '12',
      'ApplicationId': '1',
      'CultureId': '1',
      'Version': '7.0',
      'CurrentPage': str(i),
    }

# response 
    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)
    
    # json object
    result_json = response.json()
    
    # result items
    result_items = result_json['Results']
    
    for result in result_items:
    
        # address
        try:
            address.append(result['Property']['Address']['AddressText'])
        except:
            address.append('')


        # bedrooms
        try:
            bedrooms.append(result['Building']['Bedrooms'])
        except:
            bedrooms.append('')


        # bathrooms
        try:
            bathrooms.append(result['Building']['BathroomTotal'])
        except:
            bathrooms.append('')

        # agent name
        try:
            agent_name.append(result['Individual'][0]['Name'])
        except:
            agent_name.append('')

        # area code
        try:
            area_code.append(result['Individual'][0]['Phones'][0]['AreaCode'])
        except:
            area_code.append('')

        # phone number
        try:
            phone_number.append(result['Individual'][0]['Phones'][0]['PhoneNumber'])
        except:
            phone_number.append('')

        # price
        try:
            price.append(result['Property']['Price'])
        except:
            price.append('')
    

df_realtor = pd.DataFrame({'Address': address, 'Bedrooms': bedrooms, 'Bathrooms':bathrooms,
                          'Agent Name': agent_name, 'Area Code': area_code, 'Telephone': phone_number, 'Price': price})

df_realtor

#### Step 10 - Store results in Excel

df_realtor.to_excel('realtor_multiple_pages.xlsx', index=False)

