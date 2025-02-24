# Email Campaign Queries for PostgreSQL and SQLite

## 1. Counting the Number of Emails Sent for Each Campaign
**PostgreSQL & SQLite**
```sql
SELECT campaign_id, COUNT(*) AS emails_sent
FROM email_sends
GROUP BY campaign_id;
```

## 2. Counting the Number of Emails Sent Each Week in the Last Half Year

### PostgreSQL Version
```sql
SELECT TO_CHAR(event_time, 'IYYY-IW') AS week_start, 
       COUNT(*) AS emails_sent
FROM email_sends
WHERE event_time >= CURRENT_DATE - INTERVAL '6 months'
GROUP BY week_start
ORDER BY week_start;
```

### SQLite Version
```sql
SELECT strftime('%Y-%W', event_time) AS week_start, 
       COUNT(*) AS emails_sent
FROM email_sends
WHERE event_time >= date('now', '-6 months')
GROUP BY week_start
ORDER BY week_start;
```

## 3. Calculating the Open Rate for Each Campaign

**PostgreSQL & SQLite**
```sql
SELECT es.campaign_id, 
       CASE 
           WHEN COUNT(DISTINCT es.user_id) = 0 THEN 0
           ELSE COUNT(DISTINCT eo.user_id) * 1.0 / NULLIF(COUNT(DISTINCT es.user_id), 0)
       END AS open_rate
FROM email_sends es
LEFT JOIN email_opens eo 
ON es.campaign_id = eo.campaign_id AND es.user_id = eo.user_id
GROUP BY es.campaign_id;
```