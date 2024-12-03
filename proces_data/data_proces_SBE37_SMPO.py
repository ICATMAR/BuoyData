import csv
import json
from datetime import datetime
import os

def export_to_json(input_file, output_file):
    # Read the data from the .dat file
    data = []
    headers = []
    timestamp = None
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        headers.append(next(reader))  # First line of headers
        headers.append(next(reader))  # Second line of headers
        headers.append(next(reader))  # Third line of headers
        headers.append(next(reader))  # Fourth line of headers
        for row in reader:
            data.append(dict(zip(headers[1], row)))  # Use the second line of headers for the data keys
            if timestamp is None:
                timestamp = row[0]

    # Create the JSON structure
    json_data = {
        "headers": headers,
        "data": data
    }

    # Write the data to a JSON file
    with open(output_file, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f'Data has been successfully exported to {output_file}')
    return timestamp

if __name__ == "__main__":
    input_file = 'temporal_mds/BoiaBarcelona_SBE37_SMPO.dat'
    
    # Call the function and get the timestamp
    timestamp = export_to_json(input_file, 'temp.json')
    print(f'Timestamp from the first row: {timestamp}')
    
    # Extract year and month from the timestamp
    date_obj = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    year_month = date_obj.strftime('%Y-%m')
    
    # Define the output directory and file name
    output_dir = 'Somorrostro/SBE37_SMPO'
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
    output_file = os.path.join(output_dir, f'SBE37_SMPO_{year_month}.json')
    
    # Call the function again to export the data to the correct file
    export_to_json(input_file, output_file)