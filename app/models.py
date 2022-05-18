from . import db


class House(db.Model):
    __tablename__='houses'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(2000),unique = True,index = True)
    house = db.Column(db.String(1000))
    time = db.Column(db.String(240))



    def save_house(self):
        db.session.add(self)
        db.session.commit()

    def delete_house(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_posts(cls,id):
        houses = House.query.filter_by(id=id).first()
        return houses

    def __repr__(self):
        return f'House {self.house}'

class Photo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    # name=db.Column(db.String(50),nullable=False)

    def save_photo(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_photos(cls,id):
        photos = Photo.query.filter_by(id=id).first()
        return photos

    def __repr__(self):
        return f'Photo {self.name}'

