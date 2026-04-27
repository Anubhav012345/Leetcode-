SELECT
    user_id, 
    count(prompt) as prompt_count,
    ROUND(avg(tokens),2) as avg_tokens
FROM prompts 
GROUP BY user_id
HAVING COUNT(prompt) > 2 AND MAX(tokens) > AVG(tokens) 
ORDER BY avg(tokens) desc, user_id;