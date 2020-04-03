import pandas as pd
import numpy as np
import datetime as dt
import xlsxwriter
#################Sheet1#########################
df_gtc_1 = pd.read_excel('GTC_Countries(2).xlsx', sheet_name='Sheet1')
df_gtc_1 = df_gtc_1.drop(df_gtc_1.columns[3], axis=1)
df_gtc_1.insert(0, 'COUNTRY', " ")
df_gtc_1['COUNTRY'] = np.where(df_gtc_1['SDESC'] == 'Total Japan','JAPAN',df_gtc_1['COUNTRY'])
df_gtc_1['COUNTRY'] = np.where(df_gtc_1['SDESC'] == 'Total Thailand','THAILAND',df_gtc_1['COUNTRY'])
df_gtc_1['COUNTRY'] = np.where(df_gtc_1['SDESC'] == 'Total Philippines','PHILIPPINES',df_gtc_1['COUNTRY'])
df_gtc_1['COUNTRY'] = np.where(df_gtc_1['SDESC'] == 'Total Vietnam','VIETNAM',df_gtc_1['COUNTRY'])
df_gtc_1['SDESC.1'] = pd.to_datetime(df_gtc_1['SDESC.1'], errors = 'ignore')
df_gtc_1['SDESC.1'] = df_gtc_1['SDESC.1'].apply(lambda x: x.strftime('%m/%y'))
df_gtc_1_fin = df_gtc_1[(df_gtc_1['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_1['Value $ (\'000)'] == 0) & (df_gtc_1['Wtd Dist (Max)'] == 0) & (df_gtc_1['Num Dist (Max)'] == 0)].index
df_gtc_1.drop(df_gtc_1_fin, inplace=True)
df_gtc_1.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_1['CATEGORY'] = df_gtc_1['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_1['CATEGORY'] = df_gtc_1['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_1['CATEGORY'] = df_gtc_1['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_1['CATEGORY'] = df_gtc_1['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_1['CATEGORY'] = df_gtc_1['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_1.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_1 = df_gtc_1.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
#######################Sheet2#########################
df_gtc_2 = pd.read_excel('GTC_Countries(2).xlsx', sheet_name='Sheet2')
df_gtc_2 = df_gtc_2.drop(df_gtc_2.columns[3], axis=1)
df_gtc_2.insert(0, 'COUNTRY', " ")
df_gtc_2['COUNTRY'] = np.where(df_gtc_2['SDESC'] == 'Total Indonesia','INDONESIA',df_gtc_2['COUNTRY'])
df_gtc_2['SDESC.1'] = pd.to_datetime(df_gtc_2['SDESC.1'], errors = 'ignore')
df_gtc_2['SDESC.1'] = df_gtc_2['SDESC.1'].apply(lambda x: x.strftime('%m/%y'))
df_gtc_2['SDESC'].fillna(" ", inplace = True)
df_gtc_2['CATEGORY'].fillna(" ", inplace=True)
df_gtc_2['BRAND'].fillna(" ", inplace=True)
df_gtc_2['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_2['SDESC.1'].fillna(" ", inplace=True)
df_gtc_2['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_2['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_2['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_2['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_2_fin = df_gtc_2[(df_gtc_2['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_2['Value $ (\'000)'] == 0) & (df_gtc_2['Wtd Dist (Max)'] == 0) & (df_gtc_2['Num Dist (Max)'] == 0)].index
df_gtc_2.drop(df_gtc_2_fin, inplace=True)
df_gtc_2.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_2['CATEGORY'] = df_gtc_2['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_2['CATEGORY'] = df_gtc_2['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_2['CATEGORY'] = df_gtc_2['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_2['CATEGORY'] = df_gtc_2['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_2['CATEGORY'] = df_gtc_2['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_2.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_2 = df_gtc_2.apply(lambda x: x.str.upper() if x.dtype == "object" else x)


#####################Sheet3#############################
df_gtc_3 = pd.read_excel('GTC_Countries(2).xlsx', sheet_name='Sheet3')
df_gtc_3 = df_gtc_3.drop(df_gtc_3.columns[3], axis=1)
df_gtc_3.insert(0, 'COUNTRY', " ")
df_gtc_3['COUNTRY'] = np.where(df_gtc_3['SDESC'] == 'Total Nigeria','NIGERIA',df_gtc_3['COUNTRY'])
df_gtc_3['SDESC.1'] = pd.to_datetime(df_gtc_3['SDESC.1'], errors = 'ignore')
df_gtc_3['SDESC.1'] = df_gtc_3['SDESC.1'].apply(lambda x: x.strftime('%m/%y'))
df_gtc_3['SDESC'].fillna(" ", inplace = True)
df_gtc_3['CATEGORY'].fillna(" ", inplace=True)
df_gtc_3['BRAND'].fillna(" ", inplace=True)
df_gtc_3['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_3['SDESC.1'].fillna(" ", inplace=True)
df_gtc_3['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_3['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_3['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_3['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_3_fin = df_gtc_3[(df_gtc_3['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_3['Value $ (\'000)'] == 0) & (df_gtc_3['Wtd Dist (Max)'] == 0) & (df_gtc_3['Num Dist (Max)'] == 0)].index
df_gtc_3.drop(df_gtc_3_fin, inplace=True)
df_gtc_3.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_3['CATEGORY'] = df_gtc_3['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_3['CATEGORY'] = df_gtc_3['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_3['CATEGORY'] = df_gtc_3['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_3['CATEGORY'] = df_gtc_3['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_3['CATEGORY'] = df_gtc_3['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_3.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_3 = df_gtc_3.apply(lambda x: x.str.upper() if x.dtype == "object" else x)

########################Sheet4##########################
df_gtc_4 = pd.read_excel('GTC_Countries(2).xlsx', sheet_name='Sheet4')
df_gtc_4 = df_gtc_4.drop(df_gtc_4.columns[3], axis=1)
df_gtc_4.insert(0, 'COUNTRY', " ")
df_gtc_4['COUNTRY'] = np.where(df_gtc_4['SDESC'] == 'Total Algeria','ALGERIA',df_gtc_4['COUNTRY'])
df_gtc_4['COUNTRY'] = np.where(df_gtc_4['SDESC'] == 'Total Egypt','EGYPT',df_gtc_4['COUNTRY'])
df_gtc_4['COUNTRY'] = np.where(df_gtc_4['SDESC'] == 'Total Morocco','MOROCCO',df_gtc_4['COUNTRY'])
df_gtc_4['COUNTRY'] = np.where(df_gtc_4['SDESC'] == 'Total Pakistan','PAKISTAN',df_gtc_4['COUNTRY'])
df_gtc_4['COUNTRY'] = np.where(df_gtc_4['SDESC'] == 'Total Saudi Arabia','SAUDI ARABIA',df_gtc_4['COUNTRY'])
df_gtc_4['SDESC.1'] = pd.to_datetime(df_gtc_4['SDESC.1'], errors = 'ignore')
df_gtc_4['SDESC.1'] = df_gtc_4['SDESC.1'].apply(lambda x: x.strftime('%m/%y'))
df_gtc_4['SDESC'].fillna(" ", inplace = True)
df_gtc_4['CATEGORY'].fillna(" ", inplace=True)
df_gtc_4['BRAND'].fillna(" ", inplace=True)
df_gtc_4['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_4['SDESC.1'].fillna(" ", inplace=True)
df_gtc_4['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_4['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_4['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_4['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_4_fin = df_gtc_4[(df_gtc_4['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_4['Value $ (\'000)'] == 0) & (df_gtc_4['Wtd Dist (Max)'] == 0) & (df_gtc_4['Num Dist (Max)'] == 0)].index
df_gtc_4.drop(df_gtc_4_fin, inplace=True)
df_gtc_4.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_4['CATEGORY'] = df_gtc_4['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_4['CATEGORY'] = df_gtc_4['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_4['CATEGORY'] = df_gtc_4['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_4['CATEGORY'] = df_gtc_4['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_4['CATEGORY'] = df_gtc_4['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_4.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_4 = df_gtc_4.apply(lambda x: x.str.upper() if x.dtype == "object" else x)

########################Sheet5##########################
df_gtc_5 = pd.read_excel('GTC_Countries(2).xlsx', sheet_name='Sheet5')
df_gtc_5 = df_gtc_5.drop(df_gtc_5.columns[3], axis=1)
df_gtc_5.insert(0, 'COUNTRY', " ")
df_gtc_5['COUNTRY'] = np.where(df_gtc_5['SDESC'] == 'Total Italy','ITALY',df_gtc_5['COUNTRY'])
df_gtc_5['COUNTRY'] = np.where(df_gtc_5['SDESC'] == 'Total Romania','ROMANIA',df_gtc_5['COUNTRY'])
df_gtc_5['COUNTRY'] = np.where(df_gtc_5['SDESC'] == 'Total Spain','SPAIN',df_gtc_5['COUNTRY'])
df_gtc_5['COUNTRY'] = np.where(df_gtc_5['SDESC'] == 'Total Russia','RUSSIA',df_gtc_5['COUNTRY'])
df_gtc_5['SDESC.1'] = pd.to_datetime(df_gtc_5['SDESC.1'], errors = 'ignore')
df_gtc_5['SDESC.1'] = df_gtc_5['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
df_gtc_5['SDESC'].fillna(" ", inplace = True)
df_gtc_5['CATEGORY'].fillna(" ", inplace=True)
df_gtc_5['BRAND'].fillna(" ", inplace=True)
df_gtc_5['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_5['SDESC.1'].fillna(" ", inplace=True)
df_gtc_5['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_5['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_5['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_5['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_5_fin = df_gtc_5[(df_gtc_5['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_5['Value $ (\'000)'] == 0) & (df_gtc_5['Wtd Dist (Max)'] == 0) & (df_gtc_5['Num Dist (Max)'] == 0)].index
df_gtc_5.drop(df_gtc_5_fin, inplace=True)
df_gtc_5.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_5['CATEGORY'] = df_gtc_5['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_5['CATEGORY'] = df_gtc_5['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_5['CATEGORY'] = df_gtc_5['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_5['CATEGORY'] = df_gtc_5['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_5['CATEGORY'] = df_gtc_5['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_5.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_5 = df_gtc_5.apply(lambda x: x.str.upper() if x.dtype == "object" else x)

#########################Sheet6###########################
df_gtc_6 = pd.read_excel('GTC_Countries(2).xlsx', sheet_name='Sheet6')
df_gtc_6 = df_gtc_6.drop(df_gtc_6.columns[3], axis=1)
df_gtc_6.insert(0, 'COUNTRY', " ")
df_gtc_6['COUNTRY'] = np.where(df_gtc_6['SDESC'] == 'Total Colombia','COLOMBIA',df_gtc_6['COUNTRY'])
df_gtc_6['COUNTRY'] = np.where(df_gtc_6['SDESC'] == 'Total Ecuador','ECUADOR',df_gtc_6['COUNTRY'])
df_gtc_6['SDESC.1'] = pd.to_datetime(df_gtc_6['SDESC.1'], errors = 'ignore')
df_gtc_6['SDESC.1'] = df_gtc_6['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
df_gtc_6['SDESC'].fillna(" ", inplace = True)
df_gtc_6['CATEGORY'].fillna(" ", inplace=True)
df_gtc_6['BRAND'].fillna(" ", inplace=True)
df_gtc_6['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_6['SDESC.1'].fillna(" ", inplace=True)
df_gtc_6['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_6['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_6['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_6['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_6_fin = df_gtc_6[(df_gtc_6['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_6['Value $ (\'000)'] == 0) & (df_gtc_6['Wtd Dist (Max)'] == 0) & (df_gtc_6['Num Dist (Max)'] == 0)].index
df_gtc_6.drop(df_gtc_6_fin, inplace=True)
df_gtc_6.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_6['CATEGORY'] = df_gtc_6['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_6['CATEGORY'] = df_gtc_6['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_6['CATEGORY'] = df_gtc_6['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_6['CATEGORY'] = df_gtc_6['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_6['CATEGORY'] = df_gtc_6['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_6.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_6 = df_gtc_6.apply(lambda x: x.str.upper() if x.dtype == "object" else x)

#######################Sheet7##########################
df_gtc_7 = pd.read_excel('GTC_Countries(2).xlsx', sheet_name='Sheet7')
df_gtc_7 = df_gtc_7.drop(df_gtc_7.columns[3], axis=1)
df_gtc_7.insert(0, 'COUNTRY', " ")
df_gtc_7['COUNTRY'] = np.where(df_gtc_7['SDESC'] == 'Total Belgium','BELGIUM',df_gtc_7['COUNTRY'])
df_gtc_7['COUNTRY'] = np.where(df_gtc_7['SDESC'] == 'Total France','FRANCE',df_gtc_7['COUNTRY'])
df_gtc_7['COUNTRY'] = np.where(df_gtc_7['SDESC'] == 'Total Netherlands','NETHERLANDS',df_gtc_7['COUNTRY'])
df_gtc_7['SDESC.1'] = pd.to_datetime(df_gtc_7['SDESC.1'], errors = 'ignore')
df_gtc_7['SDESC.1'] = df_gtc_7['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
df_gtc_7['SDESC'].fillna(" ", inplace = True)
df_gtc_7['CATEGORY'].fillna(" ", inplace=True)
df_gtc_7['BRAND'].fillna(" ", inplace=True)
df_gtc_7['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_7['SDESC.1'].fillna(" ", inplace=True)
df_gtc_7['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_7['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_7['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_7['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_7_fin = df_gtc_7[(df_gtc_7['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_7['Value $ (\'000)'] == 0) & (df_gtc_7['Wtd Dist (Max)'] == 0) & (df_gtc_7['Num Dist (Max)'] == 0)].index
df_gtc_7.drop(df_gtc_7_fin, inplace=True)
df_gtc_7.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_7['CATEGORY'] = df_gtc_7['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_7['CATEGORY'] = df_gtc_7['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_7['CATEGORY'] = df_gtc_7['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_7['CATEGORY'] = df_gtc_7['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_7['CATEGORY'] = df_gtc_7['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_7.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_7 = df_gtc_7.apply(lambda x: x.str.upper() if x.dtype == "object" else x)

##########################Sheet8#############################
df_gtc_8 = pd.read_excel('GTC_Countries(2).xlsx', sheet_name='Sheet8')
df_gtc_8 = df_gtc_8.drop(df_gtc_8.columns[3], axis=1)
df_gtc_8.insert(0, 'COUNTRY', " ")
df_gtc_8['COUNTRY'] = np.where(df_gtc_8['SDESC'] == 'Total Poland','POLAND',df_gtc_8['COUNTRY'])
df_gtc_8['COUNTRY'] = np.where(df_gtc_8['SDESC'] == 'Total Germany','GERMANY',df_gtc_8['COUNTRY'])

df_gtc_8['SDESC.1'] = pd.to_datetime(df_gtc_8['SDESC.1'], errors = 'ignore')
df_gtc_8['SDESC.1'] = df_gtc_8['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
df_gtc_8['SDESC'].fillna(" ", inplace = True)
df_gtc_8['CATEGORY'].fillna(" ", inplace=True)
df_gtc_8['BRAND'].fillna(" ", inplace=True)
df_gtc_8['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_8['SDESC.1'].fillna(" ", inplace=True)
df_gtc_8['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_8['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_8['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_8['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_8_fin = df_gtc_8[(df_gtc_8['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_8['Value $ (\'000)'] == 0) & (df_gtc_8['Wtd Dist (Max)'] == 0) & (df_gtc_8['Num Dist (Max)'] == 0)].index
df_gtc_8.drop(df_gtc_8_fin, inplace=True)
df_gtc_8.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_8['CATEGORY'] = df_gtc_8['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_8['CATEGORY'] = df_gtc_8['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_8['CATEGORY'] = df_gtc_8['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_8['CATEGORY'] = df_gtc_8['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_8['CATEGORY'] = df_gtc_8['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_8.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_8 = df_gtc_8.apply(lambda x: x.str.upper() if x.dtype == "object" else x)


######################Sheet9-China################
df_gtc_9 = pd.read_excel('China EBT.xlsx', sheet_name='China')
df_gtc_9 = df_gtc_9.drop(df_gtc_9.columns[3], axis=1)
df_gtc_9.insert(0, 'COUNTRY', " ")
df_gtc_9['COUNTRY'] = np.where(df_gtc_9['SDESC'] == 'Total China','CHINA',df_gtc_9['COUNTRY'])
df_gtc_9['SDESC.1'] = pd.to_datetime(df_gtc_9['SDESC.1'], errors = 'ignore')
df_gtc_9['SDESC.1'] = df_gtc_9['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
df_gtc_9['SDESC'].fillna(" ", inplace = True)
df_gtc_9['CATEGORY'].fillna(" ", inplace=True)
df_gtc_9['BRAND'].fillna(" ", inplace=True)
df_gtc_9['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_9['SDESC.1'].fillna(" ", inplace=True)
df_gtc_9['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_9['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_9['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_9['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_9_fin = df_gtc_9[(df_gtc_9['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_9['Value $ (\'000)'] == 0) & (df_gtc_9['Wtd Dist (Max)'] == 0) & (df_gtc_9['Num Dist (Max)'] == 0)].index
df_gtc_9.drop(df_gtc_9_fin, inplace=True)
df_gtc_9.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_9['CATEGORY'] = df_gtc_9['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_9['CATEGORY'] = df_gtc_9['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_9['CATEGORY'] = df_gtc_9['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_9['CATEGORY'] = df_gtc_9['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_9['CATEGORY'] = df_gtc_9['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_9.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_9 = df_gtc_9.apply(lambda x: x.str.upper() if x.dtype == "object" else x)

######################Sheet10 -UK################3
df_gtc_10 = pd.read_excel('GB.xlsx', sheet_name='GB')
df_gtc_10 = df_gtc_10.drop(df_gtc_10.columns[3], axis=1)
df_gtc_10.insert(0, 'COUNTRY', " ")
df_gtc_10['COUNTRY'] = np.where(df_gtc_10['SDESC'] == 'Total GB','UK',df_gtc_10['COUNTRY'])
df_gtc_10['SDESC.1'] = pd.to_datetime(df_gtc_10['SDESC.1'], errors = 'ignore')
df_gtc_10['SDESC.1'] = df_gtc_10['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
df_gtc_10['SDESC'].fillna(" ", inplace = True)
df_gtc_10['CATEGORY'].fillna(" ", inplace=True)
df_gtc_10['BRAND'].fillna(" ", inplace=True)
df_gtc_10['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_10['SDESC.1'].fillna(" ", inplace=True)
df_gtc_10['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_10['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_10['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_10['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_10_fin = df_gtc_10[(df_gtc_10['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_10['Value $ (\'000)'] == 0) & (df_gtc_10['Wtd Dist (Max)'] == 0) & (df_gtc_10['Num Dist (Max)'] == 0)].index
df_gtc_10.drop(df_gtc_10_fin, inplace=True)
df_gtc_10.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_10['CATEGORY'] = df_gtc_10['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_10['CATEGORY'] = df_gtc_10['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_10['CATEGORY'] = df_gtc_10['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_10['CATEGORY'] = df_gtc_10['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_10['CATEGORY'] = df_gtc_10['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_10.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_10 = df_gtc_10.apply(lambda x: x.str.upper() if x.dtype == "object" else x)

######################Sheet11 - Mexico###################
df_gtc_11 = pd.read_excel('Mexico.xlsx', sheet_name='Mexico')
df_gtc_11 = df_gtc_11.drop(df_gtc_11.columns[3], axis=1)
df_gtc_11.insert(0, 'COUNTRY', " ")
df_gtc_11['COUNTRY'] = np.where(df_gtc_11['SDESC'] == 'Total Mexico','MEXICO',df_gtc_11['COUNTRY'])

df_gtc_11['SDESC.1'] = pd.to_datetime(df_gtc_11['SDESC.1'], errors = 'ignore')
df_gtc_11['SDESC.1'] = df_gtc_11['SDESC.1'].apply(lambda x: x.strftime('%m/%y').upper())
df_gtc_11['SDESC'].fillna(" ", inplace = True)
df_gtc_11['CATEGORY'].fillna(" ", inplace=True)
df_gtc_11['BRAND'].fillna(" ", inplace=True)
df_gtc_11['BRAND OWNER'].fillna(" ", inplace=True)
df_gtc_11['SDESC.1'].fillna(" ", inplace=True)
df_gtc_11['Volume in Unit Cases (\'000)'].fillna(0, inplace=True)
df_gtc_11['Value $ (\'000)'].fillna(0, inplace=True)
df_gtc_11['Wtd Dist (Max)'].fillna(0, inplace=True)
df_gtc_11['Num Dist (Max)'].fillna(0, inplace=True)
df_gtc_11_fin = df_gtc_11[(df_gtc_11['Volume in Unit Cases (\'000)'] == 0) & (df_gtc_11['Value $ (\'000)'] == 0) & (df_gtc_11['Wtd Dist (Max)'] == 0) & (df_gtc_11['Num Dist (Max)'] == 0)].index
df_gtc_11.drop(df_gtc_11_fin, inplace=True)
df_gtc_11.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_11['CATEGORY'] = df_gtc_11['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_11['CATEGORY'] = df_gtc_11['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_11['CATEGORY'] = df_gtc_11['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_11['CATEGORY'] = df_gtc_11['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_11['CATEGORY'] = df_gtc_11['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_11.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'SDESC.1':'PERIOD',
                         'Volume in Unit Cases (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)
df_gtc_11 = df_gtc_11.apply(lambda x: x.str.upper() if x.dtype == "object" else x)

#########################Sheet 12 - India#######################
df_india_1 = pd.read_excel('Energy India.xlsx', sheet_name='Sheet1', ignore_index=True)
df_india_2 = pd.read_excel('Juice India.xlsx', sheet_name='Sheet1', ignore_index=True)
df_india_3 = pd.read_excel('SSD India.xlsx', sheet_name='Sheet1', ignore_index=True)
df_india1 = pd.concat([df_india_1, df_india_2, df_india_3])
df_india1['SDESC.2'] = pd.to_datetime(df_india1['SDESC.2'], errors = 'ignore')
df_india1['SDESC.2'] = df_india1['SDESC.2'].apply(lambda x: x.strftime('%m/%y'))
df_india1.rename(columns={'SDESC.2':'PERIOD'}, inplace=True)
df_india1 = df_india1.drop(df_india1.columns[1], axis=1)
df_india1 = df_india1[['SDESC', 'CATEGORY', 'BRAND OWNER', 'BRAND', 'PERIOD', 'Volume in Litres (\'000)', 'Value $ (\'000)', 'Wtd Dist (Max)',
'Num Dist (Max)']]



df_india_4 = pd.read_excel('RTD Tea.xlsx', sheet_name='Sheet1', ignore_index=True)
df_india_5 = pd.read_excel('Sports.xlsx', sheet_name='Sheet1', ignore_index=True)
df_india_6 =  pd.read_excel('Water.xlsx', sheet_name='Sheet1', ignore_index=True)
df_india2 = pd.concat([df_india_4, df_india_5, df_india_6])
df_india2['SDESC.1'] = pd.to_datetime(df_india2['SDESC.1'], errors = 'ignore')
df_india2['SDESC.1'] = df_india2['SDESC.1'].apply(lambda x: x.strftime('%m/%y'))
df_india2.rename(columns={'SDESC.1':'PERIOD'}, inplace=True)
df_india2 = df_india2.drop(df_india2.columns[2],axis=1)
df_india2 = df_india2[['SDESC', 'CATEGORY', 'BRAND OWNER', 'BRAND', 'PERIOD', 'Volume in Litres (\'000)', 'Value $ (\'000)', 'Wtd Dist (Max)',
'Num Dist (Max)']]




df_gtc_12 = pd.concat([df_india1, df_india2])

df_gtc_12.insert(0, 'COUNTRY', 'INDIA')

df_gtc_12_fin = df_gtc_12[(df_gtc_12['Volume in Litres (\'000)'] == 0) & (df_gtc_12['Value $ (\'000)'] == 0) & (df_gtc_12['Wtd Dist (Max)'] == 0) & (df_gtc_12['Num Dist (Max)'] == 0)].index
df_gtc_12.drop(df_gtc_12_fin, inplace=True)
df_gtc_12.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_12.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
df_gtc_12['CATEGORY'] = df_gtc_12['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_12['CATEGORY'] = df_gtc_12['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_12['CATEGORY'] = df_gtc_12['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_12['CATEGORY'] = df_gtc_12['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_12['CATEGORY'] = df_gtc_12['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_12.rename(columns={'SDESC': 'DESCRIPTION',
                         'BRAND OWNER': 'MANUFACTURER',
                         'Volume in Litres (\'000)': 'SALES VOLUME',
                         'Value $ (\'000)': 'SALES VALUE',
                         'Wtd Dist (Max)': 'WEIGHTED DISTRIBUTION',
                         'Num Dist (Max)': 'NUMERIC DISTRIBUTION'
                         },
                inplace=True)


df_gtc_12 = df_gtc_12.apply(lambda x: x.str.upper() if x.dtype == "object" else x)


#######################Sheet13-Kazakhstan##############
df_gtc_13 = pd.read_excel('KazakhstanOutput.xlsx', ignore_index=True)
df_gtc_13 = df_gtc_13.drop(df_gtc_13.columns[1], axis=1)
df_gtc_13.insert(0, 'COUNTRY', "Kazakhstan")
df_gtc_13['PERIOD'] = pd.to_datetime(df_gtc_13['PERIOD'], errors = 'ignore')
df_gtc_13_fin = df_gtc_13[(df_gtc_13['Volume in Litres (\'000)'] == 0) & (df_gtc_13['Value $ (\'000)'] == 0) & (df_gtc_13['Wtd Dist (Max)'] == 0) & (df_gtc_13['Num Dist (Max)'] == 0)].index
df_gtc_13.drop(df_gtc_13_fin, inplace=True)
df_gtc_13.rename(columns={'SDESC': 'DESCRIPTION',
                          'BRAND OWNER': 'MANUFACTURER',
                          'Value $ (\'000)':'SALES VALUE',
                          'Volume in Litres (\'000)':'SALES VOLUME',
                          'Wtd Dist (Max)':'WEIGHTED DISTRIBUTION',
                          'Num Dist (Max)': 'NUMERIC DISTRIBUTION'},
                 inplace=True)
df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL CORE SPARKLING", "CARBONATED SOFT DRINKS")
df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL JUICES AND JUICE DRINKS", "JUICE DRINKS")
df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL ENERGY", "ENERGY & SPORTS DRINKS")
df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL RTD TEA", "PACKAGES TEA & COFFEE")
df_gtc_13['CATEGORY'] = df_gtc_13['CATEGORY'].replace("TOTAL SPORTS", "ENERGY & SPORTS DRINKS")
df_gtc_13 = df_gtc_13.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
df_gtc_13 = df_gtc_13[['COUNTRY', 'DESCRIPTION', 'CATEGORY', 'MANUFACTURER', 'BRAND', 'PERIOD', 'SALES VOLUME', 'SALES VALUE', 'WEIGHTED DISTRIBUTION', 'NUMERIC DISTRIBUTION']]


##################Combine All Sheets in One File############
writer = pd.ExcelWriter('gtcoutput1.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df_gtc_1.to_excel(writer, sheet_name='Sheet1', index=False)
df_gtc_2.to_excel(writer, sheet_name='Sheet2', index=False)
df_gtc_3.to_excel(writer, sheet_name='Sheet3', index=False)
df_gtc_4.to_excel(writer, sheet_name='Sheet4', index=False)
df_gtc_5.to_excel(writer, sheet_name='Sheet5', index=False)
df_gtc_6.to_excel(writer, sheet_name='Sheet6', index=False)
df_gtc_6.to_excel(writer, sheet_name='Sheet6', index=False)
df_gtc_7.to_excel(writer, sheet_name='Sheet7', index=False)
df_gtc_8.to_excel(writer, sheet_name='Sheet8', index=False)
df_gtc_9.to_excel(writer, sheet_name='Sheet9', index=False)
df_gtc_10.to_excel(writer, sheet_name='Sheet10', index=False)
df_gtc_11.to_excel(writer, sheet_name='Sheet11', index=False)
df_gtc_12.to_excel(writer, sheet_name='Sheet12', index=False)
df_gtc_13.to_excel(writer, sheet_name='Sheet13', index=False)

writer.save()
