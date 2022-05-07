import requests
import hashlib
import pandas as pd
import time
import sqlite3

class CountriesDataFrame:
    def __init__(self):
        pass


    def get_countries(self):
        json_response = ''
        r = requests.get(url='https://restcountries.com/v3.1/all')
        if(r.status_code == 200):
            json_response = r.json()
        self.json_str = json_response

    
    def to_dt(self):
        self.dt = pd.DataFrame(data=self.get_records(), columns=['Region', 'City Name', 'Language', 'Time'])


    def to_sql(self):
        conn = sqlite3.connect('restdb')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS countries (region text, city_name text, language text, process_time text)')
        conn.commit()

        self.dt.to_sql('countries', conn, if_exists='replace', index = False)
        # c.execute('''  
        # SELECT * FROM countries
        # ''')

        # for row in c.fetchall():
        #     print (row)


    def to_json(self):
        self.dt.to_json(path_or_buf='./data.json', orient='table')


    def hash_sha1(self, enc):
        return (hashlib.sha1(enc.encode())).hexdigest()


    def get_records(self):
        ob_records = list()
        stime = time.time() * 1000
        for i in self.json_str:
            ob_dict = [
                i['region'] if 'region' in i else '',
                i['name']['common'] if 'name' in i else '',
                list(i['languages'].values())[0] if 'languages' in i else '',
                ''
            ]
            ob_dict[2] = self.hash_sha1(ob_dict[2])
            ftime = (time.time() * 1000) - stime
            ob_dict[3] = str('{}ms').format(round(ftime,2))
            ob_records.append(ob_dict)
        return ob_records
        

if __name__ == '__main__':
    countries_dt = CountriesDataFrame()
    countries_dt.get_countries()
    countries_dt.to_dt()
    countries_dt.to_sql()
    countries_dt.to_json()
