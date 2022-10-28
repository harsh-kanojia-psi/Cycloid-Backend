from extensions import db



class inputModel(db.Model):
    __tablename__ = 'input'

    plot_key = db.Column(db.Integer, primary_key=True)
    radius = db.Column(db.Integer,  nullable=False)
    del_dist = db.Column(db.Integer)


    def __init__(self,radius,del_dist):
        self.radius = radius
        self.del_dist = del_dist


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def plotId(self):
        return  {"Your Plot key is":self.plot_key}

    @classmethod
    def find_by_id(cls, plot_key):
        return cls.query.filter_by(plot_key=plot_key).first()







