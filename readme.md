# Segment Data Tools
These Python scripts generate convincing and random user records comprised of the fields you'd expect to load into Segment.  See [models/user_data](models/user_data.py) for the full list.

_Important:_ To get started, rename the `sampleconfig.py` to `config.py` and add your Segment write key.

These scripts support 2 functions:
## Write random user records as Identify() calls to Segment
This is useful to create user records in Segment.

To send records to Segment,

1. edit ```config.py``` and change ```NUM_ITERATIONS``` to the desired number of Identify() calls.
2. call ``` python main.py ```

## Write random user records to local text file
This outputs a JSONL-formatted file, handy for uploading to a Google BigQuery table.

*Generate default number of records (from config.py):*

``` python generate_dataset.py ```

*Generate 1000 records:*

``` python generate_dataset.py -n 1000 ```

*Custom output filename:*

``` python generate_dataset.py -o my_bigquery_data.jsonl ```

*Preview samples without saving:*

``` python generate_dataset.py --preview ```

*Preview more samples:*

``` python generate_dataset.py --preview --preview-count 5 ```

