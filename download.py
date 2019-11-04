#!/usr/bin/env python3
import os
import requests
def download(url,path='.'):
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    if req.status_code == 403:
        print('You do not have the authority to access this page.')
        return
    filename = url.split('/')[-1]
    names = os.listdir(path)
    if filename in names:
         print('The file has exsist.')
    else:
        with open(filename,'w') as fobj:
            fobj.write(req.content.decode('utf-8'))
        print('Download over.')
if __name__ == '__main__':
    url = input('Enter a url:')
    download(url)
