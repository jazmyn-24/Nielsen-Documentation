import pandas as pd
import re
import unicodedata
from Utils import connect_mongo
import Settings
import numpy as np
from time import sleep
from BingSearchNielsen import main
import sys

def choose_brand(array):
    '''This This function chooses the brand from dataframe - nielsen, the brands chosen are normalized and added to a list.
     @:param array
     @:type: string'''
    abandoned = []
    for brand in array:
        new_brand = normalized_brand(brand)
        for re_brand in array:
            new_re_brand = normalized_brand(re_brand)
            if (new_brand in new_re_brand and new_brand != new_re_brand) and re_brand not in abandoned:
                abandoned.append(re_brand)
    return abandoned


def strip_accents(text):
    """This function converts unicoded string to normalized string to remove accents and other special characters such as umlauts etc.
        @:param text
        @:type:string"""
    return ''.join(char for char in
                   unicodedata.normalize('NFKD', str(text))
                   if unicodedata.category(char) != 'Mn')


def normalized_brand(brand):
    '''This function normalizes brand names.
       @:param brand
       @:type:string'''
    return re.sub("[:\-\+;'\"&$><%\s]+.", "", strip_accents(str(brand).lower()).replace(" and ", ""))


'''def category_mixing(original):
    category = {"Total Juice": ["Juice",
                                "Fruit/Flavoured Still Drinks",
                                "Nectars"],
                "Coffee": ["RTD (Iced) Coffee", "Coffee"],
                "Tea": ["RTD (Iced) Tea", "Tea"]
                }
    for key, value in category.items():
        if original in value:
            return key
    return original
'''
def dropDuplicateBrands(countryData):
    ''' This function drops duplicate brands within countryData dataframe.
       @:param countryData: Dataframe of  Nielsen data
       @:type: String'''
    countryData["Normalized-Brand"] = countryData["UPPER_BRAND"].apply(normalized_brand)
    countryData = countryData.drop_duplicates("Normalized-Brand")
    return countryData


def dropDiscardedBrands(countryData):
    ''' This function compares Manufacturers with Brands in CountryData and drops duplicates.'''
    discarded_brands = []
    for name, group in countryData.groupby(["MANUFACTURER"]):
        similar_brands = countryData[(countryData["MANUFACTURER"] == name)]
        if len(similar_brands["UPPER_BRAND"]) > 1:
            discarded_brand = choose_brand(similar_brands["UPPER_BRAND"])
            if discarded_brand:
                discarded_brands += discarded_brand
    countryData = countryData[~countryData.UPPER_BRAND.isin(discarded_brands)]
    return countryData


def dropEstablishedBrands(countryData,famous_brands):
    ''' This function compares Manufacturer column of countryData with Brand column in famous_brands, & Brand column of countryData with Brand column in famous_brands
       @:param famous_brands: Dataframe of established_brands
       @:type famous_brands: string'''
    countryData = countryData[~countryData["MANUFACTURER"].isin(famous_brands["UPPER_BRAND_1"])]
    countryData = countryData[~countryData["UPPER_BRAND"].isin(famous_brands["UPPER_BRAND_1"])]
    return countryData

def getPotentialDuplicates(countryData):
    ''' This function eliminates duplicate Data country wise and creates a list of potential duplicate brands.
     '''
    countryData['Duplicate Brand'] = ''
    countryData['Potential Duplicate'] = 0
    countryData['Established Brand'] = ''
    countryData['Potential Established'] = 0

    all_brands = countryData['UPPER_BRAND']

    total = countryData.shape[0]
    count = 0

    for idx, row in countryData.iterrows():
        count += 1
        if count % 100 == 0:
            progress = (count / total) * 100
            print("Processed {} out of {} ({}%)".format(count, total, round(progress)))
        if row['Duplicate Brand'] == '':
            i = 0
            for brand in all_brands:
                brand = str(brand)
                row['UPPER_BRAND'] = str(row['UPPER_BRAND'])
                brand_split = str(row['UPPER_BRAND']).split()
                brand_name = ''
                if len(brand_split) > 1:
                    brand_name = brand_split[0] + " " + brand_split[1]
                if row['UPPER_BRAND'] != brand:
                    if str(row['MANUFACTURER']) == str(
                            countryData.iloc[i]['MANUFACTURER']) and brand.startswith(
                                    brand_name + " ") and brand_name != '':
                        countryData.at[idx, 'Duplicate Brand'] = brand
                        countryData.at[i, 'Duplicate Brand'] = row['UPPER_BRAND']

                        countryData.at[idx, 'Potential Duplicate'] = 1
                        countryData.at[i, 'Potential Duplicate'] = 1
                    elif brand.startswith(row['UPPER_BRAND'] + " "):
                        countryData.at[idx, 'Duplicate Brand'] = brand
                        countryData.at[i, 'Duplicate Brand'] = row['UPPER_BRAND']

                        countryData.at[idx, 'Potential Duplicate'] = 1
                        countryData.at[i, 'Potential Duplicate'] = 1
                i += 1

    return countryData

def cleaning(ts):
    ''' This is the main function. Collections - BRANDS, ESTABLISHED_BRANDS, NIELSEN_DATA are stored in dataframes.
       All previous functions are executed in this function. The count of Manufacturer & Brand in mintel data is
       checked wrt brands in established brands, and the combination of country and brands is checked wrt country and brands in brand source & brands and new brands are inserted in CLEAN_MINTEL collection.
       @:param ts: Timestamp
       @:type: int64'''
    connection = connect_mongo()
    previous_data = connection[Settings.BRAND_SOURCE].find({}, {"_id":0})
    mongo_data = pd.DataFrame(list(previous_data))
    mongo_data['UPPER_BRAND_2'] = mongo_data['brand'].astype(str).str.upper()
    mongo_data['UPPER_COUNTRY_2'] = mongo_data['country'].astype(str).str.upper()
    established_brands = connection[Settings.ESTABLISHED_BRANDS].find({},{"_id":0})
    famous_brands = pd.DataFrame(list(established_brands))
    famous_brands.rename(columns={'name': 'Brand'}, inplace=True)
    famous_brands['UPPER_BRAND_1'] = famous_brands['Brand'].astype(str).str.upper()
    brands_data = connection[Settings.BRANDS].find({}, {"_id":0})
    brands = pd.DataFrame(list(previous_data))
    nielsendata = connection[Settings.NIELSEN_DATA].find({"ts":ts},{"_id":0})
    nielsen = pd.DataFrame(list(nielsendata))
    if 'UPPER_COUNTRY' in nielsen:
        countries = nielsen['UPPER_COUNTRY'].unique()
        # countries = ["USA"]
        for country in countries:
            print("Processing data for: ", country)
            data = nielsen[nielsen['UPPER_COUNTRY'] == country]
            print("Original Data shape: ", data.shape)
            data = dropDuplicateBrands(data)
            print("Data shape after duplicate removal: ", data.shape)
            data = dropDiscardedBrands(data)
            print("Data shape after Discarded removal: ", data.shape)
            data = dropEstablishedBrands(data,famous_brands)
            print("Data shape after Established removal: ", data.shape)
            data.reset_index(drop=True, inplace=True)
            data = getPotentialDuplicates(data)
            data.reset_index(drop=True, inplace=True)
            print(data)
            mlength = len(data)
            for i in range(mlength):
                doc = {}
                for item in data:
                    doc[item] = data[item][i]
                print(doc)
                n = {}
                for k, v in doc.items():
                    print("k==" + str(k) + " v==" + str(v))
                    if isinstance(v, np.int64):
                        v = int(v)
                    n[k] = v

                m_count = connection[Settings.ESTABLISHED_BRANDS].count({"name_low": str(n['MANUFACTURER']).lower()})
                b_count = connection[Settings.ESTABLISHED_BRANDS].count({"name_low": str(n['UPPER_BRAND']).lower()})
                if m_count==0 and b_count==0:
                     temp_var = str(n['UPPER_BRAND']).lower()
                     bs_brand_count = connection[Settings.BRAND_SOURCE].count(query={"brand_low":
                                                                                         {"$regex":temp_var,
                                                                                          "$options": 'i'}
                                                                                     })
                     # bs_brand_count = connection[Settings.BRAND_SOURCE].count({"brand_low": str(n['UPPER_BRAND']).lower()})
                     bs_country_count = connection[Settings.BRAND_SOURCE].count({"country": str(n['UPPER_COUNTRY']).lower()})
                     if bs_brand_count==0 and bs_country_count==0:
                         brand_count = connection[Settings.BRANDS].count({str(["Keyword"]).lower(): str(n['UPPER_BRAND']).lower()})
                         if brand_count == 0:
                            connection[Settings.CLEAN_NIELSEN].insert_one(n)
                            sleep(0.1)



cleaning(ts)
main(market_name,ts)
            #prebingpostclean(country,ts)