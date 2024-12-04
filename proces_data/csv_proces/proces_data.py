import csv
from datetime import datetime

def System_data_proces(input_file):
    # Read the data from the .dat file
    data = []
    headers = []
    with open(input_file, 'r') as file:
        reader = list(csv.reader(file))
        
        # Check if the file has enough rows
        if len(reader) < 5:
            print(f"El archivo {input_file} no tiene suficientes filas.")
            return None

        headers.append(reader[0])  # First line of headers
        headers.append(reader[1])  # Second line of headers
        headers.append(reader[2])  # Third line of headers
        headers.append(reader[3])  # Fourth line of headers

        # Remove the 'RECORD' column from the headers
        for i in range(len(headers)):
            if 'RECORD' in headers[i]:
                record_index = headers[i].index('RECORD')
                headers[i].pop(record_index)
        
        # Change 'PTemp' to 'PanelTemp' in the headers
        for i in range(len(headers)):
            if 'PTemp' in headers[i]:
                ptemp_index = headers[i].index('PTemp')
                headers[i][ptemp_index] = 'PanelTemp'

            

        # Get the latest timestamp to determine the last month
        latest_timestamp = reader[-1][0]
        latest_date = datetime.strptime(latest_timestamp, '%Y-%m-%d %H:%M:%S')
        latest_month = latest_date.strftime('%Y-%m')

        # Read the data in reverse order and stop when the month changes
        for row in reversed(reader[4:]):
            row_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            row_month = row_date.strftime('%Y-%m')
            if row_month != latest_month:
                break
            
            row.pop(record_index)  # Remove the 'RECORD' column from the data row


            data.append(dict(zip(headers[1], row)))  # Use the second line of headers for the data keys

    # Create the array with the third line of headers and the data
    result = [headers[1]] + data

    return result

def SBE37_SMPO_data_proces(input_file):
    # Read the data from the .dat file
    data = []
    headers = []
    with open(input_file, 'r') as file:
        reader = list(csv.reader(file))
        
        # Check if the file has enough rows
        if len(reader) < 5:
            print(f"El archivo {input_file} no tiene suficientes filas.")
            return None

        headers.append(reader[0])  # First line of headers
        headers.append(reader[1])  # Second line of headers
        headers.append(reader[2])  # Third line of headers
        headers.append(reader[3])  # Fourth line of headers

        # Remove the columns 'SBE37Date' and 'SBE37Time' from the headers
        for i in range(len(headers)):
            if 'RECORD' in headers[i]:
                record_index = headers[i].index('RECORD')
                headers[i].pop(record_index)
            if 'SBE37Time' in headers[i]:
                sbe37time_index = headers[i].index('SBE37Time')
                headers[i].pop(sbe37time_index)
            if 'SBE37Date' in headers[i]:
                sbe37date_index = headers[i].index('SBE37Date')
                headers[i].pop(sbe37date_index)

        # Get the latest timestamp to determine the last month
        latest_timestamp = reader[-1][0]
        latest_date = datetime.strptime(latest_timestamp, '%Y-%m-%d %H:%M:%S')
        latest_month = latest_date.strftime('%Y-%m')

        # Read the data in reverse order and stop when the month changes
        for row in reversed(reader[4:]):
            row_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            row_month = row_date.strftime('%Y-%m')
            if row_month != latest_month:
                break
            row.pop(record_index)  # Remove 'RECORD' from the data row
            row.pop(sbe37time_index)  # Remove 'SBE37Time' from the data row
            row.pop(sbe37date_index)  # Remove 'SBE37Date' from the data row
            data.append(dict(zip(headers[1], row)))  # Use the second line of headers for the data keys

    # Create the array with the third line of headers and the data
    result = [headers[1]] + data

    return result

def Doppler_data_proces(input_file):
    # Read the data from the .dat file
    data = []
    headers = []
    with open(input_file, 'r') as file:
        reader = list(csv.reader(file))
        
        # Check if the file has enough rows
        if len(reader) < 5:
            print(f"El archivo {input_file} no tiene suficientes filas.")
            return None

        headers.append(reader[0])  # First line of headers
        headers.append(reader[1])  # Second line of headers
        headers.append(reader[2])  # Third line of headers
        headers.append(reader[3])  # Fourth line of headers

        # Remove the columns 'SBE37Date' and 'SBE37Time' from the headers
        for i in range(len(headers)):
            if 'RECORD' in headers[i]:
                record_index = headers[i].index('RECORD')
                headers[i].pop(record_index)
            if 'DopplerMessage' in headers[i]:
                dopler_m_index = headers[i].index('DopplerMessage')
                headers[i].pop(dopler_m_index)
            if 'DoppMonth' in headers[i]:
                dopp_month_index = headers[i].index('DoppMonth')
                headers[i].pop(dopp_month_index)
            if 'DoppDay' in headers[i]:
                dopp_day_index = headers[i].index('DoppDay')
                headers[i].pop(dopp_day_index)
            if 'DoppYear' in headers[i]:
                dopp_year_index = headers[i].index('DoppYear')
                headers[i].pop(dopp_year_index)
            if 'Dopphour' in headers[i]:
                dopp_hour_index = headers[i].index('Dopphour')
                headers[i].pop(dopp_hour_index)
            if 'Doppminute' in headers[i]:
                dopp_minute_index = headers[i].index('Doppminute')
                headers[i].pop(dopp_minute_index)
            if 'Doppsecond' in headers[i]:
                dopp_second_index = headers[i].index('Doppsecond')
                headers[i].pop(dopp_second_index)

        # Get the latest timestamp to determine the last month
        latest_timestamp = reader[-1][0]
        latest_date = datetime.strptime(latest_timestamp, '%Y-%m-%d %H:%M:%S')
        latest_month = latest_date.strftime('%Y-%m')

        # Read the data in reverse order and stop when the month changes
        for row in reversed(reader[4:]):
            row_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            row_month = row_date.strftime('%Y-%m')
            if row_month != latest_month:
                break
            row.pop(record_index)  # Remove 'RECORD' from the data row
            row.pop(dopler_m_index)  # Remove 'DopplerMessage' from the data row
            row.pop(dopp_month_index)  # Remove 'DoppMonth' from the data row
            row.pop(dopp_day_index)  # Remove 'DoppDay' from the data row
            row.pop(dopp_year_index)  # Remove 'DoppYear' from the data row
            row.pop(dopp_hour_index)  # Remove 'Dopphour' from the data row
            row.pop(dopp_minute_index)  # Remove 'Doppminute' from the data row
            row.pop(dopp_second_index)  # Remove 'Doppsecond' from the data row
            
            #Adjust DoppCell data from " r speed dmg" to "speed dmg"
            for i in range(len(row)):
                if row[i].startswith(' '):
                    row[i] = ' '.join(row[i].split()[1:])


            data.append(dict(zip(headers[1], row)))  # Use the second line of headers for the data keys

    # Create the array with the third line of headers and the data
    result = [headers[1]] + data

    return result

def Meteo_data_proces(input_file):
    # Read the data from the .dat file
    data = []
    headers = []
    with open(input_file, 'r') as file:
        reader = list(csv.reader(file))
        
        # Check if the file has enough rows
        if len(reader) < 5:
            print(f"El archivo {input_file} no tiene suficientes filas.")
            return None

        headers.append(reader[0])  # First line of headers
        headers.append(reader[1])  # Second line of headers
        headers.append(reader[2])  # Third line of headers
        headers.append(reader[3])  # Fourth line of headers

        # Remove the 'RECORD' column from the headers
        for i in range(len(headers)):
            if 'RECORD' in headers[i]:
                record_index = headers[i].index('RECORD')
                headers[i].pop(record_index)
        
        # Get the latest timestamp to determine the last month
        latest_timestamp = reader[-1][0]
        latest_date = datetime.strptime(latest_timestamp, '%Y-%m-%d %H:%M:%S')
        latest_month = latest_date.strftime('%Y-%m')

        # Read the data in reverse order and stop when the month changes
        for row in reversed(reader[4:]):
            row_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            row_month = row_date.strftime('%Y-%m')
            if row_month != latest_month:
                break
            
            row.pop(record_index)  # Remove the 'RECORD' column from the data row

            data.append(dict(zip(headers[1], row)))  # Use the second line of headers for the data keys

    # Create the array with the third line of headers and the data
    result = [headers[1]] + data

    return result

def Sami_data_proces(input_file):
    # Read the data from the .dat file
    data = []
    headers = []
    with open(input_file, 'r') as file:
        reader = list(csv.reader(file))
        
        # Check if the file has enough rows
        if len(reader) < 5:
            print(f"El archivo {input_file} no tiene suficientes filas.")
            return None

        headers.append(reader[0])  # First line of headers
        headers.append(reader[1])  # Second line of headers
        headers.append(reader[2])  # Third line of headers
        headers.append(reader[3])  # Fourth line of headers

        # Remove the 'RECORD' column from the headers
        for i in range(len(headers)):
            if 'RECORD' in headers[i]:
                record_index = headers[i].index('RECORD')
                headers[i].pop(record_index)
        
        # Get the latest timestamp to determine the last month
        latest_timestamp = reader[-1][0]
        latest_date = datetime.strptime(latest_timestamp, '%Y-%m-%d %H:%M:%S')
        latest_month = latest_date.strftime('%Y-%m')

        # Read the data in reverse order and stop when the month changes
        for row in reversed(reader[4:]):
            row_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            row_month = row_date.strftime('%Y-%m')
            if row_month != latest_month:
                break
            
            row.pop(record_index)  # Remove the 'RECORD' column from the data row

            data.append(dict(zip(headers[1], row)))  # Use the second line of headers for the data keys

    # Create the array with the third line of headers and the data
    result = [headers[1]] + data

    return result

def export_to_csv(result, output_file):
    if not result:
        print("No hay datos para exportar.")
        return

    # Extract headers and data
    headers = result[0]
    data = result[1:]

    # Write to CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers
        for row in data:
            writer.writerow(row.values())  # Write data rows

    print(f'Data has been successfully exported to {output_file}')
