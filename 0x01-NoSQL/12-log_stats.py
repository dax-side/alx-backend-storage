#!/usr/bin/env python3
"""  provides stats about nginx"""

if __name__ == "__main__":
    from pymongo import MongoClient

    def log_stats():
        """provides stats about Nginx logs stored in MongoDB"""
        # Connect databse
        client = MongoClient()
        db = client["logs"]
        col = db["nginx"]

        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

        # Print output given in example
        print(col.count_documents({}), "logs")

        print("Methods:")
        for method in methods:
            logs = col.count_documents({"method": method})
            print("\tmethod {}: {}".format(method, logs))

        print(col.count_documents(
            {"method": "GET", "path": "/status"}), "status check")


# call main function
    log_stats()
