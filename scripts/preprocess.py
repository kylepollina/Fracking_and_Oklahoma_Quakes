
import pandas

def preprocess():
    preprocess_wells()
    preprocess_quakes()

def preprocess_wells():
    wells_data = pandas.read_csv('data_fracking/InjectionWells.csv')

    years = []
    months = []
    days = []

    for index, row in wells_data.iterrows():
        date = row['Approval Date']
        year = date.split('/')[2]
        month = date.split('/')[0]
        day = date.split('/')[1]

        years.append(year)
        months.append(month)
        days.append(day)

    wells_data['year'] = years
    wells_data['month'] = months
    wells_data['day'] = days

    # TODO write csv to file

def preprocess_quakes():
    quakes_data = pandas.read_csv('data_fracking/okQuakes.csv')

    years = []
    months = []
    days = []

    for index, row in quakes_data.iterrows():
        time = row['time']
        date = time.split('T')[0]
        year = date.split('-')[0]
        month = date.split('-')[1]
        day = date.split('-')[2]

        years.append(year)
        months.append(month)
        days.append(day)

    quakes_data['year'] = years
    quakes_data['months'] = months
    quakes_data['days'] = days

    # TODO write csv to file
