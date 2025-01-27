import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].astype(str).str[:7]
    transactions['country'].fillna('unknown', inplace=True)
    result = transactions[['country','state','amount','month']]
    left = result.groupby(['month', 'country']).agg(
        trans_count = ('amount','count'),
        trans_total_amount = ('amount','sum')
    ).reset_index()
    right = result[result['state'] == 'approved'].groupby(['month', 'country']).agg(
        approved_count = ('amount','count'),
        approved_total_amount = ('amount','sum')
    ).reset_index()

    merged = left.merge(right,on=['month','country'],how='left')

    merged = merged.fillna({
        'approved_count': 0,
        'approved_total_amount': 0
    })

    # Revert 'unknown' country value to NaN if desired
    merged['country'] = merged['country'].replace('unknown', None)

    return merged
