from connect import session
from model import User
from sqlalchemy.inspection import inspect


def add_user_one(data):

    model_obj = User(**data)
    try:
        session.add(model_obj) 
        session.commit()
        return inspect(model_obj).identity[0]
    except Exception as e:
        session.rollback()
        raise e

def add_user_many(data_li):
    """
    [User(username='cainiao2', password='1234'),]
    """
    try:
        session.add_all(data_li)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def query_user_one(*args,**kwargs):
    
    first_record = session.query(User).filter(*args).filter_by(**kwargs).first()
    return  first_record


def query_user_many(*args,**kwargs):
    all_record = session.query(User).filter(*args).filter_by(**kwargs).with_entities(User.username,User.password,User.creatime,User.id).all()
    return all_record


def query_page(page=1, per_page=3, *args, **kwargs):
    rows = session.query(User).filter(*args).filter_by(**kwargs).with_entities(User.username,User.password,User.creatime,User.id).limit(per_page).offset((int(page) - 1) * per_page)
    return rows

def query_count(*args,**kwargs):
    count = session.query(User).filter(*args).filter_by(**kwargs).count()
    return count

def update_user(data,*args,**kwargs):
    """
    query> User.username=='cainiao'
    data> {User.password:1}
    """
    try:
        rows = session.query(User).filter(*args).filter_by(**kwargs).update(data)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete_user(*args,**kwargs):
    """"
    query>User.username=='cainiao'
    """
    try:
        rows = session.query(User).filter(*args).filter_by(**kwargs)[0]
        session.delete(rows)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e