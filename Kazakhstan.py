import pandas as pd
import xlsxwriter
def kazakhstan_index():
jul = pd.read_excel('July.xlsx')
df = pd.read_excel('Kazakhstan.xlsx', ignore_index=True)
combined_df1 = pd.concat([jul, df[['SDESC','SDESC.1', 'CATEGORY', 'BRAND OWNER', 'BRAND']]], axis=1)
combined_df1 = combined_df1.groupby(['SDESC','SDESC.1','CATEGORY', 'BRAND OWNER', 'BRAND'])[['Value $ (\'000)','Volume in Litres (\'000)','Wtd Dist (Max)','Num Dist (Max)']].sum().reset_index()
combined_df1.insert(5, 'PERIOD', '07/19')

aug = pd.read_excel('Aug.xlsx')
combined_df2 = pd.concat([aug, df[['SDESC','SDESC.1', 'CATEGORY', 'BRAND OWNER', 'BRAND']]], axis=1)
combined_df2 = combined_df2.groupby(['SDESC','SDESC.1','CATEGORY', 'BRAND OWNER', 'BRAND'])[['Value $ (\'000)','Volume in Litres (\'000)','Wtd Dist (Max)','Num Dist (Max)']].sum().reset_index()
combined_df2.insert(5, 'PERIOD', '08/19')

sep = pd.read_excel('Sep.xlsx')
combined_df3 = pd.concat([sep, df[['SDESC','SDESC.1', 'CATEGORY', 'BRAND OWNER', 'BRAND']]], axis=1)
combined_df3 = combined_df3.groupby(['SDESC','SDESC.1','CATEGORY', 'BRAND OWNER', 'BRAND'])[['Value $ (\'000)','Volume in Litres (\'000)','Wtd Dist (Max)','Num Dist (Max)']].sum().reset_index()
combined_df3.insert(5, 'PERIOD', '09/19')

oct = pd.read_excel('Oct.xlsx')
combined_df4 = pd.concat([oct, df[['SDESC','SDESC.1', 'CATEGORY', 'BRAND OWNER', 'BRAND']]], axis=1)
combined_df4 = combined_df4.groupby(['SDESC','SDESC.1','CATEGORY', 'BRAND OWNER', 'BRAND'])[['Value $ (\'000)','Volume in Litres (\'000)','Wtd Dist (Max)','Num Dist (Max)']].sum().reset_index()
combined_df4.insert(5, 'PERIOD', '10/19')

nov = pd.read_excel('Nov.xlsx')
combined_df5 = pd.concat([nov, df[['SDESC','SDESC.1', 'CATEGORY', 'BRAND OWNER', 'BRAND']]], axis=1)
combined_df5 = combined_df5.groupby(['SDESC','SDESC.1','CATEGORY', 'BRAND OWNER', 'BRAND'])[['Value $ (\'000)','Volume in Litres (\'000)','Wtd Dist (Max)','Num Dist (Max)']].sum().reset_index()
combined_df5.insert(5, 'PERIOD', '11/19')

dec = pd.read_excel('Dec.xlsx')
combined_df6 = pd.concat([dec, df[['SDESC','SDESC.1', 'CATEGORY', 'BRAND OWNER', 'BRAND']]], axis=1)
combined_df6 = combined_df6.groupby(['SDESC','SDESC.1','CATEGORY', 'BRAND OWNER', 'BRAND'])[['Value $ (\'000)','Volume in Litres (\'000)','Wtd Dist (Max)','Num Dist (Max)']].sum().reset_index()
combined_df6.insert(5, 'PERIOD', '12/19')

combined_df = pd.concat([combined_df1,combined_df2,combined_df3,combined_df4,combined_df5,combined_df6])
writer = pd.ExcelWriter('KazakhstanOutput.xlsx', engine='xlsxwriter')
combined_df.to_excel(writer, index=False)
writer.save()