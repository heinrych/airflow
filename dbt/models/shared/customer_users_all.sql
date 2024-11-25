{{
	config(
		materialized='table',
		tags=['shared', 'daily']
	)
}}
with cte as (
	select user_id, customer_id from {{source('redshift', 'customer_users')}}
	union
	select id as user_id, customer_id from {{source('redshift', 'users')}}
)
select * from cte