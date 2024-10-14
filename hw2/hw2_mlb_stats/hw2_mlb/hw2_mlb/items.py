# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Hw2MlbItem(scrapy.Item):
    # define the fields for your item here like:
    AB = scrapy.Field() #At Bats
    AVG = scrapy.Field() #Batting Avg
    BB = scrapy.Field() #Walks
    G = scrapy.Field() #games played
    H = scrapy.Field()
    HR = scrapy.Field()
    OBP = scrapy.Field()
    PLAYER = scrapy.Field()
    R = scrapy.Field()
    RBI = scrapy.Field()
    SB = scrapy.Field()
    SLG = scrapy.Field()
    SO = scrapy.Field()
    TEAM = scrapy.Field()

