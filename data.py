import pandas as pd
import duckdb

budget_history_df = pd.read_csv("planetary_science_budget_history.csv")
budget_inflation_df = pd.read_csv("budget_history_inflation_adj.csv")

budget_history_df = duckdb.sql(
    """
SELECT year, request, actual, congress 
FROM budget_history_df
WHERE year <= 2022
"""
).df()

budget_inflation_df = duckdb.sql(
    """
SELECT year, request, actual 
FROM budget_inflation_df
WHERE year <= 2022
"""
).df()

budget_df = duckdb.sql(
    """
SELECT b.year, binf.request, binf.actual, b.congress
FROM budget_history_df b INNER JOIN budget_inflation_df binf
ON b.year = binf.year
ORDER BY b.year                                        
"""
).df()

budget_df.to_csv("budget_data.csv", index=False)

funding_destination_df = pd.read_csv("funding_by_destination_decades.csv")

print(funding_destination_df)
print()
