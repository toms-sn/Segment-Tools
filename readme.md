# Segment Data Tools
These Python scripts generate convincing and random user records comprised of the fields you'd expect to load into Segment.  See [models/user_data](models/user_data.py) for the full list.

These scripts support 2 functions:
## 1. Write random user records as Identify() calls to Segment
This is useful to create user records in Segment.

## 2. Write random user records to JSONL file
This is handy to upload to a Google BigQuery table.

To get started, rename the `sampleconfig.py` to `config.py` and add your Segment write key.