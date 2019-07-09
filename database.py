from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///images.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_image(filename,title):
    new_image = Image(filename=filename,title=title)
    session.add(new_image)
    session.commit()

def get_image(id):
     image = session.query(Image).filter_by(id=id).first()
     return image

def get_all_images():
    images = session.query(Image).all()
    return images


#create_swatch("cat1.jpg","cat1.jpg","cotton")

#print([swatch.material for swatch in get_all_swatches()])
