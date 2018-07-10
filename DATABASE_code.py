import sqlalchemy as sqla
import pymysql
import numpy as np
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
#import mysql.connector as conn


'''function to make calls to database'''

def getPostcodeFromTable(postcode, table, s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data.postcode == postcode):
        result.append(a)
    return np.array(result)

def getststion_name(station,table,s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data.station_name == station):
        result.append(a)
    return np.array(result)

def get_measure_date(m_date,table,s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data. measure_date == m_date):
        result.append(a)
    return np.array(result)

def   get_precipitation_type(p_type, table, s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data.  precipitation_type== p_type):
        result.append(a)
    return np.array(result)

def  get_precipitation_amount(p_a, table, s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data.  precipitation_amount== p_a):
        result.append(a)
    return np.array(result)

def get_avg_wind_speed(w_s, table, s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data.average_wind_speed == w_s):
        result.append(a)
    return np.array(result)

def  get_max_wind_speed(m_w_s,table,s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data.max_wind_speed == m_w_s):
        result.append(a)
    return np.array(result)

def get_max_temp(m_t,table,s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data.max_temp == m_t):
        result.append(a)
    return np.array(result)

def get_min_temp(m_t,table,s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data.min_temp == m_t):
        result.append(a)
    return np.array(result)

def get_sun_hours(s_h,table,s):
    result = []
    for a in s.query(Weather_data).filter(Weather_data.sun_hours == s_h):
        result.append(a)
    return np.array(result)
'''end of functions '''
def Load_Data(file_name):
    data = np.genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()
class Weather_data(Base):
    __tablename__ ='Weather_data'
    station_id = Column(Integer,primary_key=True)
    station_name = Column(String(100))
    postcode = Column(Integer)
    measure_date = Column(Integer,primary_key=True)
    quality_1 = Column(Integer)
    max_wind_speed = Column(Float)
    average_wind_speed = Column(Float)
    quality_2 = Column(Integer)
    precipitation_amount = Column(Float)
    precipitation_type = Column(String(50))
    sun_hours = Column(Float)
    snow_height = Column(Float)
    coverage_amount = Column(Float)
    vapor_pressure = Column(Float)
    air_pressure = Column(Float)
    average_temp = Column(Float)
    relative_himidity = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    ground_min_temp = Column(Float)

if __name__ == "__main__":

    #Create the database
    engine = create_engine('sqlite:///csv_test.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    try:
        file_name = "example.csv"
        data = Load_Data(file_name)

        for i in data:
            record = Weather_data(**{
                'station_id': i[0],
                'station_name': i[1],
                'postcode': i[2],
                'measure_date': i[3],
                'quality_1': i[4],
                'max_wind_speed': i[5],
                'average_wind_speed': i[6],
                'quality_2': i[7],
                'precipitation_amount': i[8],
                'precipitation_type': i[9],
                'sun_hours': i[10],
                'snow_height': i[11],
                'coverage_amount': i[12],
                'vapor_pressure': i[13],
                'air_pressure': i[14],
                'average_temp': i[15],
                'relative_himidity': i[16],
                'max_temp': i[17],
                'min_temp': i[18],
                'ground_min_temp': i[19]
            })

            s.add(record)

        s.commit()
    except:
        s.rollback()
    finally:
        s.close()
        
