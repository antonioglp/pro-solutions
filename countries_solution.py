import requests
import hashlib
import pandas as pd
import time
import sqlite3

class CountriesDataFrame:
    def __init__(self):
        pass


    def get_countries(self):
        '''
        Get all countries by a service
        '''
        json_response = ''
        r = requests.get(url='https://restcountries.com/v3.1/all')
        if(r.status_code == 200):
            json_response = r.json()
        self.json_str = json_response

    
    def to_dt(self):
        '''
        Create DataFrame with json previouly designed
        '''
        self.dt = pd.DataFrame(data=self.get_records(), columns=['Region', 'City Name', 'Language', 'Time'])


    def to_sql(self):
        '''
        Export DataFrame to sql table in sqlite
        '''
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
        '''
        Export DataFrame to json file
        '''
        self.dt.to_json(path_or_buf='./data.json', orient='table')


    def hash_sha1(self, enc):
        '''
        Get the hash of string
        '''
        return (hashlib.sha1(enc.encode())).hexdigest()


    def get_records(self):
        '''
        Get json to send it to DataFrame
        '''
        ob_records = list()
        for i in self.json_str:
            stime = time.time()
            ob_dict = [
                i['region'] if 'region' in i else '',
                i['name']['common'] if 'name' in i else '',
                list(i['languages'].values())[0] if 'languages' in i else '',
                ''
            ]
            ob_dict[2] = self.hash_sha1(ob_dict[2])
            ftime = (time.time() - stime) * 1000
            ob_dict[3] = ftime
            ob_records.append(ob_dict)
        return ob_records

    
    def get_time(self):
        '''
        Get time info of the Time column
        '''
        sum_dt = self.dt['Time'].sum()
        min_dt = self.dt['Time'].min()
        max_dt = self.dt['Time'].max()
        mean_dt = self.dt['Time'].mean()

        print('Total {}'.format(sum_dt))
        print('Minimo {}'.format(min_dt))
        print('Maximo {}'.format(max_dt))
        print('Promedio {}'.format(mean_dt))
        

if __name__ == '__main__':
    countries_dt = CountriesDataFrame()
    countries_dt.get_countries()
    countries_dt.to_dt()
    countries_dt.to_sql()
    countries_dt.to_json()
    countries_dt.get_time()
