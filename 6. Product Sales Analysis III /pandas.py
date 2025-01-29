import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    first_sales = sales.groupby("product_id").agg({"year": "min"}).reset_index()
    final = sales.merge(first_sales,on = ["product_id","year"],how = "inner").rename(columns={"year": "first_year"})
    return final[["product_id","first_year","quantity","price"]]
