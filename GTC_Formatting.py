import pandas as pd
import numpy as np
from Kazakhstan import kazakhstan_index
import xlsxwriter



def gtc_common():
    ''' This function read raw gtc file and converts it into a dataframe. Changes to data are made according to the instruction file.
    gtc_common() includes data for 22 countries having the same format. The formatted data is then stored on an excel File - "gtc-output.xlsx"'''

    df_workbook = pd.read_excel('GTC.xlsx',sheet_name = None)
    df_gtc = pd.DataFrame()
    for _, sheet in df_workbook.items():
            df_gtc = df_gtc.append(sheet)

    df_gtc = df_gtc.drop(df_gtc.columns[3], axis=1)
    df_gtc = df_gtc.reset_index(drop=True)
    df_gtc.insert(0, 'COUNTRY', " ")
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Japan','JAPAN',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Thailand','THAILAND',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Philippines','PHILIPPINES',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Vietnam','VIETNAM',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Indonesia','INDONESIA',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Nigeria','NIGERIA',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Algeria','ALGERIA',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Egypt','EGYPT',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Morocco','MOROCCO',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Pakistan','PAKISTAN',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Saudi Arabia','SAUDI ARABIA',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Italy','ITALY',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Romania','ROMANIA',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Spain','SPAIN',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Russia','RUSSIA',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Colombia','COLOMBIA',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Ecuador','ECUADOR',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Belgium','BELGIUM',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total France','FRANCE',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Netherlands','NETHERLANDS',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Poland','POLAND',df_gtc['COUNTRY'])
    df_gtc['COUNTRY'] = np.where(df_gtc['SDESC'] == 'Total Germany','GERMANY',df_gtc['COUNTRY'])
    df_gtc['SDESC.1'] = pd.to_datetime(df_gtc['SDESC.1'], errors='ignore')
    df_gtc['SDESC.1'] = df_gtc['SDESC.1'].apply(lambda x: x.strftime('%m/%y'))
    df_gtc['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
    df_gtc['Value $ (\'000)'].fillna(0, inplace=True)
    df_gtc['Wtd Dist (Max)'].fillna(0, inplace=True)
    df_gtc['Num Dist (Max)'].fillna(0, inplace=True)
    df_gtc_fin = df_gtc[(df_gtc['Volume in Unit Cases (\'000)'] == 0) & (df_gtc['Value $ (\'000)'] == 0) & (
                df_gtc['Wtd Dist (Max)'] == 0) & (df_gtc['Num Dist (Max)'] == 0)].index
    df_gtc.drop(df_gtc_fin, inplace=True)
    df_gtc.replace(r'\s+', np.nan, regex=True).replace('', np.nan)
    df_gtc['CATEGORY'] = df_gtc['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
    df_gtc['CATEGORY'] = df_gtc['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
    df_gtc['CATEGORY'] = df_gtc['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
    df_gtc['CATEGORY'] = df_gtc['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
    df_gtc['CATEGORY'] = df_gtc['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
    df_gtc.rename(columns={'SDESC': 'DESCRIPTION',
                             'BRAND OWNER': 'MANUFACTURER',
                             'SDESC.1': 'PERIOD',
                             'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                             'Value $ (\'000)': 'SALES VALUE',
                             'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                             'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                             },
                    inplace=True)
    df_gtc = df_gtc.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    df_gtc.to_excel(writer, sheet_name="GTC Common", index=False)

def gtc_china():
    ''' This function formats data for China'''
    df_workbook_china = pd.read_excel('China.xlsx', sheet_name=None)
    df_gtc_china = pd.DataFrame()
    for _, sheet in df_workbook_china.items():
        df_gtc_china = df_gtc_china.append(sheet)
    df_gtc_china = df_gtc_china.drop(df_gtc_china.columns[3], axis=1)
    df_gtc_china.insert(0, 'COUNTRY', " ")
    df_gtc_china['COUNTRY'] = np.where(df_gtc_china['SDESC'] == 'Total China', 'CHINA', df_gtc_china['COUNTRY'])
    df_gtc_china['SDESC.1'] = pd.to_datetime(df_gtc_china['SDESC.1'], errors='ignore')
    df_gtc_china['SDESC.1'] = df_gtc_china['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
    df_gtc_china['SDESC'].fillna(" ", inplace=True)
    df_gtc_china['CATEGORY'].fillna(" ", inplace=True)
    df_gtc_china['BRAND'].fillna(" ", inplace=True)
    df_gtc_china['BRAND OWNER'].fillna(" ", inplace=True)
    df_gtc_china['SDESC.1'].fillna(" ", inplace=True)
    df_gtc_china['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
    df_gtc_china['Value $ (\'000)'].fillna(0, inplace=True)
    df_gtc_china['Wtd Dist (Max)'].fillna(0, inplace=True)
    df_gtc_china['Num Dist (Max)'].fillna(0, inplace=True)
    df_gtc_china_fin = df_gtc_china[(df_gtc_china['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_china['Value $ (\'000)'] == 0) & (
                df_gtc_china['Wtd Dist (Max)'] == 0) & (df_gtc_china['Num Dist (Max)'] == 0)].index
    df_gtc_china.drop(df_gtc_china_fin, inplace=True)
    df_gtc_china.replace(r'\s+', np.nan, regex=True).replace('', np.nan)
    df_gtc_china['CATEGORY'] = df_gtc_china['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
    df_gtc_china['CATEGORY'] = df_gtc_china['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
    df_gtc_china['CATEGORY'] = df_gtc_china['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
    df_gtc_china['CATEGORY'] = df_gtc_china['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
    df_gtc_china['CATEGORY'] = df_gtc_china['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
    df_gtc_china.rename(columns={'SDESC': 'DESCRIPTION',
                             'BRAND OWNER': 'MANUFACTURER',
                             'SDESC.1': 'PERIOD',
                             'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                             'Value $ (\'000)': 'SALES VALUE',
                             'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                             'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                             },
                    inplace=True)
    df_gtc_china = df_gtc_china.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    df_gtc_china.to_excel(writer, sheet_name="China", index=False)
def gtc_UK():
    ''' This function formats data for UK'''
    df_workbook_uk = pd.read_excel('GB.xlsx', sheet_name=None)
    df_gtc_uk = pd.DataFrame()
    for _, sheet in df_workbook_uk.items():
        df_gtc_uk = df_gtc_uk.append(sheet)
    df_gtc_uk = df_gtc_uk.drop(df_gtc_uk.columns[3], axis=1)
    df_gtc_uk.insert(0, 'COUNTRY', " ")
    df_gtc_uk['COUNTRY'] = np.where(df_gtc_uk['SDESC'] == 'Total GB', 'UK', df_gtc_uk['COUNTRY'])
    df_gtc_uk['SDESC.1'] = pd.to_datetime(df_gtc_uk['SDESC.1'], errors='ignore')
    df_gtc_uk['SDESC.1'] = df_gtc_uk['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
    df_gtc_uk['SDESC'].fillna(" ", inplace=True)
    df_gtc_uk['CATEGORY'].fillna(" ", inplace=True)
    df_gtc_uk['BRAND'].fillna(" ", inplace=True)
    df_gtc_uk['BRAND OWNER'].fillna(" ", inplace=True)
    df_gtc_uk['SDESC.1'].fillna(" ", inplace=True)
    df_gtc_uk['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
    df_gtc_uk['Value $ (\'000)'].fillna(0, inplace=True)
    df_gtc_uk['Wtd Dist (Max)'].fillna(0, inplace=True)
    df_gtc_uk['Num Dist (Max)'].fillna(0, inplace=True)
    df_gtc_uk_fin = df_gtc_uk[(df_gtc_uk['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_uk['Value $ (\'000)'] == 0) & (
                df_gtc_uk['Wtd Dist (Max)'] == 0) & (df_gtc_uk['Num Dist (Max)'] == 0)].index
    df_gtc_uk.drop(df_gtc_uk_fin, inplace=True)
    df_gtc_uk.replace(r'\s+', np.nan, regex=True).replace('', np.nan)
    df_gtc_uk['CATEGORY'] = df_gtc_uk['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
    df_gtc_uk['CATEGORY'] = df_gtc_uk['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
    df_gtc_uk['CATEGORY'] = df_gtc_uk['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
    df_gtc_uk['CATEGORY'] = df_gtc_uk['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
    df_gtc_uk['CATEGORY'] = df_gtc_uk['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
    df_gtc_uk.rename(columns={'SDESC': 'DESCRIPTION',
                              'BRAND OWNER': 'MANUFACTURER',
                              'SDESC.1': 'PERIOD',
                              'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                              'Value $ (\'000)': 'SALES VALUE',
                              'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                              'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                              },
                     inplace=True)
    df_gtc_uk = df_gtc_uk.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    df_gtc_uk.to_excel(writer, sheet_name="UK", index=False)
def gtc_mexico():
    ''' This function formats data for mexico'''
    df_workbook_mexico = pd.read_excel('GB.xlsx', sheet_name=None)
    df_gtc_mexico = pd.DataFrame()
    for _, sheet in df_workbook_mexico.items():
        df_gtc_mexico = df_gtc_mexico.append(sheet)
    df_gtc_mexico = df_gtc_mexico.drop(df_gtc_mexico.columns[3], axis=1)
    df_gtc_mexico.insert(0, 'COUNTRY', " ")
    df_gtc_mexico['COUNTRY'] = np.where(df_gtc_mexico['SDESC'] == 'Total Mexico', 'MEXICO', df_gtc_mexico['COUNTRY'])

    df_gtc_mexico['SDESC.1'] = pd.to_datetime(df_gtc_mexico['SDESC.1'], errors='ignore')
    df_gtc_mexico['SDESC.1'] = df_gtc_mexico['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
    df_gtc_mexico['SDESC'].fillna(" ", inplace=True)
    df_gtc_mexico['CATEGORY'].fillna(" ", inplace=True)
    df_gtc_mexico['BRAND'].fillna(" ", inplace=True)
    df_gtc_mexico['BRAND OWNER'].fillna(" ", inplace=True)
    df_gtc_mexico['SDESC.1'].fillna(" ", inplace=True)
    df_gtc_mexico['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
    df_gtc_mexico['Value $ (\'000)'].fillna(0, inplace=True)
    df_gtc_mexico['Wtd Dist (Max)'].fillna(0, inplace=True)
    df_gtc_mexico['Num Dist (Max)'].fillna(0, inplace=True)
    df_gtc_mexico_fin = df_gtc_mexico[(df_gtc_mexico['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_mexico['Value $ (\'000)'] == 0) & (
                df_gtc_mexico['Wtd Dist (Max)'] == 0) & (df_gtc_mexico['Num Dist (Max)'] == 0)].index
    df_gtc_mexico.drop(df_gtc_mexico_fin, inplace=True)
    df_gtc_mexico.replace(r'\s+', np.nan, regex=True).replace('', np.nan)
    df_gtc_mexico['CATEGORY'] = df_gtc_mexico['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
    df_gtc_mexico['CATEGORY'] = df_gtc_mexico['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
    df_gtc_mexico['CATEGORY'] = df_gtc_mexico['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
    df_gtc_mexico['CATEGORY'] = df_gtc_mexico['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
    df_gtc_mexico['CATEGORY'] = df_gtc_mexico['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
    df_gtc_mexico.rename(columns={'SDESC': 'DESCRIPTION',
                              'BRAND OWNER': 'MANUFACTURER',
                              'SDESC.1': 'PERIOD',
                              'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                              'Value $ (\'000)': 'SALES VALUE',
                              'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                              'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                              },
                     inplace=True)
    df_gtc_mexico = df_gtc_mexico.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    df_gtc_mexico.to_excel(writer, sheet_name="Mexico", index=False)

def gtc_india():
    ''' This function formats data for india. Raw data for India is in 6 different sheets having different formats. Sheets with same format are concatinated into one dataframe and formatted data is stored in gtc-output under sheet name "India"'''
    df_india_1 = pd.read_excel('Energy India.xlsx', sheet_name='Sheet1', ignore_index=True)
    df_india_2 = pd.read_excel('Juice India.xlsx', sheet_name='Sheet1', ignore_index=True)
    df_india_3 = pd.read_excel('SSD India.xlsx', sheet_name='Sheet1', ignore_index=True)
    df_india1 = pd.concat([df_india_1, df_india_2, df_india_3])
    df_india1['SDESC.2'] = pd.to_datetime(df_india1['SDESC.2'], errors='ignore')
    df_india1['SDESC.2'] = df_india1['SDESC.2'].apply(lambda x: x.strftime('%m/%y'))
    df_india1.rename(columns={'SDESC.2': 'PERIOD'}, inplace=True)
    df_india1 = df_india1.drop(df_india1.columns[1], axis=1)
    df_india1 = df_india1[
        ['SDESC', 'CATEGORY', 'BRAND OWNER', 'BRAND', 'PERIOD', 'Volume in Litres (\'000)', 'Value $ (\'000)',
         'Wtd Dist (Max)',
         'Num Dist (Max)']]

    df_india_4 = pd.read_excel('RTD Tea.xlsx', sheet_name='Sheet1', ignore_index=True)
    df_india_5 = pd.read_excel('Sports.xlsx', sheet_name='Sheet1', ignore_index=True)
    df_india_6 = pd.read_excel('Water.xlsx', sheet_name='Sheet1', ignore_index=True)
    df_india2 = pd.concat([df_india_4, df_india_5, df_india_6])
    df_india2['SDESC.1'] = pd.to_datetime(df_india2['SDESC.1'], errors='ignore')
    df_india2['SDESC.1'] = df_india2['SDESC.1'].apply(lambda x: x.strftime('%m/%y'))
    df_india2.rename(columns={'SDESC.1': 'PERIOD'}, inplace=True)
    df_india2 = df_india2.drop(df_india2.columns[2], axis=1)
    df_india2 = df_india2[
        ['SDESC', 'CATEGORY', 'BRAND OWNER', 'BRAND', 'PERIOD', 'Volume in Litres (\'000)', 'Value $ (\'000)',
         'Wtd Dist (Max)',
         'Num Dist (Max)']]

    df_gtc_india = pd.concat([df_india1, df_india2])

    df_gtc_india.insert(0, 'COUNTRY', 'INDIA')

    df_gtc_india_fin = df_gtc_india[(df_gtc_india['Volume in Litres (\'000)'] == 0) & (df_gtc_india['Value $ (\'000)'] == 0) & (
                df_gtc_india['Wtd Dist (Max)'] == 0) & (df_gtc_india['Num Dist (Max)'] == 0)].index
    df_gtc_india.drop(df_gtc_india_fin, inplace=True)
    df_gtc_india.replace(r'\s+', np.nan, regex=True).replace('', np.nan)
    df_gtc_india.replace(r'\s+', np.nan, regex=True).replace('', np.nan)
    df_gtc_india['CATEGORY'] = df_gtc_india['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
    df_gtc_india['CATEGORY'] = df_gtc_india['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
    df_gtc_india['CATEGORY'] = df_gtc_india['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
    df_gtc_india['CATEGORY'] = df_gtc_india['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
    df_gtc_india['CATEGORY'] = df_gtc_india['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
    df_gtc_india.rename(columns={'SDESC': 'DESCRIPTION',
                              'BRAND OWNER': 'MANUFACTURER',
                              'Volume in Litres (\'000)': 'SALES VOLUME',
                              'Value $ (\'000)': 'SALES VALUE',
                              'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                              'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                              },
                     inplace=True)

    df_gtc_india = df_gtc_india.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    df_gtc_india.to_excel(writer, sheet_name="India", index=False)
def gtc_kazakhstan():
    kazakhstan_index()
    df_gtc_13 = pd.read_excel('KazakhstanOutput.xlsx', ignore_index=True)
    df_gtc_13 = df_gtc_13.drop(df_gtc_13.columns[1], axis=1)
    df_gtc_13.insert(0, 'COUNTRY', "Kazakhstan")
    df_gtc_13['PERIOD'] = pd.to_datetime(df_gtc_13['PERIOD'], errors='ignore')
    df_gtc_13_fin = df_gtc_13[(df_gtc_13['Volume in Litres (\'000)'] == 0) & (df_gtc_13['Value $ (\'000)'] == 0) & (
                df_gtc_13['Wtd Dist (Max)'] == 0) & (df_gtc_13['Num Dist (Max)'] == 0)].index
    df_gtc_13.drop(df_gtc_13_fin, inplace=True)
    df_gtc_13.rename(columns={'SDESC': 'DESCRIPTION',
                              'BRAND OWNER': 'MANUFACTURER',
                              'Value $ (\'000)': 'SALES VALUE',
                              'Volume in Litres (\'000)': 'SALES VOLUME',
                              'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                              'Num Dist (Max)': 'NUMERIC DISTRIBUTION'},
                     inplace=True)
    df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
    df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
    df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
    df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
    df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
    df_gtc_13 = df_gtc_13.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    df_gtc_13 = df_gtc_13[
        ['COUNTRY', 'DESCRIPTION', 'CATEGORY', 'MANUFACTURER', 'BRAND', 'PERIOD', 'SALES VOLUME', 'SALES VALUE',
         'WEIGHTED DISTRIBUTION', 'NUMERIC DISTRIBUTION']]


writer = pd.ExcelWriter('gtc-output.xlsx', engine='xlsxwriter')
writer.save()

gtc_common()
gtc_china()
gtc_mexico()
gtc_UK()
gtc_india()
gtc_kazakhstan()