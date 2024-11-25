{{
	config(
		materialized='view',
		tags=['product','daily']
	)
}}
WITH trigger_data AS (
    SELECT
        channel_id,
        user_id,
        contact_id,
        phone,
        chat_id,
        message_id,
        close_before,
        result,
        close_after,
        customer_id,
        date_occur
    FROM
        {{ source('logs_trigger', 'trigger') }}
    limit 1
)
SELECT * FROM trigger_data
