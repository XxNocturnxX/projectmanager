# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Update.resumen'
        db.add_column(u'projects_update', 'resumen',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Update.resumen'
        db.delete_column(u'projects_update', 'resumen')


    models = {
        u'projects.project': {
            'Meta': {'ordering': "('cliente', 'titulo')", 'object_name': 'Project'},
            'cliente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'consultores': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'detalle': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '200', 'blank': 'True'}),
            'fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'horas_acum': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'horas_asig': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'horas_sem': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'horas_totales': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lider': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Potencial'", 'max_length': '200', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'verticales': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        u'projects.update': {
            'Meta': {'object_name': 'Update'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_detalle': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'updates'", 'to': u"orm['projects.Project']"}),
            'resumen': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']