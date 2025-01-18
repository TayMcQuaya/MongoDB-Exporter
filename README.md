# MongoDB to Excel Exporter

A simple Python script to export MongoDB collections to an Excel file (`.xlsx`).  
It securely loads MongoDB connection details from a `.env` file.

## 📌 Features
✅ Exports MongoDB data into an Excel file  
✅ Uses `.env` for secure configuration  
✅ Lightweight and easy to use  

## 🚀 Installation

### 1️⃣ Clone this repository
```bash
git clone https://github.com/your-username/mongodb-to-excel.git
cd mongodb-to-excel
```

### 2️⃣ Install dependencies
```bash
pip install pymongo pandas openpyxl python-dotenv
```

### 3️⃣ Set up `.env` file
Create a `.env` file in the root directory and add your MongoDB credentials:
```
MONGO_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net
MONGO_DB=your_database_name
MONGO_COLLECTION=your_collection_name
```

### 4️⃣ Run the script
```bash
python export_mongo.py
```
This will generate an `mongodb_data.xlsx` file in the project directory.

## 🛠 Dependencies
- `pymongo` – Connects to MongoDB
- `pandas` – Handles data processing
- `openpyxl` – Writes data to Excel
- `python-dotenv` – Loads environment variables

## ⚡ Example Output
The script will export MongoDB data into an Excel file like this:

| Name  | Age | Email              |
|-------|----|------------------|
| Alice | 25 | alice@email.com |
| Bob   | 30 | bob@email.com   |

## 📜 License
MIT License - Feel free to use and modify!

**Happy coding! 🚀**


