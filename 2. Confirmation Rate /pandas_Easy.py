import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    
    # Merge Signups and Confirmations
    merged = signups.merge(confirmations, on='user_id', how='left')
    
    # Step 1: Calculate the total number of actions per user
    total_actions = merged.groupby('user_id').size().reset_index(name='total_actions')
    
    # Step 2: Calculate the number of confirmed actions per user
    confirmed_actions = merged[merged['action'] == 'confirmed'].groupby('user_id').size().reset_index(name='confirmed_actions')
    
    # Step 3: Merge total actions and confirmed actions
    result = total_actions.merge(confirmed_actions, on='user_id', how='left')
    
    # Step 4: Fill NaN values in confirmed_actions with 0 (for users with no confirmed actions)
    result['confirmed_actions'] = result['confirmed_actions'].fillna(0)
    
    # Step 5: Calculate the confirmation rate
    result['confirmation_rate'] = round(result['confirmed_actions'] / result['total_actions'], 2)
    
    # Return only the user_id and confirmation_rate columns
    return result[['user_id', 'confirmation_rate']]
