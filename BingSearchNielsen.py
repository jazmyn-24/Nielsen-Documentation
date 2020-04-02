import http.client, urllib.parse, json
from tld import get_fld
import datetime
from Utils import connect_mongo
import Settings
import pandas as pd
from BingSummaryNielsen import bingSummary

host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/search"

def BingWebSearch(search, offset,marketmap,mkt="en-GB"):
    '''This function performs bing search after it is called in the main function.
     @:param search: enters search query
     @:type: String
     @:param offset: Position of cursor
     @:type: int64
     @:param marketmap: MARKET_MAP collection dataframe
     @:type: object
     @:param mkt: Code of the market in market map
 '''
    try:
        headers = {'Ocp-Apim-Subscription-Key': Settings.bing_subscription_key}
        conn = http.client.HTTPSConnection(host)
        query = urllib.parse.quote(search)
        print(marketmap)
        mktc = list(marketmap.loc[marketmap['country']==mkt.capitalize()]['code'])[0]
        print(mktc)
        conn.request("GET", path + "?q=" + query + "&count=100&mkt="+mktc+"&setLang=EN&offset=" + str(offset), headers=headers)
        response = conn.getresponse()
        headers = [k + ": " + v for (k, v) in response.getheaders()
                       if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
        return headers, response.read().decode("utf8")
    except Exception as e:
        print(str(e))

def main(market_name,ts):
    ''' Main function where Bing Search is implemented and search term is defined. The results are returned and stored in new dataframe
    and the df is then exported to BING_SEARCH_NIELSEN collection.
    @:param ts: Timestamp
    @:type: int64'''
    connection = connect_mongo()
    marketmap = pd.DataFrame((connection[Settings.MARKET_MAP].find({"country":market_name.capitalize()},{"code":1,"country":1,"_id":0})))
    print(marketmap)
    reader = connection[Settings.CLEAN_NIELSEN].find({"UPPER_COUNTRY":market_name.upper(), "ts":ts},{"_id": 0})
    print(reader)
    for records in reader:
        try:
            count = connection[Settings.BRAND_SOURCE].count({"brand_low": str(records['UPPER_BRAND']).lower(), "country": str(records['UPPER_COUNTRY']).lower()})
            if count == 0:
                term = str(records['UPPER_BRAND']).lower()+" "+str(records['MANUFACTURER']).lower()
                print("fetching Records : ", term)
                brand=str(records['UPPER_BRAND']).lower()
                company=str(records['MANUFACTURER']).lower()
                market=str(records['UPPER_COUNTRY']).lower()
                if len(Settings.bing_subscription_key) == 32 and company != "PRIVATE LABEL":
                    print('Searching the Web for: ', term)
                    offset = 0
                    totalEstimatedMatches = 100
                    count = 0
                    while (offset < totalEstimatedMatches):
                        count = count + 1
                        headers, result = BingWebSearch(term, offset,marketmap, market)
                        data = json.dumps(json.loads(result), indent=4)
                        d_data = json.loads(data)
                        print("count : ", str(count))
                        print("offset : ", str(offset))
                        if 'webPages' in d_data:
                            totalEstimatedMatches = d_data['webPages']['totalEstimatedMatches']
                            news_dict = d_data['webPages']['value']
                            for news in news_dict:
                                news['hitCount'] = count
                                news['totalEstimateMatches'] = totalEstimatedMatches
                                news['fetchdate'] = datetime.datetime.utcnow()
                                news['offset'] = offset
                                news['query'] = term
                                news['count'] = 1
                                news['brand'] = brand
                                news['company'] = company
                                news['country'] = market
                                news['ts'] = ts
                                news['domain'] = get_fld(news['url'])
                                exists = connection[Settings.BING_SEARCH_NIELSEN].count({'brand': news['brand'], 'domain': news['domain'],'country':market_name})
                                if exists == 0:
                                    connection[Settings.BING_SEARCH_NIELSEN].insert(news)
                                else:
                                    connection[Settings.BING_SEARCH_NIELSEN].update_one({'brand': news['brand'], 'domain': news['domain'],'country':market_name})
                        offset = offset + len(news_dict)
                        totalEstimatedMatches = 0
        except Exception as e:
            print(str(e))

bingSummary(market, ts)