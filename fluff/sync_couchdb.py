from django.db.models import signals
import os
from couchdbkit.ext.django.loading import get_db
from pillowtop.run_pillowtop import import_pillows
from dimagi.utils.couch.sync_docs import sync_design_docs as sync_docs


FLUFF = 'fluff'


def sync_design_docs(temp=None):
    dir = os.path.abspath(os.path.dirname(__file__))
    for pillow in import_pillows():
        app_label = pillow.indicator_class._meta.app_label
        db = get_db(app_label)

        sync_docs(db, os.path.join(dir, "_design"), FLUFF, temp=temp)


def catch_signal(app, **kwargs):
    """Function used by syncdb signal"""
    app_name = app.__name__.rsplit('.', 1)[0]
    app_label = app_name.split('.')[-1]
    if app_label == FLUFF:
        sync_design_docs()


def copy_designs(temp='tmp', delete=True):
    for pillow in import_pillows():
        app_label = pillow.indicator_class._meta.app_label
        db = get_db(app_label)

        copy_designs(db, FLUFF)


signals.post_syncdb.connect(catch_signal)
