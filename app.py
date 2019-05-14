from flask import Flask, url_for, render_template, redirect,session, request,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Date, Integer, String, Boolean
from flask import request

import os
from xml.etree import ElementTree as ET
import datetime


app = Flask(__name__)

db = SQLAlchemy(app)

# tree = ET.parse('/home/narendra/narendra/xmlflaskpro/country_data.xml')

# file_name = "country_data.xml"
# full_file = os.path.abspath(os.path.join('data', file_name))




# # dom = ElementTree.parse(full_file)
# dom = ET.parse(full_file)
# country = dom.findall('country')
#
# for c in country:
#     name = c.find('name').text
#     rank = c.find('rank').text
#     year = c.find('year').text
#     neighbor = c.find('neighbor').text
#
#     print('* {} [{}] {} {}'. format(
#         name, rank, year, neighbor
#     ))


def parsing(filename):
    tree = ET.parse(filename)
    data = tree.getroot()
    print("Hellooooo",data)

    return data



master_file = "1.XML"
full_filename = os.path.abspath(os.path.join('Master Files', master_file))
# print(full_filename)

# full_filename = os.path.abspath(os.path.join('Group 1', master_file))


Order_file = "Order1.XML"
Order_file = '/home/narendra/narendra/xmlflaskpro/data/Order1.XML'
# print(Order_file)
def parse_xml(Order_file):
    dom = ET.parse(Order_file)
    data = dom.getroot()
    Number = data.find('Number').text
    Name = data.find('Name').text
    # Mode = data.find('Mode').text

    print('{} [{}] '.format(
                Number, Name
    ))
# parse_xml(Order_file)



Master_file = "1.XML"
Master_file = '/home/narendra/narendra/xmlflaskpro/data/1.XML'
print(Master_file)
def parse_xml(Master_file):
    dom = ET.parse(Master_file)
    data = dom.getroot()
    # print(data.tag)  #gives the root of xml
    # print(data.attrib) #gives the attrib of element
    # print(ET.tostring(data, encoding='utf8').decode('utf8'))

    # to fing all element with name
    # for Name in data.iter('Name'):
    #     print(Name.text)

    for Name in data.find("./Records/Record/[Number='3']"):
        print(Name.text)

parse_xml(Master_file)





def get_xml_records(data):
    """Get data of a <Record> tag"""
    records_root = data.find("Records")
    records = records_root.findall("Record")

    return records


# parse_xml(full_file)


class User(db.Model):
    """"""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column('country', String(20), unique=True , index=True)
    rank = Column('rank', String(10), nullable=False)
    year = Column('year', String(50),unique=True , index=True, nullable=False)
    neighbor = Column('neighbor', String(50),unique=True , index=True, nullable=False)
    active = Column(Boolean(), nullable=False, server_default='0')

    def get_id(self):
        return unicode(self.alternative_id)

#----------------------------------------------------------------------


# def __init__(self , country ,rank , year, neighbor ):
#     self.country = country
#     self.rank = rank
#     self.year = year
#     self.neighbor = neighbor
#     self.registered_on = datetime.utcnow()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method =='POST':
        country= request.args.get('name')
        rank=request.args.get('rank')
        year=request.args.get('year')
        neighbor=request.args.get('neighbor')
        user = User(country, rank, year, neighbor)
        db.session.add(user)
        db.session.commit()
        print('User successfully registered')
        return redirect(url_for('login'))
    return render_template("myform.html")


@app.route('/layout')
def layout():
    return render_template("layout.html")

if __name__ == '__main__':
    app.run(debug=True)
