import pandas as pd
import datetime
final_data = pd.read_excel('output-local.xlsx')
final_data = final_data.rename(columns={"PERIOD": "TIME PERIOD"})

final_data = final_data[pd.notnull(final_data['TIME PERIOD'])]
final_data = final_data[pd.notnull(final_data['BRAND'])]
final_data = final_data[pd.notnull(final_data['COUNTRY'])]

# New columns (capital case)
final_data['UPPER_BRAND'] = final_data['BRAND'].astype(str).str.upper()
final_data['UPPER_COUNTRY'] = final_data['COUNTRY'].astype(str).str.upper()

# To get timestamp
final_data['TIME PERIOD'] = final_data['TIME PERIOD'].astype(str)
final_data['TIME PERIOD NEW'] = "01/" + final_data['TIME PERIOD']
final_data['TIME PERIOD NEW'] = final_data['TIME PERIOD NEW'].apply(lambda x: x[0:6] + "20" + x[6:])
final_data['ts'] = final_data['TIME PERIOD NEW'].apply(
    lambda x: datetime.datetime.strptime(str(x), "%d/%m/%Y").replace(tzinfo=datetime.timezone.utc).timestamp())
final_data.drop(['TIME PERIOD NEW'], axis=1, inplace=True)
final_data['ts'] = final_data['ts'].astype(int)
final_data['ts'] = final_data['ts'] * 1000
final_data['ts'] = final_data['ts'].astype(int)
final_data['TIME PERIOD'] = final_data['TIME PERIOD'].astype(str)


final_data.to_csv('output-local-final.csv', index=False)