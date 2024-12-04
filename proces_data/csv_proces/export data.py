import csv
from datetime import datetime, timezone
from proces_data import System_data_proces, SBE37_SMPO_data_proces, Doppler_data_proces, Meteo_data_proces, Sami_data_proces

def merge_data_by_timestamp(system_result, sbe37_result, doppler_result, meteo_result, sami_result):
    merged_data = {}

    # Helper function to add data to the merged_data dictionary
    def add_data_to_merged(data, sensor_name):
        for row in data[1:]:  # Skip headers
            timestamp = row['TIMESTAMP']
            # Convert timestamp to ISO format
            dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
            dt_utc = dt.replace(tzinfo=timezone.utc)
            iso_timestamp = dt_utc.strftime('%Y-%m-%dT%H:%M:%S') + 'Z'

            if iso_timestamp not in merged_data:
                merged_data[iso_timestamp] = {'TIMESTAMP': iso_timestamp}
            for key, value in row.items():
                if key != 'TIMESTAMP':
                    # Correct the field name for System_Current
                    if sensor_name == 'System' and key == 'System_Current':
                        key = 'Current'
                    merged_data[iso_timestamp][f"{sensor_name}_{key}"] = value

    # Add data from each sensor to the merged_data dictionary
    add_data_to_merged(system_result, 'System')
    add_data_to_merged(sbe37_result, 'SBE37')
    add_data_to_merged(doppler_result, 'Doppler')
    add_data_to_merged(meteo_result, 'Meteo')
    add_data_to_merged(sami_result, 'Sami')

    # Sort the merged data by timestamp
    sorted_timestamps = sorted(merged_data.keys())
    sorted_data = [merged_data[timestamp] for timestamp in sorted_timestamps]

    return sorted_data

def export_merged_data_to_csv(merged_data, output_file, headers_order):
    if not merged_data:
        print("No hay datos para exportar.")
        return

    # Ensure all rows have the same keys
    for row in merged_data:
        for header in headers_order:
            if header not in row:
                row[header] = ''

    # Check for any unexpected fields
    for row in merged_data:
        for key in row.keys():
            if key not in headers_order:
                print(f"Unexpected field: {key}")

    # Write to CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers_order)
        writer.writeheader()
        for row in merged_data:
            writer.writerow(row)

    print(f'Data has been successfully exported to {output_file}')

if __name__ == "__main__":
    meteo_input_file = 'temporal_mds/BoiaBarcelona_Meteo.dat'
    sbe37_input_file = 'temporal_mds/BoiaBarcelona_SBE37_SMPO.dat'
    doppler_input_file = 'temporal_mds/BoiaBarcelona_Doppler.dat'
    sami_input_file = 'temporal_mds/BoiaBarcelona_Sami.dat'
    system_input_file = 'temporal_mds/BoiaBarcelona_System.dat'

    # Call the functions and get the results
    meteo_result = Meteo_data_proces(meteo_input_file)
    sbe37_result = SBE37_SMPO_data_proces(sbe37_input_file)
    doppler_result = Doppler_data_proces(doppler_input_file)
    sami_result = Sami_data_proces(sami_input_file)
    system_result = System_data_proces(system_input_file)

    # Merge the results by timestamp
    merged_data = merge_data_by_timestamp(system_result, sbe37_result, doppler_result, meteo_result, sami_result)

    # Define the headers order
    headers_order = [
        'TIMESTAMP',
        'Meteo_Latitude', 'Meteo_Longitude', 'Meteo_HASL', 'Meteo_Rel_WindDir', 'Meteo_Corr_WindDir', 'Meteo_Corr_WindS', 'Meteo_WindDir_True', 'Meteo_Rel_WS', 'Meteo_BP', 'Meteo_RH', 'Meteo_AirTemp', 'Meteo_DP', 'Meteo_AD', 'Meteo_WBT',
        'SBE37_SBE37Sn', 'SBE37_SBE37Temp', 'SBE37_SBE37Cond', 'SBE37_SBE37Pres', 'SBE37_SBE37OXY', 'SBE37_SBE37Sal',
        'Doppler_DoppVolts', 'Doppler_DoppSoundSpeed', 'Doppler_DoppHeading', 'Doppler_DoppPitch', 'Doppler_DoppRoll', 'Doppler_DoppPress', 'Doppler_DoppTemp',
        'Doppler_DoppCell(1)', 'Doppler_DoppCell(2)', 'Doppler_DoppCell(3)', 'Doppler_DoppCell(4)', 'Doppler_DoppCell(5)', 'Doppler_DoppCell(6)', 'Doppler_DoppCell(7)', 'Doppler_DoppCell(8)', 'Doppler_DoppCell(9)', 'Doppler_DoppCell(10)', 'Doppler_DoppCell(11)', 'Doppler_DoppCell(12)', 'Doppler_DoppCell(13)', 'Doppler_DoppCell(14)', 'Doppler_DoppCell(15)', 'Doppler_DoppCell(16)', 'Doppler_DoppCell(17)', 'Doppler_DoppCell(18)', 'Doppler_DoppCell(19)', 'Doppler_DoppCell(20)', 'Doppler_DoppCell(21)', 'Doppler_DoppCell(22)', 'Doppler_DoppCell(23)', 'Doppler_DoppCell(24)', 'Doppler_DoppCell(25)', 'Doppler_DoppCell(26)', 'Doppler_DoppCell(27)', 'Doppler_DoppCell(28)', 'Doppler_DoppCell(29)', 'Doppler_DoppCell(30)', 'Doppler_DoppCell(31)', 'Doppler_DoppCell(32)', 'Doppler_DoppCell(33)', 'Doppler_DoppCell(34)', 'Doppler_DoppCell(35)', 'Doppler_DoppCell(36)', 'Doppler_DoppCell(37)', 'Doppler_DoppCell(38)', 'Doppler_DoppCell(39)', 'Doppler_DoppCell(40)',
        'Sami_SamiData', 'Sami_SamiMessage', 'Sami_SamiNBlank',
        'System_PanelTemp', 'System_Datalogg_Batt', 'System_Batt_Volt', 'System_Solar_Voltage', 'System_Current', 'System_CTD_PwrOff', 'System_ADP_PwrOff', 'System_SAMI_PwrOff', 'System_Meteo_PwrOff'
    ]

    # Export the merged data to a CSV file
    output_file = 'merged_output.csv'
    export_merged_data_to_csv(merged_data, output_file, headers_order)