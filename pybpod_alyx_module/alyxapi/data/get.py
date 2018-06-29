import requests
import json
from pyforms import conf

class Get():
    def __init__(self,_apibase):
        self.apibase = _apibase

    def allprojects(self):
        result = requests.get(conf.ALYX_ADDR+'/projects',headers= self.apibase.headers)
        if result.ok:
            result_data = result.json()
            for a in result_data:
                print(a)
    
    def project(self,_name):
        result = requests.get(conf.ALYX_ADDR+'/projects/'+_name,headers= self.apibase.headers)
        if result.ok:
            print(result.json())

    def alldatasettypes(self):
        result = requests.get(conf.ALYX_ADDR+'/dataset-types',headers= self.apibase.headers)
        if result.ok:
            result_data = result.json()
            for a in result_data:
                print(a)

    def datasettype(self, _name):
        result = requests.get(conf.ALYX_ADDR+'/dataset-types/'+_name,headers= self.apibase.headers)
        if result.ok:
            print(result.json())

    
    def alldataformats(self):
        result = requests.get(conf.ALYX_ADDR+'/data-formats',headers= self.apibase.headers)
        if result.ok:
            result_data = result.json()
            for a in result_data:
                print(a)

    def dataformat(self, _name):
        result = requests.get(conf.ALYX_ADDR+'/data-formats/'+_name,headers= self.apibase.headers)
        if result.ok:
            print(result.json())

    def alldatasets(self):
        result = requests.get(conf.ALYX_ADDR+'/datasets',headers= self.apibase.headers)
        if result.ok:
            result_data = result.json()
            for a in result_data:
                print(a)
    
    def dataset(self,_name):
        result = requests.get(conf.ALYX_ADDR+'/datasets/'+_name,headers= self.apibase.headers)
        if result.ok:
            print(result.json())

    def allfiles(self):
        result = requests.get(conf.ALYX_ADDR+'/files',headers= self.apibase.headers)
        if result.ok:
            result_data = result.json()
            for a in result_data:
                print(a)
    
    def files(self,_name):
        result = requests.get(conf.ALYX_ADDR+'/files/'+_name,headers= self.apibase.headers)
        if result.ok:
            print(result.json())


    def alldatarepositorytypes(self):
        result = requests.get(conf.ALYX_ADDR+'/data-repository-type',headers= self.apibase.headers)
        if result.ok:
            result_data = result.json()
            for a in result_data:
                print(a)

    def repositorytype(self, _name):
        result = requests.get(conf.ALYX_ADDR+'/data-repository-type/'+_name,headers= self.apibase.headers)
        if result.ok:
            print(result.json())

    def alldatarepositories(self):
        result = requests.get(conf.ALYX_ADDR+'/data-repository',headers= self.apibase.headers)
        if result.ok:
            result_data = result.json()
            for a in result_data:
                print(a)

    def datarepositoryty(self, _name):
        result = requests.get(conf.ALYX_ADDR+'/data-repository/'+_name,headers= self.apibase.headers)
        if result.ok:
            print(result.json())
