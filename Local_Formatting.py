import pandas as pd
import numpy as np
import datetime
from pandas import ExcelWriter
import xlsxwriter
##########ARGENTINA####################
def acpb():
        #Merge All Sheets in One
        df_argentina = pd.concat(pd.read_excel('Emerging Brands - Global (6).xlsx', sheet_name=['SSDs AR', 'Plain AR', 'Flavor AR', 'RTD AR', 'Sport AR']),ignore_index=True, sort=False )
        #Drop columns not required
        df_argentina = df_argentina.drop(df_argentina.columns[[2, 9, 12]], axis=1)

        df_argentina["COUNTRY"].fillna(method='ffill', inplace=True)
        #df_argentina['SDESC.1'] = pd.to_datetime(df_argentina['SDESC.1'].str.strip(), format = '%m/%y',errors = 'ignore')


        #Replace Names of Columns
        df_argentina.rename(columns={'SDESC':'DESCRIPTION',
                                  'SDESC.1' :'PERIOD',
                                  'VENTAS UNIT CASES (\'000)':'SALES VOLUME',
                                  'VENTAS EN VALORES PESOS (\'000)':'SALES VALUE',
                                  'DISTRIBUCION FISICA': 'NUMERIC DISTRIBUTION',
                                  'DISTRIBUCION PONDERADA': 'WEIGHTED DISTRIBUTION'},
                         inplace=True)



        #Translate Names in Categories & Period Column
        df_argentina["CATEGORY"]= df_argentina["CATEGORY"].str.replace("BEBIDAS GASEOSAS", "CARBONATED SOFT DRINKS" )
        df_argentina["CATEGORY"]= df_argentina["CATEGORY"].replace("AGUAS MINERALES+SODAS+AGUAS PO", "TOTAL WATER")
        df_argentina["CATEGORY"]= df_argentina["CATEGORY"].str.replace("JUGOS", "JUICE DRINKS")
        df_argentina["PERIOD"]= df_argentina["PERIOD"].replace(regex={r'^ENE': 'JAN', '^ABR': 'APR',  '^AGO': 'AUG', '^DIC' : 'DEC'})
        df_argentina["PERIOD"] = df_argentina["PERIOD"].astype('datetime64[ns]')
        #df_argentina["PERIOD"] = pd.to_datetime(df_argentina["PERIOD"], format="%m/%y")
        df_argentina["PERIOD"]=df_argentina["PERIOD"].apply(lambda x: x.strftime('%m/%y'))
        #Fill Null Values with either Empty String or 0
        df_argentina["DESCRIPTION"].fillna(" ", inplace = True)
        df_argentina["CATEGORY"].fillna(" ", inplace=True)
        df_argentina["BRAND"].fillna(" ", inplace=True)
        df_argentina["MANUFACTURER"].fillna(" ", inplace=True)
        df_argentina["PERIOD"].fillna(" ", inplace=True)
        df_argentina["SALES VALUE"].fillna(0, inplace=True)
        df_argentina["SALES VOLUME"].fillna(0, inplace=True)
        df_argentina["NUMERIC DISTRIBUTION"].fillna(0, inplace=True)
        df_argentina["WEIGHTED DISTRIBUTION"].fillna(0, inplace=True)
        #Drop row with columns where Sales Value , Sales Volume, Numeric Distribution & Weighted Distribution is 0
        df_argentina_fin = df_argentina[(df_argentina['SALES VALUE'] == 0) & (df_argentina['SALES VOLUME'] == 0) & (df_argentina['NUMERIC DISTRIBUTION'] == 0) & (df_argentina['WEIGHTED DISTRIBUTION'] == 0)].index

        df_argentina.drop(df_argentina_fin, inplace=True)
##############CHILE################

        df_chile_1 = pd.concat(pd.read_excel('Emerging Brands - Global (6).xlsx', sheet_name= ['SSDs CL', 'RTD CL', 'Sport CL']))
        df_chile_1.rename(columns={'CATEGORIA': 'CATEGORY'}, inplace=True)

        df_chile_2 = pd.concat(pd.read_excel('Emerging Brands - Global (6).xlsx', sheet_name=['Plain CL', 'Flavor CL']))
        df_chile_2.rename(columns={'SEGMENTO': 'CATEGORY'}, inplace = True)

        df_chile = pd.concat([df_chile_1, df_chile_2])
        df_chile = df_chile.drop(df_chile.columns[[2, 9, 12]], axis = 1)
        #df_chile['SDESC.1'] = pd.to_datetime(df_chile['SDESC.1'].str.strip(), format= '%m/%y', errors = 'ignore')
        #df_chile['SDESC.1'] = df_chile['SDESC.1'].apply(lambda x: x.strftime('%m/%y'))

        df_chile["COUNTRY"].fillna( method ='ffill', inplace = True)
        df_chile.rename(columns={'SDESC':'DESCRIPTION',
                                  'SDESC.1':'PERIOD',
                                  'FABRICANTE' : 'MANUFACTURER',
                                  'MARCA': 'BRAND',
                                  'VENTAS C.UNITARIAS (\'000)':'SALES VOLUME',
                                  'VENTAS EN VALOR PESOS (\'000)':'SALES VALUE',
                                  'DIST. NUM.  MANEJANTES': 'NUMERIC DISTRIBUTION',
                                  'DIST. POND. MANEJANTES': 'WEIGHTED DISTRIBUTION',
                                  },
                         inplace=True)


        df_chile["CATEGORY"]= df_chile["CATEGORY"].replace("GASEOSAS", "CARBONATED SOFT DRINKS" )
        df_chile["CATEGORY"]= df_chile["CATEGORY"].replace("A.PURIFICADAS", "TOTAL WATER")
        df_chile["CATEGORY"]= df_chile["CATEGORY"].replace("A.SABORIZADAS", "TOTAL WATER")
        df_chile["CATEGORY"]= df_chile["CATEGORY"].replace("A.MINERALES", "TOTAL WATER")
        df_chile["CATEGORY"]= df_chile["CATEGORY"].replace("JUGOS RTD", "JUICE DRINKS")
        df_chile["CATEGORY"]= df_chile["CATEGORY"].replace("BEBIDAS DEPORTIVAS", "SPORTS & ENERGY DRINKS")
        df_chile["PERIOD"] = df_chile["PERIOD"].replace(regex={r'^Enero': 'JAN', '^Febrero': 'FEB', '^Marzo': 'MAR', '^Abril' : 'APR', '^Mayo' : 'MAY', '^Junio': 'JUN',
                                                                '^Julio': 'JUL', '^Agosto': 'AUG', '^Septiembre' : 'SEP', '^Octubre': 'OCT', '^Noviembre': 'NOV', '^Diciembre': 'DEC'})
        df_chile["PERIOD"] = df_chile["PERIOD"].astype('datetime64[ns]')
        df_chile["PERIOD"]=df_chile["PERIOD"].apply(lambda x: x.strftime('%m/%y'))
        df_chile["DESCRIPTION"].fillna(" ", inplace = True)
        df_chile["CATEGORY"].fillna(" ", inplace=True)
        df_chile["BRAND"].fillna(" ", inplace=True)
        df_chile["MANUFACTURER"].fillna(" ", inplace=True)
        df_chile["PERIOD"].fillna(" ", inplace=True)
        df_chile["SALES VALUE"].fillna(0, inplace=True)
        df_chile["SALES VOLUME"].fillna(0, inplace=True)
        df_chile["NUMERIC DISTRIBUTION"].fillna(0, inplace=True)
        df_chile["WEIGHTED DISTRIBUTION"].fillna(0, inplace=True)
        df_chile_fin = df_chile[(df_chile['SALES VALUE'] == 0) & (df_chile['SALES VOLUME'] == 0) & (df_chile['NUMERIC DISTRIBUTION'] == 0) & (df_chile['WEIGHTED DISTRIBUTION'] == 0)].index

        df_chile.drop(df_chile_fin, inplace=True)
#######################PERU########################
        df_peru_1 = pd.concat(pd.read_excel('Emerging Brands - Global (6).xlsx', sheet_name= ['SSDs PE', 'RTD PE', 'Sport PE']))


        df_peru_2 = pd.concat(pd.read_excel('Emerging Brands - Global (6).xlsx', sheet_name=['Plain PE', 'Flavor PE']))
        df_peru_2.rename(columns={'TIPO': 'CATEGORY'}, inplace = True)

        df_peru = pd.concat([df_peru_1, df_peru_2])
        df_peru = df_peru.drop(df_peru.columns[[2, 9, 12]], axis = 1)
        #df_peru['SDESC.1'] = pd.to_datetime(df_peru['SDESC.1'].str.strip(), format = '%m/%y', errors = 'ignore')
        #df_peru['SDESC.1'] = df_peru['SDESC.1'].apply(lambda x: x.strftime('%m/%y'))
        df_peru.rename(columns={'SDESC':'DESCRIPTION',
                                  'SDESC.1':'PERIOD',
                                  'MANUF': 'MANUFACTURER',
                                  'VENTAS VOLUMEN UNIT CASES (\'000)': 'SALES VOLUME',
                                  'Ventas Valor (\'000)':'SALES VALUE',
                                  'DISTRIBUCION FISICA' : 'NUMERIC DISTRIBUTION',
                                  'DISTRIBUCION PONDERADA': 'WEIGHTED DISTRIBUTION'
                                  },
                         inplace=True)


        df_peru["CATEGORY"]= df_peru["CATEGORY"].replace("BEBIDAS GASEOSAS", "CARBONATED SOFT DRINKS" )
        df_peru["CATEGORY"]= df_peru["CATEGORY"].replace("MINERAL", "TOTAL WATER")
        df_peru["CATEGORY"]= df_peru["CATEGORY"].replace("SABORIZADA", "TOTAL WATER")
        df_peru["CATEGORY"]= df_peru["CATEGORY"].replace("POTABLE", "TOTAL WATER")
        df_peru["CATEGORY"]= df_peru["CATEGORY"].replace("JUGOS ISOTONICOS", "JUICE DRINKS")
        df_peru["CATEGORY"]= df_peru["CATEGORY"].replace("JUGOS RTD", "JUICE DRINKS")
        df_peru["PERIOD"]= df_peru["PERIOD"].replace(regex={r'^ENE': 'JAN','^ABR': 'APR', '^AGO': 'AUG','^DIC' : 'DEC'})
        df_peru["PERIOD"] = df_peru["PERIOD"].astype('datetime64[ns]')
        df_peru["PERIOD"]=df_peru["PERIOD"].apply(lambda x: x.strftime('%m/%y'))
        df_peru["DESCRIPTION"].fillna(" ", inplace = True)
        df_peru["CATEGORY"].fillna(" ", inplace=True)
        df_peru["BRAND"].fillna(" ", inplace=True)
        df_peru["MANUFACTURER"].fillna(" ", inplace=True)
        df_peru["PERIOD"].fillna(" ", inplace=True)
        df_peru["SALES VALUE"].fillna(0, inplace=True)
        df_peru["SALES VOLUME"].fillna(0, inplace=True)
        df_peru["NUMERIC DISTRIBUTION"].fillna(0, inplace=True)
        df_peru["WEIGHTED DISTRIBUTION"].fillna(0, inplace=True)
        df_peru = df_peru.drop(df_peru.columns[0], axis=1)
        df_peru.insert(0, 'COUNTRY', 'PERU')
        df_peru["COUNTRY"].fillna(method='ffill', inplace=True)
        df_peru_fin = df_peru[(df_peru['SALES VALUE'] == 0) & (df_peru['SALES VOLUME'] == 0) & (df_peru['NUMERIC DISTRIBUTION'] == 0) & (df_peru['WEIGHTED DISTRIBUTION'] == 0)].index

        df_peru.drop(df_peru_fin, inplace=True)
####################BOLIVIA#######################
        df_bolivia_1 = pd.read_excel('Emerging Brands - Global (6).xlsx', sheet_name= 'SSDs BO')
        df_bolivia_1 = df_bolivia_1.drop(df_bolivia_1.columns[3], axis=1)
        df_bolivia_1.insert(3, 'CATEGORY', 'CARBONATED SOFT DRINKS')


        df_bolivia_2 = pd.concat(pd.read_excel('Emerging Brands - Global (6).xlsx', sheet_name = ['Plain BO', 'Flavor BO']))
        df_bolivia_2.rename(columns={'TIPO': 'CATEGORY'}, inplace = True)
        df_bolivia_2['CATEGORY']= df_bolivia_2['CATEGORY'].replace("MINERAL", "TOTAL WATER")
        df_bolivia_2['CATEGORY']= df_bolivia_2['CATEGORY'].replace("SABORIZADA", "TOTAL WATER")



        df_bolivia_3 = pd.read_excel('Emerging Brands - Global (6).xlsx', sheet_name= 'RTD BO')
        df_bolivia_3 = df_bolivia_3.drop(df_bolivia_3.columns[3], axis=1)
        df_bolivia_3.insert(3, 'CATEGORY', 'JUICE DRINKS')



        df_bolivia_4=pd.read_excel('Emerging Brands - Global (6).xlsx', sheet_name= 'Sport BO')
        df_bolivia_4 = df_bolivia_4.drop(df_bolivia_4.columns[3], axis=1)
        df_bolivia_4.insert(3, 'CATEGORY', 'SPORTS DRINKS')


        df_bolivia = pd.concat([df_bolivia_1, df_bolivia_2, df_bolivia_3, df_bolivia_4])
        df_bolivia = df_bolivia.drop(df_bolivia.columns[[2, 9, 12]], axis=1)

        #df_bolivia["SDESC.1"] = df_bolivia["SDESC.1"].apply(lambda x: x.strftime('%m/%y'))
        df_bolivia["COUNTRY"].fillna( method ='ffill', inplace = True)
        df_bolivia.rename(columns={'FABRICANTE': 'MANUFACTURER',
                                   'MARCA': 'BRAND',
                                   'SDESC': 'DESCRIPTION',
                                   'SDESC.1': 'PERIOD',
                                   'VENTAS EN UNIDADES EQ (in UNIT CASES(000': 'SALES VOLUME',
                                   'VENTAS EN VALOR (in $  BOLIVIANOS(000))': 'SALES VALUE',
                                   'DISTRIBUCION NUMERICA MANEJANTES': 'NUMERIC DISTRIBUTION',
                                   'DISTRIBUCION PONDERADA MANEJANTES': 'WEIGHTED DISTRIBUTION'
                                   },
                          inplace = True)

        df_bolivia["PERIOD"] = df_bolivia["PERIOD"].replace(regex={r'^ENERO': 'JAN', '^FEBRERO': 'FEB', '^MARZO': 'MAR', '^ABRIL' : 'APR', '^MAYO' : 'MAY', '^JUNIO': 'JUN',
                                                                '^JULIO': 'JUL', '^AGOSTO': 'AUG', '^SEPTIEMBRE' : 'SEP', '^OCTUBRE': 'OCT', '^NOVIEMBRE' : 'NOV', '^DICIEMBRE': 'DEC'})
        df_bolivia["PERIOD"] = df_bolivia["PERIOD"].astype('datetime64[ns]')
        df_bolivia["PERIOD"]=df_bolivia["PERIOD"].apply(lambda x: x.strftime('%m/%y'))

        df_bolivia["DESCRIPTION"].fillna(" ", inplace = True)
        df_bolivia["CATEGORY"].fillna(" ", inplace=True)
        df_bolivia["BRAND"].fillna(" ", inplace=True)
        df_bolivia["MANUFACTURER"].fillna(" ", inplace=True)
        df_bolivia["PERIOD"].fillna(" ", inplace=True)
        df_bolivia["SALES VALUE"].fillna(0, inplace=True)
        df_bolivia["SALES VOLUME"].fillna(0, inplace=True)
        df_bolivia["NUMERIC DISTRIBUTION"].fillna(0, inplace=True)
        df_bolivia["WEIGHTED DISTRIBUTION"].fillna(0, inplace=True)



        df_bolivia_fin = df_bolivia[(df_bolivia['SALES VALUE'] == 0) & (df_bolivia['SALES VOLUME'] == 0) & (df_bolivia['NUMERIC DISTRIBUTION'] == 0) & (df_bolivia['WEIGHTED DISTRIBUTION'] == 0)].index

        df_bolivia.drop(df_bolivia_fin, inplace=True)
        df_ACPB = pd.concat([df_argentina, df_chile, df_peru, df_bolivia])
        df_ACPB = df_ACPB[['COUNTRY', 'DESCRIPTION', 'CATEGORY', 'MANUFACTURER', 'BRAND', 'PERIOD', 'SALES VOLUME', 'SALES VALUE', 'WEIGHTED DISTRIBUTION', 'NUMERIC DISTRIBUTION']]
        df_ACPB.to_excel(writer, sheet_name ='ACPB', index=False)

##############Brazil################
def brazil():
###############SSD####################

        df_brazil_1 = pd.read_excel('Brazil.xlsx', sheet_name='SSD')
        df_brazil_1 = df_brazil_1.drop(df_brazil_1.columns[[1, 7, 8, 9]], axis=1)
        df_brazil_1["SDESC.2"]=df_brazil_1["SDESC.2"].apply(lambda x: x.strftime('%m/%y'))
        df_brazil_1.insert(1, 'CATEGORY', "CARBONATED SOFT DRINKS")

        df_brazil_1.rename(columns={'SDESC':'DESCRIPTION',
                                    'SDESC.2' : 'PERIOD',
                                    'FABRICANTE':'MANUFACTURER',
                                    'MARCA':'BRAND',
                                    'VOL SALES \'000 UNIT CASE': 'SALES VOLUME',
                                    'VAL SALES \'000 REAL': 'SALES VALUE'},
                           inplace=True)
        df_brazil_1.insert(0, 'COUNTRY', "BRAZIL")
        ##############JUICE###################

        df_brazil_2 = pd.read_excel('Brazil.xlsx', sheet_name='Juice')
        df_brazil_2 = df_brazil_2.drop(df_brazil_2.columns[[1, 3, 4, 6, 10, 11, 12]], axis=1)
        df_brazil_2["SDESC.2"]=df_brazil_2["SDESC.2"].apply(lambda x: x.strftime('%m/%y'))
        df_brazil_2.insert(1, 'CATEGORY', "JUICE DRINKS")
        df_brazil_2.rename(columns={'SDESC':'DESCRIPTION',
                                    'SDESC.2' : 'PERIOD',
                                    'FABRICANTE':'MANUFACTURER',
                                    'MARCA':'BRAND',
                                    'VOL SALES \'000 UC': 'SALES VOLUME',
                                    'VAL SALES \'000 REAL': 'SALES VALUE'},
                           inplace=True)
        df_brazil_2.insert(0, 'COUNTRY', "BRAZIL")



        ##############WATER####################

        df_brazil_3 = pd.read_excel('Brazil.xlsx', sheet_name='Water')
        df_brazil_3 = df_brazil_3.drop(df_brazil_3.columns[[1, 4, 8, 9, 10]], axis=1)
        df_brazil_3["SDESC.2"]=df_brazil_3["SDESC.2"].apply(lambda x: x.strftime('%m/%y'))
        df_brazil_3.insert(1, 'CATEGORY', "TOTAL WATER")
        df_brazil_3.rename(columns={'SDESC':'DESCRIPTION',
                                    'SDESC.2' : 'PERIOD',
                                    'FABRICANTE':'MANUFACTURER',
                                    'MARCA':'BRAND',
                                    'VOL SALES \'000': 'SALES VOLUME',
                                    'VAL SALES \'000 REAL': 'SALES VALUE'},
                           inplace=True)
        df_brazil_3.insert(0, 'COUNTRY', "BRAZIL")
        df_brazil = pd.concat([df_brazil_1, df_brazil_2, df_brazil_3])
        df_brazil.replace(r'\s+',np.nan,regex=True).replace('',np.nan)
        df_brazil["COUNTRY"].fillna(method='ffill', inplace=True)
        df_brazil["SALES VALUE"].fillna(0, inplace=True)
        df_brazil["SALES VOLUME"].fillna(0, inplace=True)
        df_brazil["NUMERIC DISTRIBUTION"].fillna(0, inplace=True)
        df_brazil["WEIGHTED DISTRIBUTION"].fillna(0, inplace=True)
        df_brazil_fin = df_brazil[(df_brazil['SALES VALUE'] == 0) & (df_brazil['SALES VOLUME'] == 0) & (df_brazil['NUMERIC DISTRIBUTION'] == 0) & (df_brazil['WEIGHTED DISTRIBUTION'] == 0)].index
        df_brazil.drop(df_brazil_fin, inplace=True)
        df_brazil = df_brazil[['COUNTRY', 'DESCRIPTION', 'CATEGORY', 'MANUFACTURER', 'BRAND', 'PERIOD', 'SALES VOLUME', 'SALES VALUE', 'WEIGHTED DISTRIBUTION', 'NUMERIC DISTRIBUTION']]
        df_brazil.to_excel(writer, sheet_name='Brazil', index=False)
##################South Africa######################
def south_africa():
        df_SA1 = pd.read_excel('TCCC Emerging Brands - South Africa - Energy Drinks (1).xlsx', sheet_name='Energy Drinks', ignore_index=True)
        df_SA1.insert(2, 'CATEGORY', 'SPORTS & ENERGY DRINKS')
        df_SA2 = pd.read_excel('TCCC Emerging Brands - South Africa - Ice Tea (1).xlsx', sheet_name='Ice Tea', ignore_index=True)
        df_SA2.insert(2, 'CATEGORY', 'PACKAGES TEA & COFFEE')
        df_SA3 = pd.read_excel('TCCC Emerging Brands - South Africa - Juice (1).xlsx', sheet_name='Juice', ignore_index=True)
        df_SA3.insert(2, 'CATEGORY', 'JUICE DRINKS')
        df_SA4 = pd.read_excel('TCCC Emerging Brands - South Africa - Sports Dinks (1).xlsx', sheet_name='Sports Drinks', ignore_index=True)
        df_SA4.insert(2, 'CATEGORY', 'SPORTS & ENERGY DRINKS')
        df_SA5 = pd.read_excel('TCCC Emerging Brands - South Africa - SSDs (1).xlsx', sheet_name='SSDs', ignore_index=True)
        df_SA5.insert(2, 'CATEGORY', 'CARBONATED SOFT DRINKS')
        df_SA6 = pd.read_excel('TCCC Emerging Brands - South Africa - Water (2).xlsx', sheet_name='Water', ignore_index=True)
        df_SA6.insert(2, 'CATEGORY', 'TOTAL WATER')

        df_SA = pd.concat([df_SA1, df_SA2, df_SA3, df_SA4, df_SA5, df_SA6])

        df_SA["BRAND"] = df_SA["Brands"].fillna(df_SA["Brand"])
        df_SA["MANUFACTURER"] = df_SA["Manufacturers"].fillna(df_SA["Manufacturer"])
        df_SA['Time Period'] = pd.to_datetime(df_SA['Time Period'], errors = 'ignore')
        df_SA['Time Period'] = df_SA['Time Period'].apply(lambda x: x.strftime('%m/%y'))
        df_SA = df_SA.drop(df_SA.columns[[1, 7, 9, 13, 14]], axis=1)
        df_SA = df_SA[["Country", "Description", "CATEGORY", "MANUFACTURER", "BRAND", "Time Period", "Volume Sales (\'000)", "Value Sales (Usd)", "Wtd Dist (Avg)", "Num Dist (Avg)"]]
        df_SA_fin = df_SA[(df_SA["Volume Sales (\'000)"] == 0) & (df_SA["Value Sales (Usd)"] == 0) & (df_SA["Wtd Dist (Avg)"] == 0) & (df_SA["Num Dist (Avg)"] == 0)].index
        df_SA.drop(df_SA_fin, inplace=True)
        df_SA.rename(columns={"Time Period": "PERIOD",
                              "Volume Sales (\'000)": "SALES VOLUME",
                              "Value Sales (Usd)": "SALES VALUE",
                              "Wtd Dist (Avg)": "WEIGHTED DISTRIBUTION",
                              "Num Dist (Avg)": "NUMERIC DISTRBUTION"},
                     inplace=True)
        df_SA.columns = [x.upper() for x in df_SA.columns]
        df_SA = df_SA.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
        df_SA["SALES VALUE"].fillna(0, inplace=True)
        df_SA["SALES VOLUME"].fillna(0, inplace=True)
        df_SA["NUMERIC DISTRIBUTION"].fillna(0, inplace=True)
        df_SA["WEIGHTED DISTRIBUTION"].fillna(0, inplace=True)
        df_SA["COUNTRY"].fillna(method='ffill', inplace=True)
        df_SA.to_excel(writer, sheet_name='South Africa', index=False)
#######################Turkey##################
def turkey():

############################Dairy############################
        df_turkey_milk = pd.read_excel('Turkey (Milk & Drinkable Yogurt) Emerging Brands Data Pull Dec2019.xlsx', sheet_name='MILK_TR', ignore_index=True)
        df_turkey_milk = df_turkey_milk.drop(df_turkey_milk.columns[[1, 4, 5, 9, 10]], axis=1)
        df_turkey_milk = df_turkey_milk.drop(df_turkey_milk.index[0])
        df_turkey_yogurt = pd.read_excel('Turkey (Milk & Drinkable Yogurt) Emerging Brands Data Pull Dec2019.xlsx', sheet_name='DRINKABLE YOGURT_TR', ignore_index=True)
        df_turkey_yogurt = df_turkey_yogurt.drop(df_turkey_yogurt.columns[[1, 7, 8]], axis=1)
        df_turkey_yogurt = df_turkey_yogurt.drop(df_turkey_yogurt.index[0])
        df_turkey_1 = pd.concat([df_turkey_milk, df_turkey_yogurt])

        df_turkey_1.insert(0, 'COUNTRY', 'TURKEY')
        df_turkey_1.insert(2, 'CATEGORY', 'DAIRY')
        df_turkey_1["Sales Volume (1 in 000 LIT)"].fillna(0, inplace=True)
        df_turkey_1["Sales Value (in 1 000)"].fillna(0, inplace=True)
        df_turkey_1["Weighted Distribution %"].fillna(0, inplace=True)
        df_turkey_1["Numeric Distribution %"].fillna(0, inplace=True)
        df_turkey_1_fin = df_turkey_1[(df_turkey_1['Sales Volume (in 1 000 LIT)'] == 0) & (df_turkey_1['Sales Value (in 1 000)'] == 0) & (df_turkey_1['Weighted Distribution %'] == 0) & (df_turkey_1['Numeric Distribution %'] == 0)].index
        df_turkey_1.drop(df_turkey_1_fin, inplace=True)
        df_turkey_1.rename(columns={'CHANNEL': 'DESCRIPTION',
                                    'COMPANY': 'MANUFACTURER',
                                    'BRAND': 'BRAND',
                                    'PERIOD': 'PERIOD',
                                    'Sales Volume (in 1 000 LIT)': 'SALES VOLUME',
                                    'Sales Value (in 1 000)': 'SALES VALUE',
                                    'Weighted Distribution %': 'WEIGHTED DISTRIBUTION',
                                    'Numeric Distribution %': 'NUMERIC DISTRIBUTION'},
                           inplace=True)
        df_turkey_1["PERIOD"] = pd.to_datetime(df_turkey_1["PERIOD"], errors = 'ignore')
        df_turkey_1["PERIOD"] = df_turkey_1["PERIOD"].apply(lambda x: x.strftime('%m/%y'))



        ############################SSD############################
        df_turkey_2 = pd.read_excel('Turkey (SSD) Emerging Brands Data Pull Dec2019.xlsx', ignore_index=True)
        df_turkey_2= df_turkey_2.drop(df_turkey_2.columns[[1, 2, 8, 9]], axis=1)
        df_turkey_2= df_turkey_2.drop(df_turkey_2.index[0])
        df_turkey_2.insert(0, 'COUNTRY', 'TURKEY')
        df_turkey_2.insert(2, 'CATEGORY', 'CARBONATED SOFT DRINKS')
        df_turkey_2["Volume Sales (000) UC"].fillna(0, inplace=True)
        df_turkey_2["Value Sales\'000"].fillna(0, inplace=True)
        df_turkey_2["Wtd Dist"].fillna(0, inplace=True)
        df_turkey_2["Num Dist"].fillna(0, inplace=True)
        df_turkey_2_fin = df_turkey_2[(df_turkey_2['Volume Sales (000) UC'] == 0) & (df_turkey_2['Value Sales\'000'] == 0) & (df_turkey_2['Wtd Dist'] == 0) & (df_turkey_2['Num Dist'] == 0)].index
        df_turkey_2.drop(df_turkey_2_fin, inplace=True)
        df_turkey_2.rename(columns={'CHANNEL': 'DESCRIPTION',
                                    'MANUFACTURER': 'MANUFACTURER',
                                    'BRAND': 'BRAND',
                                    'PERIOD': 'PERIOD',
                                    'Volume Sales (000) UC': 'SALES VOLUME',
                                    'Value Sales\'000': 'SALES VALUE',
                                    'Wtd Dist': 'WEIGHTED DISTRIBUTION',
                                    'Num Dist': 'NUMERIC DISTRIBUTION'},
                           inplace=True)
        df_turkey_2["PERIOD"] = pd.to_datetime(df_turkey_2["PERIOD"], errors = 'ignore')
        df_turkey_2["PERIOD"] = df_turkey_2["PERIOD"].apply(lambda x: x.strftime('%m/%y'))

        #########################Still###############################
        df_turkey_RTD = pd.read_excel('Turkey (Still) Emerging Brands Data Pull Dec2019.xlsx', sheet_name='RTD Tea_TR', ignore_index=True)
        df_turkey_RTD= df_turkey_RTD.drop(df_turkey_RTD.columns[[1, 2, 8, 9]], axis=1)
        df_turkey_RTD= df_turkey_RTD.drop(df_turkey_RTD.index[0])
        df_turkey_RTD.insert(2, 'CATEGORY', 'PACKAGES TEA & COFFEE')
        df_turkey_RTD.insert(0, 'COUNTRY', 'TURKEY')
        df_turkey_RTD["Volume Sales (000) UC"].fillna(0, inplace=True)
        df_turkey_RTD["Value Sales\'000"].fillna(0, inplace=True)
        df_turkey_RTD["Wtd Dist"].fillna(0, inplace=True)
        df_turkey_RTD["Num Dist"].fillna(0, inplace=True)
        df_turkey_RTD_fin = df_turkey_RTD[(df_turkey_RTD['Volume Sales (000) UC'] == 0) & (df_turkey_RTD['Value Sales\'000'] == 0) & (df_turkey_RTD['Wtd Dist'] == 0) & (df_turkey_RTD['Num Dist'] == 0)].index
        df_turkey_RTD.drop(df_turkey_RTD_fin, inplace=True)
        df_turkey_RTD.rename(columns={'CHANNEL': 'DESCRIPTION',
                                    'MANUFACTURER': 'MANUFACTURER',
                                    'BRAND': 'BRAND',
                                    'MONTH': 'PERIOD',
                                    'Volume Sales (000) UC': 'SALES VOLUME',
                                    'Value Sales\'000': 'SALES VALUE',
                                    'Wtd Dist': 'WEIGHTED DISTRIBUTION',
                                    'Num Dist': 'NUMERIC DISTRIBUTION'},
                           inplace=True)

        df_turkey_energy = pd.read_excel('Turkey (Still) Emerging Brands Data Pull Dec2019.xlsx', sheet_name='Energy_TR', ignore_index=True)
        df_turkey_energy= df_turkey_energy.drop(df_turkey_energy.columns[[1, 8, 9]], axis=1)
        df_turkey_energy= df_turkey_energy.drop(df_turkey_energy.index[0])
        df_turkey_energy['CATEGORY']=df_turkey_energy['CATEGORY'].replace('ENERGY DRINKS', 'SPORTS & ENERGY DRINKS')
        df_turkey_energy.insert(0, 'COUNTRY', 'TURKEY')
        df_turkey_energy["Volume Sales (000) UC"].fillna(0, inplace=True)
        df_turkey_energy["Value Sales\'000"].fillna(0, inplace=True)
        df_turkey_energy["Wtd Dist"].fillna(0, inplace=True)
        df_turkey_energy["Num Dist"].fillna(0, inplace=True)
        df_turkey_energy_fin = df_turkey_energy[(df_turkey_energy['Volume Sales (000) UC'] == 0) & (df_turkey_energy['Value Sales\'000'] == 0) & (df_turkey_energy['Wtd Dist'] == 0) & (df_turkey_energy['Num Dist'] == 0)].index
        df_turkey_energy.drop(df_turkey_energy_fin, inplace=True)
        df_turkey_energy.rename(columns={'CHANNEL': 'DESCRIPTION',
                                    'MANUFACTURER': 'MANUFACTURER',
                                    'BRAND': 'BRAND',
                                    'MONTH': 'PERIOD',
                                    'Volume Sales (000) UC': 'SALES VOLUME',
                                    'Value Sales\'000': 'SALES VALUE',
                                    'Wtd Dist': 'WEIGHTED DISTRIBUTION',
                                    'Num Dist': 'NUMERIC DISTRIBUTION'},
                           inplace=True)

        df_turkey_sport = pd.read_excel('Turkey (Still) Emerging Brands Data Pull Dec2019.xlsx', sheet_name='Sport DrinkS_TR', ignore_index=True)
        df_turkey_sport= df_turkey_sport.drop(df_turkey_sport.columns[[1, 8, 9, 12]], axis=1)
        df_turkey_sport= df_turkey_sport.drop(df_turkey_sport.index[0])
        df_turkey_sport['CATEGORY']=df_turkey_sport['CATEGORY'].replace('SPORT DRINKS', 'SPORTS & ENERGY DRINKS')
        df_turkey_sport.insert(0, 'COUNTRY', 'TURKEY')
        df_turkey_sport["Volume Sales (000) UC"].fillna(0, inplace=True)
        df_turkey_sport["Value Sales\'000"].fillna(0, inplace=True)
        df_turkey_sport["Wtd Dist"].fillna(0, inplace=True)
        df_turkey_sport["Num Dist"].fillna(0, inplace=True)
        df_turkey_sport_fin = df_turkey_sport[(df_turkey_sport['Volume Sales (000) UC'] == 0) & (df_turkey_sport['Value Sales\'000'] == 0) & (df_turkey_sport['Wtd Dist'] == 0) & (df_turkey_sport['Num Dist'] == 0)].index
        df_turkey_sport.drop(df_turkey_sport_fin, inplace=True)
        df_turkey_sport.rename(columns={'CHANNEL': 'DESCRIPTION',
                                    'MANUFACTURER': 'MANUFACTURER',
                                    'BRAND': 'BRAND',
                                    'MONTH': 'PERIOD',
                                    'Volume Sales (000) UC': 'SALES VOLUME',
                                    'Value Sales\'000': 'SALES VALUE',
                                    'Wtd Dist': 'WEIGHTED DISTRIBUTION',
                                    'Num Dist': 'NUMERIC DISTRIBUTION'},
                           inplace=True)

        df_turkey_juice = pd.read_excel('Turkey (Still) Emerging Brands Data Pull Dec2019.xlsx', sheet_name='Juice_TR', ignore_index=True)
        df_turkey_juice= df_turkey_juice.drop(df_turkey_juice.columns[[1, 2, 4, 8, 9]], axis=1)
        df_turkey_juice= df_turkey_juice.drop(df_turkey_juice.index[0])
        df_turkey_juice.insert(2, 'CATEGORY', 'JUICE DRINKS')
        df_turkey_juice.insert(0, 'COUNTRY', 'TURKEY')
        df_turkey_juice["Volume Sales (000) UC"].fillna(0, inplace=True)
        df_turkey_juice["Value Sales\'000"].fillna(0, inplace=True)
        df_turkey_juice["Wtd Dist"].fillna(0, inplace=True)
        df_turkey_juice["Num Dist"].fillna(0, inplace=True)
        df_turkey_juice_fin = df_turkey_juice[(df_turkey_juice['Volume Sales (000) UC'] == 0) & (df_turkey_juice['Value Sales\'000'] == 0) & (df_turkey_juice['Wtd Dist'] == 0) & (df_turkey_juice['Num Dist'] == 0)].index
        df_turkey_juice.drop(df_turkey_juice_fin, inplace=True)
        df_turkey_juice.rename(columns={'CHANNEL': 'DESCRIPTION',
                                    'MANUFACTURER': 'MANUFACTURER',
                                    'BRAND': 'BRAND',
                                    'MONTH.1': 'PERIOD',
                                    'Volume Sales (000) UC': 'SALES VOLUME',
                                    'Value Sales\'000': 'SALES VALUE',
                                    'Wtd Dist': 'WEIGHTED DISTRIBUTION',
                                    'Num Dist': 'NUMERIC DISTRIBUTION'},
                           inplace=True)

        df_turkey_SPW = pd.read_excel('Turkey (Still) Emerging Brands Data Pull Dec2019.xlsx', sheet_name='SPW_TR', ignore_index=True)
        df_turkey_SPW= df_turkey_SPW.drop(df_turkey_SPW.columns[[1, 4, 5, 9, 10]], axis=1)
        df_turkey_SPW= df_turkey_SPW.drop(df_turkey_SPW.index[0])
        df_turkey_SPW.insert(2, 'CATEGORY', 'TOTAL WATER')
        df_turkey_SPW.insert(0, 'COUNTRY', 'TURKEY')
        df_turkey_SPW["Volume Sales (000) UC"].fillna(0, inplace=True)
        df_turkey_SPW["Value Sales\'000"].fillna(0, inplace=True)
        df_turkey_SPW["Wtd Dist"].fillna(0, inplace=True)
        df_turkey_SPW["Num Dist"].fillna(0, inplace=True)
        df_turkey_SPW_fin = df_turkey_SPW[(df_turkey_SPW['Volume Sales (000) UC'] == 0) & (df_turkey_SPW['Value Sales\'000'] == 0) & (df_turkey_SPW['Wtd Dist'] == 0) & (df_turkey_SPW['Num Dist'] == 0)].index
        df_turkey_SPW.drop(df_turkey_SPW_fin, inplace=True)
        df_turkey_SPW.rename(columns={'CHANNEL': 'DESCRIPTION',
                                    'MANUFACTURER': 'MANUFACTURER',
                                    'BRAND': 'BRAND',
                                    'PERIOD': 'PERIOD',
                                    'Volume Sales (000) UC': 'SALES VOLUME',
                                    'Value Sales\'000': 'SALES VALUE',
                                    'Wtd Dist': 'WEIGHTED DISTRIBUTION',
                                    'Num Dist': 'NUMERIC DISTRIBUTION'},
                           inplace=True)


        df_turkey_SWA = pd.read_excel('Turkey (Still) Emerging Brands Data Pull Dec2019.xlsx', sheet_name='SWA_TR', ignore_index=True)
        df_turkey_SWA= df_turkey_SWA.drop(df_turkey_SWA.columns[[1, 2, 3, 4, 10, 11]], axis=1)
        df_turkey_SWA= df_turkey_SWA.drop(df_turkey_SWA.index[0])
        df_turkey_SWA.insert(2, 'CATEGORY', 'TOTAL WATER')
        df_turkey_SWA.insert(0, 'COUNTRY', 'TURKEY')
        df_turkey_SWA["Volume Sales (000) UC"].fillna(0, inplace=True)
        df_turkey_SWA["Value Sales\'000"].fillna(0, inplace=True)
        df_turkey_SWA["Wtd Dist"].fillna(0, inplace=True)
        df_turkey_SWA["Num Dist"].fillna(0, inplace=True)
        df_turkey_SWA_fin = df_turkey_SWA[(df_turkey_SWA['Volume Sales (000) UC'] == 0) & (df_turkey_SWA['Value Sales\'000'] == 0) & (df_turkey_SWA['Wtd Dist'] == 0) & (df_turkey_SWA['Num Dist'] == 0)].index
        df_turkey_SWA.drop(df_turkey_SWA_fin, inplace=True)
        df_turkey_SWA.rename(columns={'CHANNEL': 'DESCRIPTION',
                                    'MANUFACTURER': 'MANUFACTURER',
                                    'BRAND': 'BRAND',
                                    'PERIOD': 'PERIOD',
                                    'Volume Sales (000) UC': 'SALES VOLUME',
                                    'Value Sales\'000': 'SALES VALUE',
                                    'Wtd Dist': 'WEIGHTED DISTRIBUTION',
                                    'Num Dist': 'NUMERIC DISTRIBUTION'},
                           inplace=True)


        df_turkey_3 = pd.concat([df_turkey_RTD,  df_turkey_energy, df_turkey_sport, df_turkey_juice, df_turkey_SPW, df_turkey_SWA])
        df_turkey_3 = df_turkey_3.drop(df_turkey_3.columns[[10, 11, 12]], axis=1)
        df_turkey_3["PERIOD"] = pd.to_datetime(df_turkey_3["PERIOD"], errors = 'ignore')
        df_turkey_3["PERIOD"] = df_turkey_3["PERIOD"].apply(lambda x: x.strftime('%m/%y'))
        df_turkey = pd.concat([df_turkey_1, df_turkey_2, df_turkey_3])
        df_turkey["COUNTRY"].fillna(method='ffill', inplace=True)
        df_turkey.to_excel(writer, sheet_name='Turkey', index=False)

######################USA#########################
def usa():
        df_workbook = pd.read_excel('Copy of 2.3.20 USA Emerging Brands Data DEC19.xlsx',sheet_name = None)
        df_usa = pd.DataFrame()
        for _, sheet in df_workbook.items():
            df_usa = df_usa.append(sheet)

        # Reset index or you'll have duplicates
        df_usa = df_usa.drop(df_usa.columns[[1, 9, 10, 13, 14 ,15 ,16 ,17, 18 ,19, 20, 21, 22, 23, 24, 25, 26]], axis=1)
        df_usa = df_usa.reset_index(drop=True)
        df_usa["BRAND"] = df_usa["KEY BRAND"].fillna(df_usa["Key Brand"])
        df_usa["CATEGORY"] = df_usa["TOTAL CATEGORY"].fillna(df_usa["Total Category"])
        df_usa = df_usa.drop(df_usa.columns[[1, 3, 7, 9, 10]], axis=1)
        df_usa['PER'] = df_usa['PER'].map(lambda x:x.split(" ", 3)[-1])
        df_usa['PER'] = pd.to_datetime(df_usa['PER'], errors = 'ignore')
        df_usa['PER'] = df_usa['PER'].apply(lambda x: x.strftime('%m/%y'))
        df_usa["Eq Vol (000)\'s"].fillna(0, inplace=True)
        df_usa["Dol Vol (000)\'s"].fillna(0, inplace=True)
        df_usa["Avg % ACV Selling"].fillna(0, inplace=True)
        df_usa_fin = df_usa[(df_usa['Eq Vol (000)\'s'] == 0) & (df_usa['Dol Vol (000)\'s'] == 0) & (df_usa['Avg % ACV Selling'] == 0)].index
        df_usa.drop(df_usa_fin, inplace=True)
        df_usa.columns = [x.upper() for x in df_usa.columns]
        df_usa = df_usa[['MKT', 'CATEGORY', 'KEY MANUFACTURER', 'BRAND', 'PER','EQ VOL (000)\'S', 'DOL VOL (000)\'S', 'AVG % ACV SELLING']]
        #df_usa['PER'] = df_usa['PER'].apply(lambda x: x.strftime('%b-%y').upper())
        df_usa.insert(0, 'COUNTRY', 'USA')
        df_usa.rename(columns={'MKT': 'DESCRIPTION',
                                'KEY MANUFACTURER': 'MANUFACTURER',
                                'PER': 'PERIOD',
                                'EQ VOL (000)\'S': 'SALES VOLUME',
                                'DOL VOL (000)\'S':'SALES VALUE',
                                'AVG % ACV SELLING': 'NUMERIC DISTRIBUTION'
                                },
                       inplace=True)
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL SSD', 'CARBONATED SOFT DRINKS')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL WATER', 'TOTAL WATER')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL COFFEE', 'PACKAGES TEA & COFFEE')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL ENERGY', 'SPORTS & ENERGY DRINKS')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL PLANT WATER/JUICE', 'JUICE DRINKS')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL SPORTS DRINK', 'SPORTS & ENERGY DRINKS')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL TEA', 'PACKAGES TEA & COFFEE')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL COMPLETE NUTRITIONAL', 'OTHER BEVERAGES')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL DRINKABLE DAIRY', 'DAIRY')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL JUICE/DRINK', 'JUICE DRINKS')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL KOMBUCHA', 'DAIRY')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL N-RTD FT FLAVORED BEVS', 'OTHER BEVERAGES')
        df_usa['CATEGORY']=df_usa['CATEGORY'].replace('TTL NCB MIXERS', 'OTHER BEVERAGES')
        df_usa.to_excel(writer, sheet_name='USA', index=False)

################South Korea######################3
def south_korea():
    df_korea = pd.concat(pd.read_excel('SKorea.xlsx', sheet_name=None), ignore_index=True)
    df_korea = df_korea.drop(df_korea.columns[[5, 8, 10, 13, 14, 15, 16]], axis=1)
    df_korea.rename(columns={'Channels': 'DESCRIPTION',
                             'Brand Owner': 'MANUFACTURER',
                             'Time period': 'PERIOD',
                             'Sales Volume (192OZ)': 'SALES VOLUME',
                             'Sales Value (000 USD)': 'SALES VALUE',
                             'Distribution Numeric': 'NUMERIC DISTRIBUTION',
                             'Distribution Weighted': 'WEIGHTED DISTRIBUTION'},
                    inplace=True)
    df_korea['PERIOD'] = df_korea['PERIOD'].str.replace(r'(16|17|18|19)', r'-\1')
    df_korea['PERIOD'] = pd.to_datetime(df_korea['PERIOD'], errors='ignore')
    df_korea["DESCRIPTION"].fillna(" ", inplace=True)
    df_korea["MANUFACTURER"].fillna(" ", inplace=True)
    df_korea["PERIOD"].fillna(" ", inplace=True)
    df_korea["SALES VOLUME"].fillna(0, inplace=True)
    df_korea["SALES VALUE"].fillna(0, inplace=True)
    df_korea["NUMERIC DISTRIBUTION"].fillna(0, inplace=True)
    df_korea["WEIGHTED DISTRIBUTION"].fillna(0, inplace=True)
    df_korea_fin = df_korea[
        (df_korea['SALES VALUE'] == 0) & (df_korea['SALES VOLUME'] == 0) & (df_korea['NUMERIC DISTRIBUTION'] == 0) & (
                    df_korea['WEIGHTED DISTRIBUTION'] == 0)].index
    df_korea.drop(df_korea_fin, inplace=True)
    df_korea.columns = map(str.upper, df_korea.columns)
    df_korea = df_korea.apply(lambda x: x.str.upper() if x.dtype == "object" else x)
    df_korea["CATEGORY"] = df_korea["CATEGORY"].replace("SPARKLING WATER+MINERAL WATER", "TOTAL WATER")
    df_korea["CATEGORY"] = df_korea["CATEGORY"].replace("ENERGY+HEALTH+BEAUTY DRINK", "SPORTS & ENERGY DRINKS")
    df_korea["CATEGORY"] = df_korea["CATEGORY"].replace("VEGETABLE JUICE", "JUICE DRINKS")
    df_korea["CATEGORY"] = df_korea["CATEGORY"].replace("FRUIT JUICE", "JUICE DRINKS")
    df_korea["CATEGORY"] = df_korea["CATEGORY"].replace("RTD TEA", "PACKAGES TEA & COFFEE")
    df_korea["CATEGORY"] = df_korea["CATEGORY"].replace("SSD", "CARBONATED SOFT DRINKS")
    df_korea["CATEGORY"] = df_korea["CATEGORY"].replace("SPORTS DRINK", "SPORTS & ENERGY DRINKS")
    df_korea["CATEGORY"] = df_korea["CATEGORY"].replace("RTD COFFEE", "PACKAGES TEA & COFFEE")
    df_korea.to_excel(writer, sheet_name="South Korea", index=False)


writer = pd.ExcelWriter('output-local.xlsx', engine='xlsxwriter')


# Close the Pandas Excel writer and output the Excel file.
writer.save()
