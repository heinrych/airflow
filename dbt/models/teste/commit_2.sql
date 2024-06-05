

{{ config(materialized='table') }}

with source_data as (

    select *
    from raw.commits

)

select *
from source_data