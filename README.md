# InfoSnap-API-Wrapper

This module uses two packages: requests and pandas. Right now you can call various GET requests using the PowerSchool Registration (formally InfoSnap) API.

# InfoSnap.forms()
Returns a json response of all your PS Registration Forms
```python
from InfoSnap import InfoSnap
IS = InfoSnap(api_key='your_api_key')
forms = IS.forms()
```
# InfoSnap.import_schema()
Returns the import schema for the for identified in form_id. You can get the form ID by using InfoSnap.forms()
```python
schema_j = IS.import_schema(form_id='12345', resp='json')
```
You can also return a pandas DataFrame and specify the axis 0 or 1 (default is 0):
```python
schema_df = IS.import_schema(form_id='12345', resp='frame', axis=0)
```
# InfoSnap.submissions()

Returns all your submission data as a json respose
```python
submissions_j = IS.submissions(form_id='12345', resp='json', page_size=50)
```
You can also return a pandas DataFrame:
```python
submissions_df = IS.submissions(form_id='12345', resp='frame', page_size=50)
```
