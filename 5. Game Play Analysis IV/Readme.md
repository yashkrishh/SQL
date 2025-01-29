## Finding the Fraction of Players Who Logged in the Next Day

### Step 1: Find Each Player’s First Login Date  
The `first_login` **Common Table Expression (CTE)** retrieves the earliest (`MIN(event_date)`) login date for each `player_id`.

### Step 2: Self-Join to Find Logins on the Next Day  
We join the `Activity` table on `player_id`, checking if the `event_date` is exactly **one day after** the first login date.

### Step 3: Count Players Who Logged in on the Next Day  
- `COUNT(DISTINCT a.player_id)`: Counts unique players who logged in the day after their first login.  
- `COUNT(DISTINCT f.player_id)`: Counts all unique players from the `first_login` CTE.

### Step 4: Compute the Fraction and Round to Two Decimal Places  
We divide the count of players who logged in the next day by the total number of players and use `ROUND(..., 2)` to get the result with two decimal places.

### Complexity Analysis  
This solution efficiently calculates the required fraction in **O(N log N)** complexity due to the `GROUP BY` operation.
