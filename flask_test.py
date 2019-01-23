import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import test

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017'
mongo = PyMongo(app)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.scrape_mars_db
collection = db.scrape_mars_db

@app.route("/")
def index():
    #records = mongo.db.records.find_one()
    return render_template("index.html")

@app.route("/scrape")
def scraper():
    test_scrape = test.scrape()
    #collection.insert_one(records)
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)


