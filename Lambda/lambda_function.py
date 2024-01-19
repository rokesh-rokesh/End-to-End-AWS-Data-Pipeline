from data_ingestion_to_S3 import dowmload

balance_sheet = [
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?limit=5&apikey=key_id",
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/IBM?limit=5&apikey=",
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/GOOGL?limit=5&apikey=",
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/MSFT?limit=5&apikey=",
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/META?limit=5&apikey=",
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/TSLA?limit=5&apikey=",
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/NVDA?limit=5&apikey=",
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/AMZN?limit=5&apikey=",
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/NFLX?limit=5&apikey=",
    "https://financialmodelingprep.com/api/v3/balance-sheet-statement/ORCL?limit=5&apikey="]


def lambda_handler(event, context):
    for bs in balance_sheet:
        res = dowmload(bs)
    return {
        'statusCode': res.status_code
    }
