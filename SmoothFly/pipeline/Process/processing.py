"""
This function takes two arguments: name and csv. The csv argument is expected to be a Pandas
DataFrame object containing flight data. The name argument is a string representing the name 
of the file from which the csv data was extracted. The function modifies the csv data in-place 
by renaming and deleting certain columns, and adding new columns to represent the flight data in 
a standardized format. Finally, the function returns a modified DataFrame that filters out rows 
where the flightNumber column is equal to 'Flight Number'.
"""
def process_csv(name, csv):

    """
    Process flight data in a CSV file to a standardized format.

    Parameters:
    name (str): The name of the CSV file.
    csv (pandas.DataFrame): A pandas DataFrame object containing flight data.

    Returns:
    pandas.DataFrame: The modified DataFrame object, where certain columns have been renamed, 
    deleted or added.
    """

    name = name.split('.')[0]
    csv['source'] = name

    csv['destination'] = csv['Destination Airport']
    del csv['Destination Airport']

    csv['carrier'] = csv['Carrier Code']
    del csv['Carrier Code']

    csv['date'] = csv['Date (MM/DD/YYYY)']
    del csv['Date (MM/DD/YYYY)']

    csv['flightNumber'] = csv['Flight Number']
    del csv['Flight Number']

    csv['tailNumber'] = csv['Tail Number']
    del csv['Tail Number']

    csv['scheduledDepartureTime'] = csv['Scheduled departure time']
    del csv['Scheduled departure time']

    csv['actualDepartureTime'] = csv['Actual departure time']
    del csv['Actual departure time']

    csv['scheduledElapsedMinutes'] = csv['Scheduled elapsed time (Minutes)']
    del csv['Scheduled elapsed time (Minutes)']

    csv['actualElapsedMinutes'] = csv['Actual elapsed time (Minutes)']
    del csv['Actual elapsed time (Minutes)']

    csv['departureDelayMinutes'] = csv['Departure delay (Minutes)']
    del csv['Departure delay (Minutes)']

    csv['wheelsOffTime'] = csv['Wheels-off time']
    del csv['Wheels-off time']

    csv['taxiOutMinutes'] = csv['Taxi-Out time (Minutes)']
    del csv['Taxi-Out time (Minutes)']

    csv['delayCarrierMinutes'] = csv['Delay Carrier (Minutes)']
    del csv['Delay Carrier (Minutes)']

    csv['delayWeatherMinutes'] = csv['Delay Weather (Minutes)']
    del csv['Delay Weather (Minutes)']

    csv['delayNationalAviationSystemMinutes'] = csv[
        'Delay National Aviation System (Minutes)']
    del csv['Delay National Aviation System (Minutes)']

    csv['delaySecurityMinutes'] = csv['Delay Security (Minutes)']
    del csv['Delay Security (Minutes)']

    csv['delayLateAircraftArrivalMinutes'] = csv[
        'Delay Late Aircraft Arrival (Minutes)']
    del csv['Delay Late Aircraft Arrival (Minutes)']

    return csv[(csv['flightNumber'] != 'Flight Number')]
