# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:20:30 2022

@author: p.pream kumar
"""

from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return"HELLO WORLD!"
 if __name__=='__main__':
     app.run()