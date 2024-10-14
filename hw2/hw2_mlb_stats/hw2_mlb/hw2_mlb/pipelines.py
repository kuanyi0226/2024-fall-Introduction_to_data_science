# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from bs4 import BeautifulSoup
from itemadapter import ItemAdapter


class Hw2MlbPipeline:
    def process_item(self, item, spider):
        item['PLAYER'] = self.process_player(item['PLAYER'])
        return item
    
    #special case: 
    #.000,4,74J.T.J RealmutoRealmutoC74‌‌‌,PHI
    #.625,2,1MichaelM Harris IIHarrisCF1‌‌‌,ATL
    def process_player(self, player_name):
        # remove any hidden HTML tags
        #return player_name
        soup = BeautifulSoup(player_name, 'html.parser')
        text = soup.get_text()
        text = text.strip() #remove spaces

        first_upper_index = 0 ## find the upper index of first name 
        space_index = 0 # find the index of space between the first and last name
        last_upper_index = 0
        last_lower_index = 0
        #find the values above
        for i, char in enumerate(text):
            if char == ' ' and space_index == 0:
                space_index = i
                continue
            if char.isupper():
                if(first_upper_index == 0):
                    first_upper_index = i
                elif (first_upper_index !=0 and last_upper_index ==0 and space_index != 0):
                    last_upper_index = i
            elif char.islower():
                if i != len(text) and last_upper_index != 0 and (text[i+1].isupper() or text[i+1] == ' '):
                    last_lower_index = i
                    break

        fullName = text[first_upper_index:space_index-1] + ' ' + text[last_upper_index:last_lower_index+1]
        
        return fullName
