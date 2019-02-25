import requests
import pandas as pd
from pandas.io.json import json_normalize


class InfoSnap(object):
    """
    InfoSnap uses the requests package to preform
    various get requests with the InfoSnap API
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def forms(self):
        """
        uses publishedactions to get information from all the forms

        :return: json response of all form information

        from InfoSnap import InfoSnap
        IS = InfoSnap(api_key = 'api_key')
        IS.forms()

        [{"id": 123, "title": "Enrollment", "academicYear": "2008-2009"},
         {"id": 456, "title": "Registration", "academicYear": "2009-2010"}]

        """

        url = 'http://secure.infosnap.com/api/v1/publishedactions'
        r = requests.get(url, auth=(self.api_key, ''))
        return r.json()

    def import_schema(self, form_id, resp='json', axis=0):
        """
        Takes a look at the import schema for a specific Form
        :param form_id: the form ID
        :param resp: type of response -- if json then a json response else a Pandas data frame of the whole json
        :param axis: if 0 then return fields as rows else return fields as columns
        :return: returns a json or a pandas data frame

         IS = InfoSnap(api_key='your_key')
         IS.forms() # to get form id
         df = IS.import_schema(id='16376', type='frame') # data frame example
         json_resp = IS.import_schema(id='16376', type='json') # json example
        """

        url = 'http://secure.infosnap.com/api/v1/publishedactions/'+form_id+'/importschemas'
        r = requests.get(url, auth=(self.api_key, ''))

        if resp == 'json':
            return r.json()

        else:
            data = r.json()
            if axis == 0:
                dfs = []

                for i in range(len(data)):
                    df = pd.DataFrame(data[i])['fields'].to_frame()
                    df.columns = [data[i]['title'] + ' Fields']
                    dfs.append(df)
                return dfs

            else:
                dfs = []
                for i in range(len(data)):
                    df = pd.DataFrame(data[i])['fields'].to_frame().set_index('fields').T
                    dfs.append(df)
                return dfs

    def submissions(self, form_id, resp='json', page_size=50):
        """
         Looks at all the submission data for the form identified
         
        :param form_id: the form id from infosnap
        :param resp: response type default to json but could be frame
        :param page_size: how many results to return default is 50
        :return: returns all submissions in either a json format or DataFrame
        """

        url = f'http://secure.infosnap.com/api/v1/publishedactions/{form_id}/submissionrecords?pagesize={page_size}'
        r = requests.get(url, auth=(self.api_key, ''))

        if resp == 'json':
            return r.json()
        else:
            return json_normalize(r.json()['records'])

