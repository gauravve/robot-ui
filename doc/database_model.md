Robot Database Schema Description
=================================

Notes:

* Types are SQLite3-combatible datatypes (http://www.sqlite.org/datatype3.html)

* All DATETIMEs are saved in format %Y-%m-%d %H:%M:%S.%f with %f being number of
microseconds (micro: 10e-6) having length of 6 e.g:
2013-04-23 12:35:18.730000


test_run
---------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
source_file | TEXT     |          | absolute path to the original output.xml file
started_at  | DATETIME |          | when was the root suite started at
finished_at | DATETIME |          | when was the root suite finished at
imported_at | DATETIME | X        | when was the output.xml serialized into database
hash        | TEXT     | X        | a SHA1 hash of the source file

Row is unique if the combination of following is unique:
    hash

test_run_status
---------------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
test_run_id | INTEGER  | X        | FOREIGN KEY to test_runs
name        | TEXT     | X        | 'total' or 'critical'
elapsed     | INTEGER  |          | number of milliseconds took to run
failed      | INTEGER  | X        | number of tests failed
passed      | INTEGER  | X        | number of tests passed

Row is unique if the combination of following is unique:
    test_run_id, name


test_run_error
---------------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
test_run_id | INTEGER  | X        | FOREIGN KEY to test_runs
level       | TEXT     | X        | one of the following: TRACE/DEBUG/INFO/WARN/ERROR/FAIL
timestamp   | DATETIME | X        | timestamp of the error
content     | TEXT     | X        | the actual error message

Row is unique if the combination of following is unique:
    test_run_id, level, content


tag_status
---------------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
test_run_id | INTEGER  | X        | FOREIGN KEY to test_runs
name        | TEXT     | X        | name of the tag
critical    | INTEGER  | X        | 0 if not critical, 1 if critical (SQLite has no booleans)
elapsed     | INTEGER  |          | number of milliseconds took to run
failed      | INTEGER  | X        | number of tests failed
passed      | INTEGER  | X        | number of tests passed

Row is unique if the combination of following is unique:
    test_run_id, name


suite
------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
suite_id    | INTEGER  |          | FOREIGN KEY to parent suite if has one
xml_id      | TEXT     | X        | suite id attribute in the xml file, e.g. 's1' or 's1-s1'
name        | TEXT     |          | full name of the suite
source      | TEXT     |          | absolute path to the suite ran
doc         | TEXT     | X        | optional suite documentation, otherwise ''

A row is unique if the combination of following is unique:
    name, source


suite_status
------------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
test_run_id | INTEGER  | X        | FOREIGN KEY to the test_run
suite_id    | INTEGER  | X        | FOREIGN KEY to the suite
elapsed     | INTEGER  | X        | number of milliseconds took to run
failed      | INTEGER  | X        | number of tests failed
passed      | INTEGER  | X        | number of tests passed
status      | TEXT     | X        | either 'PASS' or 'FAIL'

A row is unique if the combination of following is unique:
    test_run_id, suite_id


test
-----

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
suite_id    | INTEGER  | X        | FOREIGN KEY to the suite
xml_id      | TEXT     | X        | test id attribute in the xml file, e.g. 's1-t1' or 's1-s1-t1'
name        | TEXT     | X        | full name of the test
timeout     | TEXT     |          | '' by default
doc         | TEXT     |          | optional test documentation, otherwise ''

A row is unique if the combination of following is unique:
    suite_id, name


test_statu
-----------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
test_run_id | INTEGER  | X        | FOREIGN KEY to the test run
test_id     | INTEGER  | X        | FOREIGN KEY to the test
status      | TEXT     | X        | either 'PASS' or 'FAIL'
elapsed     | INTEGER  | X        | number of milliseconds took to run

A row is unique if the combination of following is unique:
    test_run_id, test_id


keyword
--------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
suite_id    | INTEGER  |          | FOREIGN KEY to the suite if is suite keyword
test_id     | INTEGER  |          | FOREIGN KEY to the test if is test keyword
keyword_id  | INTEGER  |          | FOREIGN KEY to the parent keyword if is sub-keyword
name        | TEXT     | X        | full name of the keyword
type        | TEXT     | X        | usually '', either 'setup' or 'teardown' for suite keywords
timeout     | TEXT     |          | '' by default
doc         | TEXT     |          | optional keyword documentation, otherwise ''

A row is unique if the combination of following is unique:
    name, type


keyword_status
--------------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
test_run_id | INTEGER  | X        | FOREIGN KEY to the test run
keyword_id  | INTEGER  | X        | FOREIGN KEY to the keyword
status      | TEXT     | X        | either 'PASS' or 'FAIL'
elapsed     | INTEGER  | X        | number of milliseconds keyword took to run

A row is unique has no unique constraints.

message
--------------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
keyword_id  | INTEGER  | X        | FOREIGN KEY to the keyword
level       | TEXT     | X        | one of the following: TRACE/DEBUG/INFO/WARN/ERROR/FAIL
timestamp   | DATETIME | X        | timestamp of the message
content     | TEXT     | X        | textual content of the message

A row is unique if the combination of following is unique:
    keyword_id, level, content


tag
----

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
test_id     | INTEGER  | X        | FOREIGN KEY to the test
content     | TEXT     | X        | name of the tag

A row is unique if the combination of following is unique:
    test_id, content


argument
---------

column      | type     | not null | description
------------|----------|----------|------------
id          | INTEGER  | X        | primary key
keyword_id  | INTEGER  | X        | FOREIGN KEY to the keyword
content     | TEXT     | X        | textual content

A row is unique if the combination of following is unique:
    keyword_id, content

project
---------

column        | type     | not null | description
--------------|----------|----------|------------
id            | TEXT     | X        | primary key. TEXT primary key to have human friendly ids.
project_name  | TEXT     | X        | Descriptive name of the application.


application
-----------

column            | type     | not null | description
------------------|----------|----------|------------
id                | TEXT     | X        | primary key. TEXT primary key to have human friendly ids.
application_name  | INTEGER  | X        | Descriptive name of the application. 
project_id        | TEXT     | X        | FOREIGN KEY to the project
git_link          | TEXT     | X        | textual content
framework_name    | TEXT     | X        | textual content
jira_link         | TEXT     | X        | textual content

