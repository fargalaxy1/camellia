# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UnnostroTe.prezzo_hg'
        db.add_column(u'website_unnostrote', 'prezzo_hg',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UnnostroTe.prezzo_hg'
        db.delete_column(u'website_unnostrote', 'prezzo_hg')


    models = {
        u'website.accessorite': {
            'Meta': {'ordering': "['id']", 'object_name': 'AccessoriTe'},
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingfree': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingminiatura': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingslider': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immagine': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'prezzo': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'website.categoriete': {
            'Meta': {'object_name': 'CategorieTe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'website.immaginichisiamo': {
            'Meta': {'object_name': 'ImmaginiChiSiamo'},
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingcarousel': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingrender': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingslide': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingthumb': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'designbig': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'designnews': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'designthumb': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'didascalia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slidepage': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'website.immaginilocale': {
            'Meta': {'object_name': 'ImmaginiLocale'},
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingcarousel': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingrender': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingslide': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingthumb': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'designbig': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'designnews': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'designthumb': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'didascalia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slidepage': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'website.slider': {
            'Meta': {'object_name': 'Slider'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'didascalia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slidepage': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'website.unnostrote': {
            'Meta': {'ordering': "['id']", 'object_name': 'UnnostroTe'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.CategorieTe']", 'null': 'True', 'blank': 'True'}),
            'cropping': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingfree': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingminiatura': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingslider': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'croppingthumb': (u'django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'descrizione': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgContenitore': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imgSfuso': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'imgTazza': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'prezzo_hg': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'temperatura': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tempoInfusione_min': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['website']