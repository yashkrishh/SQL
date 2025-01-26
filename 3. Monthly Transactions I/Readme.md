### Edge Cases Solved by `COALESCE`
1. **No Matching Rows in Join**  
   When a `LEFT JOIN` finds no matching rows, the right-hand table values become `NULL`.  
   - **Without `COALESCE`:** Results have `NULL` counts and sums.
   - **With `COALESCE`:** Replace `NULL` with `0` for better clarity.

   **Example:**
   | month   | country | trans_count | approved_count |
   | ------- | ------- | ----------- | -------------- |
   | 2018-12 | US      | 2           | 0              |

2. **Missing Aggregates**  
   If there are no rows for a specific group, `SUM` or `COUNT` return `NULL`.  
   - **Without `COALESCE`:** Aggregates are `NULL`.  
   - **With `COALESCE`:** Aggregates default to `0`.

   **Example:**
   | month   | country | trans_total_amount |
   | ------- | ------- | ------------------ |
   | 2019-01 | CA      | 0                  |

---

### Edge Cases Solved by `(a.country IS NULL AND b.country IS NULL)`
1. **Matching `NULL` Values**  
   SQL treats `NULL = NULL` as `FALSE`, so `NULL` rows are excluded unless explicitly handled.

   **Example:**
   - Without `(IS NULL)`:
     | month   | country | approved_count |
     | ------- | ------- | -------------- |
     | 2019-01 | NULL    | NULL           |
   - With `(IS NULL)`:
     | month   | country | approved_count |
     | ------- | ------- | -------------- |
     | 2019-01 | NULL    | 1              |

2. **Preserving `NULL` Rows**  
   Ensures rows with `NULL` values in the `country` column are not lost in joins.

---

### Summary
- **`COALESCE`:** Handles missing data by replacing `NULL` with `0` in aggregates and joins.
- **`(a.country IS NULL AND b.country IS NULL)`:** Matches `NULL` values to ensure data completeness.
