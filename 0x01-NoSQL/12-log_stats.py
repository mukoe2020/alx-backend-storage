#!/usr/bin/env python3
"""
    This script contains a function that displays some
    stats about nginx logs stored in mongoDb
"""


from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_doc = nginx_collection.estimated_document_count()
    print("{} logs".format(total_doc))

    list_method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in list_method:
        count = nginx_collection.count_documents(
                {"method": method})
        print(f"\tmethod {method}: {count}")
    query = {"method": "GET", "path": "/status"}
    count_status = nginx_collection.count_documents(query)
    print("{} status check".format(count_status))
