import pandas as pd
import logging
from datetime import datetime
import os

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_and_reformat_xls_to_csv(file_path, output_path):
    """
    Converts an XLS file to CSV and reformats the time column.

    :param file_path: Path to the XLS file.
    :param output_path: Path where the output CSV file will be saved.
    """
    try:
        # Reading the .xls file
        logging.info(f"Reading {file_path}")
        data = pd.read_excel(file_path)

        # Checking if 'time' column exists and reformatting
        if 'time' in data.columns:
            logging.info("Reformatting 'time' column")
            data['time'] = pd.to_datetime(data['time'], format='%d/%m/%Y %H:%M').dt.strftime('%Y-%m-%d %H:%M')
        else:
            logging.warning("'time' column not found in the data")

        # Saving to .csv
        data.to_csv(output_path, index=False)
        logging.info(f"File saved as {output_path}")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

def main():
    # File paths
    base_path = r'C:\Users\DELL\Documents\Data Engineering\DataMasters DE Bootcamp\Week 3\Traffic Project\Traffic-ETL\data'
    input_file = os.path.join(base_path, 'traffic_spreadsheet.xls')
    output_file = os.path.join(base_path, 'traffic_data.csv')

    # Convert and reformat the XLS file
    convert_and_reformat_xls_to_csv(input_file, output_file)

if __name__ == "__main__":
    main()
