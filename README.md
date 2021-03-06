# Flask-RESTful API project

#### Please note that public access to this repository will disappear in 2 days

This project shows one of the possible ways to implement RESTful API server: import xlsx and export json. It is worth noting that this is the MVP version of the service. It has not been tested and there are some architectural problems that generally do not affect the functionality of the service.

To learn more about the approach to the project and the stages, follow the link - https://docs.google.com/document/d/1AptbmwC4PmcfOXYc-qPs8QA8-blSoTY8hAzfG4m6yy0/edit?usp=sharing

<b>Forewarned is forearmed</b>.

## TECH
1. [Flask-RESTful] - restful API library.
2. [Flask-SQLAlchemy] - adds support for SQLAlchemy ORM.
3. [Pandas] - convert df to sql and from sql to df

## Project structure:
```
├── README.md
├── app.py
├── db.py
├── config.py
├── models.py
├── resources.py
├── requirements.txt
│── service
│       │── utils
│       │     ├── logger.py
│       │     ├── export.py
│       │     ├── parsing.py
│       │     ├── queries.py
│       │     ├── responses.py
│       │     ├── create_view.py
│       │     
│       ├── export_service.py
│       └── import_service.py
```

## Installation

1. Create PostgreSQL database
2. Create and fill .env using .env.example
3. Install requirements using python3.9 -m pip install -r requirements.txt

The required python version is 3.9

## Usage

**POSTMAN COLLECTION -** 
https://documenter.getpostman.com/view/20800782/UzJFvJB9


##### POST {{server}}/import/xlsx

##### Request
```json
{
    "path": "testData.xlsx"
}
```
##### Response
```json
{
    "message": "File testData.xlsx uploaded successfully"
}
```

#### Error messages
*   "The path field cannot be empty. Example {'path': 'testData.xlsx'}"
*   "An internal error occurred when loading the {name} table into the database"
*   "File {} can not be found in server. Check file name"
*   "Specify the path to the file in the format {'path': 'testData.xlsx'}"
*   "Use one of the available formats: xlsx, xls"


##### GET {{server}}/export/sql

##### Response
```json
{
  "df": [
    {
      "id": 1,
      "rep_dt": "2020-01-31",
      "delta": 7384271.5,
      "delta_lag": 3849508.2
    },
    {
      "id": 2,
      "rep_dt": "2020-02-29",
      "delta": 7784508.5,
      "delta_lag": 69066016.0
    }
  ]
}
```
##### GET {{server}}/export/pandas

##### Response
```json
{
  "df": [
    {
      "id": 1,
      "rep_dt": "2020-01-31",
      "delta": 7384271.5,
      "delta_lag": 3849508.2
    },
    {
      "id": 2,
      "rep_dt": "2020-02-29",
      "delta": 7784508.5,
      "delta_lag": 69066016.0
    }
  ]
}
```
##### GET {{server}}/export/sql?lag_num=3

##### Response
```json
{
  "df": [
    {
      "id": 1,
      "rep_dt": "2020-01-31",
      "delta": 7384271.5,
      "delta_lag": 69066016.0
    },
    {
      "id": 2,
      "rep_dt": "2020-02-29",
      "delta": 7784508.5,
      "delta_lag": 688557.3
    },
    {
      "id": 3,
      "rep_dt": "2020-03-31",
      "delta": 3849508.2,
      "delta_lag": 1640127.0
    },
    {
      "id": 4,
      "rep_dt": "2020-04-30",
      "delta": 69066016.0,
      "delta_lag": 6336723.5
    }
  ]
}
```
##### GET {{server}}/export/pandas?lag_num=3

##### Response
```json
{
  "df": [
    {
      "id": 1,
      "rep_dt": "2020-01-31",
      "delta": 7384271.5,
      "delta_lag": 69066016.0
    },
    {
      "id": 2,
      "rep_dt": "2020-02-29",
      "delta": 7784508.5,
      "delta_lag": 688557.3
    },
    {
      "id": 3,
      "rep_dt": "2020-03-31",
      "delta": 3849508.2,
      "delta_lag": 1640127.0
    },
    {
      "id": 4,
      "rep_dt": "2020-04-30",
      "delta": 69066016.0,
      "delta_lag": 6336723.5
    }
  ]
}
```

### Error Codes

*   "An internal error occurred when exporting file"
*   "Specify one of the available upload formats: export/pandas or export/sql"
*   "Specify the log_num parameter in the format /export/sql?log_num=. Example  
    /export/sql?log_num=4"
