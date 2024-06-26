from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Boolean

from app.database.database import Base


class Role(Base):
    __tablename__ = 'Roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=True)


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, unique=True)
    user_fullname = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('Roles.id'))


class Organization(Base):
    __tablename__ = 'Organizations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    organization_name = Column(String, unique=True, nullable=False)
    invite_code = Column(String, nullable=False)
    default_slots_amount = Column(Integer, default=4)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)


class User_Organization(Base):
    __tablename__ = 'Users_Organizations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    organization_id = Column(Integer, ForeignKey('Organizations.id'), nullable=False)
    is_current_organization = Column(Boolean, default=False, nullable=False)


class RecordingWeek(Base):
    __tablename__ = 'RecordingWeeks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)


class Recording(Base):
    __tablename__ = 'Recordings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    slots_amount = Column(Integer, nullable=False)
    recording_week_id = Column(Integer, ForeignKey('RecordingWeeks.id'), nullable=False)
    organization_id = Column(Integer, ForeignKey('Organizations.id'), nullable=False)

