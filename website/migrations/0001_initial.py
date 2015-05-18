# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategorieTe'
        db.create_table(u'website_categoriete', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'website', ['CategorieTe'])

        # Adding model 'UnnostroTe'
        db.create_table(u'website_unnostrote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.CategorieTe'], null=True, blank=True)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('imgSfuso', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('imgContenitore', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('imgTazza', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('tempoInfusione_min', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('temperatura', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('croppingthumb', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingminiatura', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingslider', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingfree', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'website', ['UnnostroTe'])

        # Adding model 'AccessoriTe'
        db.create_table(u'website_accessorite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('immagine', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('prezzo', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('croppingminiatura', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingslider', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingfree', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'website', ['AccessoriTe'])

        # Adding model 'ImmaginiLocale'
        db.create_table(u'website_immaginilocale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('didascalia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('slidepage', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingthumb', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingslide', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingcarousel', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingrender', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('designthumb', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('designbig', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('designnews', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'website', ['ImmaginiLocale'])

        # Adding model 'ImmaginiChiSiamo'
        db.create_table(u'website_immaginichisiamo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('didascalia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('slidepage', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingthumb', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingslide', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingcarousel', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('croppingrender', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('designthumb', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('designbig', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('designnews', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'website', ['ImmaginiChiSiamo'])

        # Adding model 'Slider'
        db.create_table(u'website_slider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('didascalia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cropping', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('slidepage', self.gf(u'django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'website', ['Slider'])


    def backwards(self, orm):
        # Deleting model 'CategorieTe'
        db.delete_table(u'website_categoriete')

        # Deleting model 'UnnostroTe'
        db.delete_table(u'website_unnostrote')

        # Deleting model 'AccessoriTe'
        db.delete_table(u'website_accessorite')

        # Deleting model 'ImmaginiLocale'
        db.delete_table(u'website_immaginilocale')

        # Deleting model 'ImmaginiChiSiamo'
        db.delete_table(u'website_immaginichisiamo')

        # Deleting model 'Slider'
        db.delete_table(u'website_slider')


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
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'temperatura': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tempoInfusione_min': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['website']