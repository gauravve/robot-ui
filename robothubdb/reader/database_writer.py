#  Copyright 2013-2014 Nokia Solutions and Networks
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from robothubdb import RobotDatabase
from robothubdb import logger

class SQLLiteDatabaseWriter(RobotDatabase):
    application_name = ''

    def __init__(self, db_file_path, verbose_stream,application_name):
        self.application_name = application_name
        super(SQLLiteDatabaseWriter, self).__init__(db_file_path, verbose_stream)
        self._init_schema()

    def _init_schema(self):
        self._verbose('- Initializing database schema')
        self._create_table_project()
        self._create_table_application()
        self._create_table_test_run()
        self._create_table_test_run_status()
        self._create_table_test_run_errors()
        self._create_table_tag_status()
        self._create_table_suite()
        self._create_table_suite_status()
        self._create_table_test()
        self._create_table_test_status()
        self._create_table_keyword()
        self._create_table_keyword_status()
        self._create_table_message()
        self._create_table_tag()
        self._create_table_argument()
        self._populate_project_and_application()

    def _populate_project_and_application(self):
        self._verbose('- Adding values to projects and applications tables')
#        cursor = self._connection.execute("INSERT INTO robothub_project (id, project_name) VALUES ('ACP', 'Atlassian Competency')")
#        cursor = self._connection.execute("INSERT INTO robothub_application (id, application_name, project_id, git_link, framework_name, jira_link) VALUES ('JIRA', 'JIRA', 'ACP', '', '', '')")

    def _create_table_test_run(self):
        self._create_table('test_run', {
            'hash': 'TEXT NOT NULL',
            'imported_at': 'DATETIME NOT NULL',
            'source_file': 'TEXT',
            'started_at': 'DATETIME',
            'finished_at': 'DATETIME',
        }, ('hash',))

    def _create_table_test_run_status(self):
        self._create_table('test_run_status', {
            'test_run_id': 'INTEGER NOT NULL REFERENCES test_runs',
            'name': 'TEXT NOT NULL',
            'elapsed': 'INTEGER',
            'failed': 'INTEGER NOT NULL',
            'passed': 'INTEGER NOT NULL'
        }, ('test_run_id', 'name'))

    def _create_table_test_run_errors(self):
        self._create_table('test_run_error', {
            'test_run_id': 'INTEGER NOT NULL REFERENCES test_runs',
            'level': 'TEXT NOT NULL',
            'timestamp': 'DATETIME NOT NULL',
            'content': 'TEXT NOT NULL'
        }, ('test_run_id', 'level', 'content'))

    def _create_table_tag_status(self):
        self._create_table('tag_status', {
            'test_run_id': 'INTEGER NOT NULL REFERENCES test_runs',
            'name': 'TEXT NOT NULL',
            'critical': 'INTEGER NOT NULL',
            'elapsed': 'INTEGER',
            'failed': 'INTEGER NOT NULL',
            'passed': 'INTEGER NOT NULL',
        }, ('test_run_id', 'name'))

    def _create_table_suite(self):
        self._create_table('suite', {
            'suite_id': 'INTEGER REFERENCES suites',
            'xml_id': 'TEXT NOT NULL',
            'name': 'TEXT NOT NULL',
            'source': 'TEXT',
            'doc': 'TEXT',
            'application_id': 'TEXT'
        }, ('name', 'source'))

    def _create_table_application(self):
        self._create_table_text_id('application', {
            'application_name': 'TEXT',
            'framework_name': 'TEXT',
            'jira_link': 'TEXT',
            'git_link': 'TEXT',
            'project_id': 'INTEGER NOT NULL REFERENCES projects'
        })

    def _create_table_project(self):
        self._create_table_text_id('project', {
            'project_name': 'TEXT'
        })

    def _create_table_suite_status(self):
        self._create_table('suite_status', {
            'test_run_id': 'INTEGER NOT NULL REFERENCES test_runs',
            'suite_id': 'INTEGER  NOT NULL REFERENCES suites',
            'elapsed': 'INTEGER NOT NULL',
            'failed': 'INTEGER NOT NULL',
            'passed': 'INTEGER NOT NULL',
            'status': 'TEXT NOT NULL'
        }, ('test_run_id', 'suite_id'))

    def _create_table_test(self):
        self._create_table('test', {
            'suite_id': 'INTEGER NOT NULL REFERENCES suite',
            'xml_id': 'TEXT NOT NULL',
            'name': 'TEXT NOT NULL',
            'timeout': 'TEXT',
            'doc': 'TEXT'
        }, ('suite_id', 'name'))

    def _create_table_test_status(self):
        self._create_table('test_status', {
            'test_run_id': 'INTEGER NOT NULL REFERENCES test_run',
            'test_id': 'INTEGER  NOT NULL REFERENCES test',
            'status': 'TEXT NOT NULL',
            'elapsed': 'INTEGER NOT NULL'
        }, ('test_run_id', 'test_id'))

    def _create_table_keyword(self):
        self._create_table('keyword', {
            'suite_id': 'INTEGER REFERENCES suite',
            'test_id': 'INTEGER REFERENCES test',
            'keyword_id': 'INTEGER REFERENCES keyword',
            'name': 'TEXT NOT NULL',
            'type': 'TEXT NOT NULL',
            'timeout': 'TEXT',
            'doc': 'TEXT'
        }, ('name', 'type'))

    def _create_table_keyword_status(self):
        self._create_table('keyword_status', {
            'test_run_id': 'INTEGER NOT NULL REFERENCES test_run',
            'keyword_id': 'INTEGER NOT NULL REFERENCES keyword',
            'status': 'TEXT NOT NULL',
            'elapsed': 'INTEGER NOT NULL'
        })

    def _create_table_message(self):
        self._create_table('message', {
            'keyword_id': 'INTEGER NOT NULL REFERENCES keyword',
            'level': 'TEXT NOT NULL',
            'timestamp': 'DATETIME NOT NULL',
            'content': 'TEXT NOT NULL'
        }, ('keyword_id', 'level', 'content'))

    def _create_table_tag(self):
        self._create_table('tag', {
            'test_id': 'INTEGER NOT NULL REFERENCES test',
            'content': 'TEXT NOT NULL'
        }, ('test_id', 'content'))

    def _create_table_argument(self):
        self._create_table('argument', {
            'keyword_id': 'INTEGER NOT NULL REFERENCES keyword',
            'content': 'TEXT NOT NULL'
        }, ('keyword_id', 'content'))

    def _create_table(self, table_name, columns, unique_columns=()):
        definitions = ['id INTEGER PRIMARY KEY']
        for column_name, properties in columns.items():
            definitions.append('%s %s' % (column_name, properties))
        if unique_columns:
            unique_column_names = ', '.join(unique_columns)
            definitions.append('CONSTRAINT unique_%s UNIQUE (%s)' % (
                table_name, unique_column_names)
            )
        table_name = self.application_name + "_" + table_name
        sql_statement = 'CREATE TABLE IF NOT EXISTS %s (%s)' % (table_name, ', '.join(definitions))
        self._connection.execute(sql_statement)

    def _create_table_text_id(self, table_name, columns, unique_columns=()):
        definitions = ['id TEXT PRIMARY KEY']
        for column_name, properties in columns.items():
            definitions.append('%s %s' % (column_name, properties))
        if unique_columns:
            unique_column_names = ', '.join(unique_columns)
            definitions.append('CONSTRAINT unique_%s UNIQUE (%s)' % (
                table_name, unique_column_names)
            )
        table_name = self.application_name + "_" + table_name
        sql_statement = 'CREATE TABLE IF NOT EXISTS %s (%s)' % (table_name, ', '.join(definitions))
        self._connection.execute(sql_statement)

    def rename_table(self, old_name, new_name):
        sql_statement = 'ALTER TABLE %s RENAME TO %s' % (old_name, new_name)
        self._connection.execute(sql_statement)

    def drop_table(self, table_name):
        sql_statement = 'DROP TABLE %s' % table_name
        self._connection.execute(sql_statement)

    def copy_table(self, from_table, to_table, columns_to_copy):
        column_names = ', '.join(columns_to_copy)
        sql_statement = 'INSERT INTO %s(%s) SELECT %s FROM %s' % (
            to_table,
            column_names,
            column_names,
            from_table
        )
        self._connection.execute(sql_statement)

    def fetch_id(self, table_name, criteria):
        table_name_complete = self.application_name + '_' + table_name
        sql_statement = 'SELECT id FROM %s WHERE ' % table_name_complete
        sql_statement += ' AND '.join('%s=?' % key for key in criteria.keys())
        res = self._connection.execute(sql_statement, criteria.values()).fetchone()
        if not res:
            raise Exception('Query did not yield id, even though it should have.'
                            '\nSQL statement was:\n%s\nArguments were:\n%s' % (sql_statement, criteria.values()))
        return res[0]

    def insert(self, table_name, criteria):
        table_name_complete = self.application_name + '_' + table_name
        sql_statement = self._format_insert_statement(table_name_complete, criteria.keys())
        cursor = self._connection.execute(sql_statement, criteria.values())
        return cursor.lastrowid

    def insert_or_ignore(self, table_name, criteria):
        table_name_complete = self.application_name + '_' + table_name
        sql_statement = self._format_insert_statement(table_name_complete, criteria.keys(), 'IGNORE')
        self._connection.execute(sql_statement, criteria.values())

    def insert_many_or_ignore(self, table_name, column_names, values):
        table_name_complete = self.application_name + '_' + table_name
        sql_statement = self._format_insert_statement(table_name_complete, column_names, 'IGNORE')
        self._connection.executemany(sql_statement, values)

    def _format_insert_statement(self, table_name, column_names, on_conflict='ABORT'):
        return 'INSERT OR %s INTO %s (%s) VALUES (%s)' % (
            on_conflict,
            table_name,
            ','.join(column_names),
            ','.join('?' * len(column_names))
        )

    def commit(self):
        self._connection.execute("UPDATE robothub_suite SET application_id = 'JIRA'")
        self._verbose('- Committing changes into database')
        self._connection.commit()

