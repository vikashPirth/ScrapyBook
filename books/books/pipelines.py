import pymongo 
from itemadapter import ItemAdapter 


class MongoPipeline:

    COLLECTION_NAME = "BOOKS"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.get("MONGO_URI"),
            mongo_dn = crawler.get("MONGO_DATABASE")
        )
    

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]


    def close_spider(self, spider):
        self.client.close()

    
    def process_item(self, item, spider):
        self.db[self.COLLECTION_NAME].insert_one(ItemAdapter(item).asdict())
        return item