from data_base import sqlite_db

from parser_docx import parser

sqlite_db.sql_start()
sqlite_db.create_bd()
parser.pars_docx()