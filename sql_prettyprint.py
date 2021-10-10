import sqlparse
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlalchemy import create_engine
from sqlalchemy.orm import Query


engine = create_engine("sqlite+pysqlite:///db.sqlite", echo=True, future=True)


def format_sql(query: Query):
    compiled_statement = query.statement.compile(engine, compile_kwargs={"literal_binds": True})
    parsed_query = sqlparse.format(str(compiled_statement), reindent=True, keyword_case='upper')
    print(highlight(parsed_query, SqlLexer(), TerminalFormatter()))


# or option without sqlparse
def format_sql_2(query: Query):
    compiled_statement = query.statement.compile(engine, compile_kwargs={"literal_binds": True})
    print(highlight(str(compiled_statement), SqlLexer(), TerminalFormatter()))
