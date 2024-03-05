import requests
import xmlrpc.client
from typing import Union

import uvicorn
import os
import telnyx
from fastapi import FastAPI, Request
from dotenv import load_dotenv

app = FastAPI()


url2 = "https://api.tiltx.com/sms/send-sms/"

url = 'https://crm.jusbryn.com'
db = 'Jusbryn'
username = 'crm.projems@gmail.com'
password = 'trcadminprojems'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

if uid:
    print('authentication success')
else:
    print('authentication failed')

headers = {
  'x-api-key': 'myiu7paGri7uj4Ocg9gcnaK1p5kMGOQmaWeFSkrE',
  'Content-Type': 'application/text',
  'Authorization': 'Bearer KEY0182C747BA632A6D552A8797B7478A7E_2qfCpjq7ro5JmOh2CEu87M'
}

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/messaging/send_sms/")
async def send_sms(request: Request):
    params = request.query_params
    payload = '{\r\n\"from\": \"'+(params.get("from"))+'\",\r\n\"to\": \"'+(params.get("to"))+'\",\r\n\"text\": \"'+(params.get("text"))+'\"\r\n}'
    response = requests.request("POST", url2, headers=headers, data=payload)
    print(response.text)

@app.get("/api/messaging/send_sms2/")
async def send_sms2(request: Request):
    params = request.query_params
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    #id2 = models.execute_kw(db, uid, password, 'res.partner', 'create', 
                           #[{ 'name' : params.get('partner_name') }])
    id = models.execute_kw(db, uid, password, 'crm.lead', 'create', 
                           [{ 'name' : params.get('name'), 'contact_name' : params.get('contact_name'), 'phone' : params.get('phone'), 'email_from' : params.get('email_from'),
                           'mobile' : params.get('mobile'), 'cus_product' : params.get('cus_product'), 'cus_title' : params.get('cus_title'), 'street' : params.get('street'),
                           'state_id' : params.get('state_id'), 'city' : params.get('city'), 'zip' : params.get('zip'), 'cus_aptdate' : params.get('cus_aptdate'),
                           'cus_apttime' : params.get('cus_apttime'), 'cus_description' : params.get('cus_description'), 'cus_marital' : params.get('cus_marital')}])
    #id2 = models.execute_kw(db, uid, password, 'res.partner', 'create', 
                           #[{ 'name' : params.get('contact_name') }])
    return("Message Sent Successfully", id )

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8100, reload=True)
