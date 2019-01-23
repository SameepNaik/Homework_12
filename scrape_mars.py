
# coding: utf-8

# In[1]:

def scrape():

# Import
    import pymongo
    from bs4 import BeautifulSoup as bs
    import requests
    from splinter import Browser
    import pandas as pd
    import datetime


# In[2]:


    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.scrape_mars_db

    collection = db.scrape_mars_db


# In[3]:


# URLs to be scraped
    url_nasa = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url_marsweather = 'https://twitter.com/marswxreport?lang=en'
    url_marsfacts = 'https://space-facts.com/mars/'
    url_marshemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'





# In[4]:


# NASA Mars News
# Retrieve the page
    response_nasa = requests.get(url_nasa)

# Create a Beautiful Soup object
    soup_nasa = bs(response_nasa.text, 'html.parser')
    #print(soup_nasa.prettify())


# In[5]:


    news_title = soup_nasa.find(class_="content_title").text
    #print(news_title)

    news_p = soup_nasa.find(class_="rollover_description_inner").text
    #print(news_p)


# In[6]:


# JPL Mars Space Images
# Retrieve the page
    response_jpl = requests.get(url_jpl)

# Create a Beautiful Soup object
    soup_jpl = bs(response_jpl.text, 'html.parser')
    #print(soup_jpl.prettify())


# In[7]:


    featured_image = soup_jpl.find('article', class_="carousel_item").find('a')["data-fancybox-href"]
    featured_image_url = "https://www.jpl.nasa.gov"+featured_image
#print(featured_image_url.find('article'))
#print("____________________________")
#print(featured_image_url)
#print("____________________________")
#print(featured_image_url)

    #print(featured_image)
    #print(featured_image_url)


# In[8]:


# Mars Weather
# Retrieve the page
    response_marsweather = requests.get(url_marsweather)

# Create a Beautiful Soup object
    soup_marsweather = bs(response_marsweather.text, 'html.parser')
    #print(soup_marsweather.prettify())


# In[9]:


    mars_weather = soup_marsweather.find(class_="js-tweet-text-container").text
#print(mars_weather.text[0:95])
    #print(mars_weather)


# In[10]:


# Mars Facts
# Use Pandas to scrape table
    table = pd.read_html(url_marsfacts)
    #table


# In[11]:


# Convert list into dataframe
    mars_facts = table[0]
# Convert data to html string
    mars_facts_html = mars_facts.to_html()
# Remove unwanted new lines
    mars_facts_html.replace('\n','')
    #mars_facts
# Save table directly to a file
    mars_facts.to_html('mars_facts.html')


# The website for this section could not be accesessd.  I've included the code, but commented it out
# so that it wouldn't interfere with the rest of the work.
# Mars Hemispheres
# Retrieve the page
    #response_hemispheres = requests.get(url_marshemispheres)

# Create a Beautiful Soup object
#    soup_hemispheres = bs(response_hemispheres.text, 'html.parser')
#    print(soup_hemispheres.prettify())

    
#    results = soup_hemispheres.find_all(class_="hemisphere_images")
#    for result in results:
#        title = :result.find('a', class_="image_title").text
#        link = result.a["href"]

#        hemisphere_image_urls = [{
#            "title": title, "img_url": link,
#            "title": title, "img_url": link,
#            "title": title, "img_url": link,
#            "title": title, "img_url": link,
#        }]

# In[12]:
    
    records = {"News Title": news_title,
            "News Paragraph": news_p,
            "Featured Image": featured_image_url,
            "Mars Weather": mars_weather,
             }
    collection.insert_one(records)
    return records

print()
print("--------------------------")
test = scrape()
print(test)
print("--------------------------")
print()
#records
# In[13]:


# Mars Hemispheres

