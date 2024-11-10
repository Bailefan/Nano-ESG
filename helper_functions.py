import numpy as np
import pandas as pd


def filter_data(data, company, aspect_filter):
    '''
    Filters ESG sentiment data and sorts by date.

    Args:
        company (str): The company name to filter the data. If None, all companies are included.
        aspect_filter (str): The aspect to filter by ('env_soc', 'env_gov', 'soc_gov', or specific aspect).
        
    Returns:
        pd.DataFrame: A DataFrame with daily sentiment scores sorted by date.
    
    '''
    if company:
        data_comp = data[data['company'] == company]
    else:
        data_comp = data.copy()
    if aspect_filter:
        data_comp = data_comp[data_comp['aspect'] == aspect_filter]
    
    data_comp = data_comp.sort_values(by='date')

    return data_comp

def calculate_daily_data(data, start_date, end_date, fill_edges=True):
    """Takes the input data and converts it into daily values based on the input parameters.

    Args:
        data (pd.DataFrame): The input data containing ESG sentiment information.
        start_date (str): The start date for the filtering in 'YYYY-MM-DD' format.
        end_date (str): The end date for the filtering in 'YYYY-MM-DD' format.
        fill_edges(bool): Whether to fill the edges with 0s/ffill.

    Raises:
        Exception: If the daily sentiment is below -1 or above 1.

    Returns:
        dataframe: Daily data with sentiment and relevance scores.
    """

    esg_sentiment = data[['date', 'sentiment_int', 'relevance_score']]
    if len(esg_sentiment) == 0:
        #Return empty dataframe from start to end date
        daily_data = pd.DataFrame(index=pd.date_range(start_date, end_date, freq='D'))
        daily_data['sentiment_int'] = [0] * len(daily_data)
        return daily_data

    daily_data = esg_sentiment.resample('d', on='date').mean()
    
    if np.max(daily_data['sentiment_int']) > 1 or np.min(daily_data['sentiment_int']) < -1:
        raise Exception('Sentiment is not in the expected range!')

    if fill_edges:
        #missing days with 0 (neutral) if the company has no data for the day
        daily_data = daily_data.reindex(pd.date_range(start_date, end_date, freq='D'))
        daily_data.fillna(0, inplace=True)

    return daily_data