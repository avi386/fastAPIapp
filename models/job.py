from sqlalchemy import Column,Integer,String,Enum,ForeignKey
from models.company import Company
from sqlalchemy.orm import Base,engine,SessionLocal,



class Job(Base):
    __tablename__="jobs"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    description = Column(String)
    salary = Column(Integer)
    company_id = Column(Integer,ForeignKey("companies.id"))
    company = relationship("company",back_populates="jobs")