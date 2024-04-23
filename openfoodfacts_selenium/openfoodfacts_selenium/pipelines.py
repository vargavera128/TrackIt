# pipelines.py

import psycopg2

class PostgreSQLPipeline:
    def __init__(self, db_settings):
        self.db_settings = db_settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_settings={
                'host': crawler.settings.get('PG_HOST'),
                'port': crawler.settings.get('PG_PORT'),
                'database': crawler.settings.get('PG_DATABASE'),
                'user': crawler.settings.get('PG_USER'),
                'password': crawler.settings.get('PG_PASSWORD'),
            }
        )

    def open_spider(self, spider):
        self.conn = psycopg2.connect(**self.db_settings)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        print(item)
        self.cur.execute("""
            INSERT INTO tracks (item_name, image_url) VALUES (%s, %s)
        """, (item['item_name'], item['image_url']))
        return item
