# ecc_uds_pipeline

### Over view:
A ETL script to dumping email data from MySQL, transforming the normalized data into a flat data schema and upload to Hive
This ETL refreshing logic will be fully updating. 

- Script log: /var/log/ecc_uds_pipelog.log <br>
- Configure file: [project_root]/config.ini <br>
- Temp dump file path: [project_root]/tmp/ <br>
- Slack notification chanel: #ws-prod-automated

### Usage:
cd [PROJECT_ROOT] && python ecc_uds_pipeline.py -e [prod|dev] >> /var/log/ecc_uds_pipelog.log

- -e: enviroment parameter: prod or dev, default value is prod.

### Crontab:
```
30 1 * * * cd [project_root] && python ecc_uds_etl.py `date -d"-1 day" '+%Y%m%d'`
```

python ecc_uds_pipeline.py -e prod >> /var/log/ecc_uds_pipelog.log
