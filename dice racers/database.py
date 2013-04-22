from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(\
    'sqlite:////home/zapperken/flaskapp/hotel2/hotel2/lantern.db',
    convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata. Otherwise
    # you will have to import them first before calling init_db()
    import hotel2.models
    try:
        Base.metadata.drop_all(bind=engine)
    except:
        # catch drop all error on empty db
        pass
    finally:
        Base.metadata.create_all(bind=engine)
