from sqlalchemy import create_engine, MetaData

from polls.settings import config
from polls.db import question, choice

DSN = 'postgresql://{user}:{password}@{host}:{port}/{database}'

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])

def sample_data(engine):
    with engine.connect() as conn:
        conn.execute(question.insert(), [
            {
                'question_text': 'What\'s new?',
                'pub_date': '2015-12-15 17:17:49.629+02'
            }
        ])
        conn.execute(choice.insert(), [
            {'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
            {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
            {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
        ])

if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)