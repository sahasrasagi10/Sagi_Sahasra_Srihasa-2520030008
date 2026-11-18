from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/",
    serverSelectionTimeoutMS=5000
)

try:
    client.admin.command("ping")
    print("MongoDB connection successful!")

    db = client["llm_monitoring"]
    collection = db["call_logs"]

    print("Database:", db.name)
    print("Collection:", collection.name)

except Exception as e:
    print("Connection failed:", e)

finally:
    client.close()