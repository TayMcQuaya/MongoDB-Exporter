import pymongo
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection using .env variables
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Fetch data
data = list(collection.find({}, {"_id": 0}))  # Exclude _id if not needed

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
excel_file = "mongodb_data.xlsx"
df.to_excel(excel_file, index=False)

print(f"Data successfully exported to {excel_file}")
