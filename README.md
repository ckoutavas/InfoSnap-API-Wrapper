# InfoSnap-API-Wrapper

This module uses two packages: requests and pandas. Right now you can call various GET requests using the PowerSchool Registration (formally InfoSnap) API.

# InfoSnap.forms()
Returns a json response of all your PS Registration Forms

>>> from InfoSnap import InfoSnap
>>> IS = InfoSnap(api_key='your_api_key')
>>> IS.forms()

# InfoSnap.import_schema
Returns the import schema for the for identified in form_id. You can get the form ID by using InfoSnap.forms()

`>>> schema = IS.import_schema(form_id='12345', resp='json')`

You can also return a pandas DataFrame and specify the axis 0 or 1 (default is 0):

`>>> schema = IS.import_schema(form_id='12345', resp='frame', axis=0)`

# InfoSnap.submission()

Returns all your submission data as a json respose

`>>> j = IS.submissions(form_id='16376', resp='json', page_size=50)`

You can also return a pandas DataFrame:

`>>> df_submissions = IS.submissions(form_id='12345', resp='frame', page_size=50)`
