# Main Flask application file
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app) # Enable Cross-Origin Resource Sharing

# Load data once when the app starts 
PROCESSED_DATA_PATH = os.path.join('../../data', '02_processed', 'brent_prices_processed.csv')
df = pd.read_csv(PROCESSED_DATA_PATH, index_col='Date', parse_dates=True)

events_data = {
    'EventDate': ['1990-08-02', '1997-07-02', '2001-09-11', '2003-03-20', '2008-09-15', '2011-01-25', '2014-11-27', '2016-11-30', '2020-03-11', '2022-02-24'],
    'EventName': ['Iraq Invades Kuwait', 'Asian Financial Crisis', '9/11 Attacks', 'Start of Iraq War', 'Lehman Collapse', 'Arab Spring', 'OPEC No-Cut', 'OPEC+ Cut', 'COVID-19 Pandemic', 'Russia Invades Ukraine']
}
events_df = pd.DataFrame(events_data)
events_df['EventDate'] = events_df['EventDate'].astype(str)


@app.route('/api/prices', methods=['GET'])
def get_prices():
    # Get query parameters for date filtering
    start_date = request.args.get('start', df.index.min().strftime('%Y-%m-%d'))
    end_date = request.args.get('end', df.index.max().strftime('%Y-%m-%d'))

    # Filter dataframe
    filtered_df = df[(df.index >= start_date) & (df.index <= end_date)]
    
    # Convert to JSON format suitable for charting libraries
    result = filtered_df.reset_index().to_dict(orient='records')
    return jsonify(result)

@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(events_df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5001) 