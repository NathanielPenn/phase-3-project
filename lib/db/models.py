from sqlalchemy import create_engine, func

from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String, Boolean

from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine


engine = create_engine('sqlite:///stardew.db', echo = True)


Base = declarative_base()


class Fish(Base):

    __tablename__ = 'fishes'

    id = Column(Integer(), primary_key=True)

    name = Column(String())

    season = Column(String())

    price = Column(Float())

    location_id = Column(Integer(), ForeignKey('locations.id'))

    bait_id = Column(Integer(), ForeignKey('baits.id'))


    def __repr__(self):

        return f'Fish(id={self.id}, name={self.name}, price={self.price})'


class Location(Base):

    __tablename__ = 'locations'

    id = Column(Integer(), primary_key=True)

    name = Column(String())

    type = Column(String())

    water = Column(String())


    # fishes = relationship("Fish", backref="location")

    def __repr__(self):

        return f'Location(id={self.id}), name={self.name}'



class Bait(Base):

    __tablename__ = 'baits'

    id = Column(Integer(), primary_key=True)

    name = Column(String())

    live = Column(Boolean())

    price = Column(Integer())

    # fishes = relationship("Fish", backref="bait")

    def __repr__(self):

        return f'Bait(id={self.id}), name={self.name}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)