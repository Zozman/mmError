# -*- coding: utf-8 -*-
from mindmeld import Application

__version__ = "0.0.1"

app = Application(__name__)

__all__ = ['app']

@app.handle(intent='greeting')
def greeting(request, responder):
    responder.reply('greeting')

@app.handle(intent='is_live')
def is_live(request, responder):
    responder.reply('is_live')

@app.handle(default=True)
def default(request, responder):
    responder.reply('default')

