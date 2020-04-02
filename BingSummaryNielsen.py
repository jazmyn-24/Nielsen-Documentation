from pymongo import DESCENDING
from Utils import connect_mongo,exclusion_list
import Settings

def bingSummary(market,ts):
    '''This function aggregates all URLs brand-wise stored in BING_SEARCH_MINTEL and stores them in AIDLE_DATA.
    @:param market: Country Name
    @:type : String
    @:param ts: Timestamp
    @:type: int64'''
    connection = connect_mongo()

    brand_list = connection[Settings.BING_SEARCH_NIELSEN].find({"country": market,'ts':ts},{"brand":1,"_id":0}).distinct("brand")

    for brand in brand_list:
        try:
            mdata = connection[Settings.BING_SEARCH_NIELSEN].find({"ts":ts,"brand": brand, "country": market, "domain": {"$nin": exclusion_list}},no_cursor_timeout=True).sort("count", DESCENDING).limit(5)
            bjson = {}
            manufacturer=""
            for data in mdata:
                if brand + market in bjson:
                    bjson[brand + market]['urls'].append(data['url'])

                else:
                    bjson[brand + market] = {}
                    bjson[brand + market]['urls'] = []
                    bjson[brand + market]['variants'] = []
                    bjson[brand + market]['urls'].append(data['url'])

                    bjson[brand + market]['brand'] = data['brand']
                    bjson[brand + market]['manufacturer'] = data['company']
                    bjson[brand + market]["country"] = data['country']
                    bjson[brand + market]['verified'] = False
                    bjson[brand + market]['lock'] = False
                    bjson[brand + market]['data'] = 'Nielsen'
                    # bjson[brand + market]['recordid'] = data['recordid']
                manufacturer = data['company']

            if brand + market not in bjson:
                manufacturer = connection[Settings.BING_SEARCH_NIELSEN].find({"ts":ts,"country": market, "brand": brand}, no_cursor_timeout=True).distinct("company")

                bjson[brand + market] = {}

                bjson[brand + market]['urls'] = []
                bjson[brand + market]['variants'] = []
                bjson[brand + market]['urls'] = []

                bjson[brand + market]['brand'] = brand
                bjson[brand + market]['manufacturer'] = manufacturer[0]
                bjson[brand + market]["country"] = market
                bjson[brand + market]['verified'] = False
                bjson[brand + market]['lock'] = False
                bjson[brand + market]['data'] = 'Nielsen'

                manufacturer = manufacturer[0]
            bjson[brand + market]['ts'] = ts



            print(brand)
            print(manufacturer)

            count = connection[Settings.BRAND_SOURCE].count({"brand_low":brand.lower(),"country":market})
            eb_count = connection[Settings.ESTABLISHED_BRANDS].count({"name_low":brand.lower()})
            m_count = connection[Settings.ESTABLISHED_BRANDS].count({"name_low":manufacturer.lower()})
            print(count)
            print(eb_count)
            print(m_count)
            if count==0 and eb_count==0 and m_count==0:
                connection[Settings.AIDLE_DATA].insert(bjson[brand + market])
        except Exception as e:
            print(str(e))


