
import pandas
from datetime import datetime

WELLS_PATH_RAW = 'data_fracking/raw/InjectionWells.csv'
QUAKES_PATH_RAW = 'data_fracking/raw/okQuakes.csv'
WELLS_PATH = 'data_fracking/processed/Wells.csv'
QUAKES_PATH = 'data_fracking/processed/Quakes.csv'


def preprocess():
    """Preprocess all data and store in data_fracking/processed"""
    preprocess_wells()
    preprocess_quakes()

