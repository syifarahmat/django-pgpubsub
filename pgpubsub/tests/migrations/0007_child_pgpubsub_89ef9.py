# Generated by Django 3.2.12 on 2023-05-19 13:55

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_child_parent'),
    ]

    operations = [
        pgtrigger.migrations.AddTrigger(
            model_name='child',
            trigger=pgtrigger.compiler.Trigger(name='pgpubsub_89ef9', sql=pgtrigger.compiler.UpsertTriggerSql(declare='DECLARE payload TEXT;', func="\n            \n            payload := json_build_object(\n                'app', 'tests',\n                'model', 'Child',\n                'old', row_to_json(OLD),\n                'new', row_to_json(NEW)\n              );\n        \n            \n            INSERT INTO pgpubsub_notification (channel, payload)\n            VALUES ('pgpubsub_89ef9', to_json(payload::text));\n        \n            perform pg_notify('pgpubsub_89ef9', payload);\n            RETURN NEW;\n        ", hash='d2d276ef8c024dff4f84c145a99fabb8890d7b8a', operation='UPDATE OR INSERT', pgid='pgtrigger_pgpubsub_89ef9_92bc1', table='tests_child', when='AFTER')),
        ),
    ]