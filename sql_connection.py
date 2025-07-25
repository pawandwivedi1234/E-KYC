# import mysql
# import pandas as pd
# import logging
# import os 
# import toml

# # Logging configuration
# logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
# log_dir = "logs"
# os.makedirs(log_dir, exist_ok=True)
# logging.basicConfig(filename=os.path.join(log_dir, "ekyc_logs.log"), level=logging.INFO, format=logging_str, filemode="a")

# # Load database configuration from config.toml
# config = toml.load("config.toml")
# db_config = config.get("database", {})

# db_user = db_config.get("user")
# db_password = db_config.get("password")
# db_host = db_config.get("host", "localhost")
# db_name = db_config.get("database")

# if not db_user or not db_password:
#     logging.error("Database user or password not found in config.toml")
#     raise ValueError("Database user or password not found in config.toml")

# # Establish a connection to the MySQL server
# try:
#     mydb = mysql.connector.connect(
#         host=db_host,
#         user=db_user,
#         password=db_password,
#         database=db_name
#     )
#     mycursor = mydb.cursor()
#     logging.info("Connection established with database")
# except mysql.connector.Error as err:
#     logging.error(f"Error connecting to the database: {err}")
#     raise



# def insert_records(text_info):
#     try:
#         sql = "INSERT INTO users(id, name, father_name, dob, id_type, embedding) VALUES (%s, %s, %s, %s, %s, %s)"
#         values = (text_info['ID'],
#                   text_info['Name'],
#                   text_info["Father's Name"],
#                   text_info['DOB'],  # Make sure this is formatted as a string 'YYYY-MM-DD'
#                   text_info['ID Type'],
#                   str(text_info['Embedding']))
        
#         mycursor.execute(sql, values)
#         mydb.commit()
#         logging.info("Inserted records successfully into users table.")
#     except Exception as e:
#         logging.error(f"Error inserting records into users table: {e}")

# def insert_records_aadhar(text_info):
#     try:
#         sql = "INSERT INTO aadhar(id, name, gender, dob, id_type, embedding) VALUES (%s, %s, %s, %s, %s, %s)"
#         values = (text_info['ID'],
#                   text_info['Name'],
#                   text_info["Gender"],
#                   text_info['DOB'],  # Make sure this is formatted as a string 'YYYY-MM-DD'
#                   text_info['ID Type'],
#                   str(text_info['Embedding']))
        
#         mycursor.execute(sql, values)
#         mydb.commit()
#         logging.info("Inserted records successfully into aadhar table.")
#     except Exception as e:
#         logging.error(f"Error inserting records into aadhar table: {e}")

# def fetch_records(text_info):
#     try:
#         sql = "SELECT * FROM users WHERE id = %s"
#         values = (text_info['ID'],)
#         mycursor.execute(sql, values)
#         result = mycursor.fetchall()
#         if result:
#             df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
#             logging.info("Fetched records successfully from users table.")
#             return df
#         else:
#             logging.info("No records found.")
#             return pd.DataFrame()
#     except Exception as e:
#         logging.error(f"Error fetching records: {e}")
#         return pd.DataFrame()
    
# def fetch_records_aadhar(text_info):
#     try:
#         sql = "SELECT * FROM aadhar WHERE id = %s"
#         values = (text_info['ID'],)
#         mycursor.execute(sql, values)
#         result = mycursor.fetchall()
#         if result:
#             df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
#             logging.info("Fetched records successfully from aadhar table.")
#             return df
#         else:
#             logging.info("No records found.")
#             return pd.DataFrame()
#     except Exception as e:
#         logging.error(f"Error fetching records: {e}")
#         return pd.DataFrame()

# def check_duplicacy(text_info):
#     try:
#         df = fetch_records(text_info)
#         if df.shape[0] > 0:
#             logging.info("Duplicate records found.")
#             return True
#         else:
#             logging.info("No duplicate records found.")
#             return False
#     except Exception as e:
#         logging.error(f"Error checking duplicacy: {e}")
#         return False
    
# def check_duplicacy_aadhar(text_info):
#     try:
#         df = fetch_records_aadhar(text_info)
#         if df.shape[0] > 0:
#             logging.info("Duplicate records found.")
#             return True
#         else:
#             logging.info("No duplicate records found.")
#             return False
#     except Exception as e:
#         logging.error(f"Error checking duplicacy: {e}")
#         return False

# # import pymysql
# # import pandas as pd
# # import logging
# # import os 
# # import toml

# # # Logging configuration
# # logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
# # log_dir = "logs"
# # os.makedirs(log_dir, exist_ok=True)
# # logging.basicConfig(
# #     filename=os.path.join(log_dir, "ekyc_logs.log"),
# #     level=logging.INFO,
# #     format=logging_str,
# #     filemode="a"
# # )

# # # Load database configuration from config.toml
# # config = toml.load("config.toml")
# # db_config = config.get("database", {})

# # db_user = db_config.get("user")
# # db_password = db_config.get("password")
# # db_host = db_config.get("host", "localhost")
# # db_name = db_config.get("database")

# # if not db_user or not db_password:
# #     logging.error("Database user or password not found in config.toml")
# #     raise ValueError("Database user or password not found in config.toml")

# # # Establish a connection to the MySQL server using PyMySQL
# # try:
# #     mydb = pymysql.connect(
# #         host=db_host,
# #         user=db_user,
# #         password=db_password,
# #         database=db_name,
# #         cursorclass=pymysql.cursors.Cursor
# #     )
# #     mycursor = mydb.cursor()
# #     logging.info("Connection established with database using PyMySQL.")
# # except pymysql.MySQLError as err:
# #     logging.error(f"Error connecting to the database: {err}")
# #     raise

# # # --------- FUNCTIONS ------------

# # def insert_records(text_info):
# #     try:
# #         sql = "INSERT INTO users(id, name, father_name, dob, id_type, embedding) VALUES (%s, %s, %s, %s, %s, %s)"
# #         values = (
# #             text_info['ID'],
# #             text_info['Name'],
# #             text_info["Father's Name"],
# #             text_info['DOB'],
# #             text_info['ID Type'],
# #             str(text_info['Embedding'])
# #         )
# #         mycursor.execute(sql, values)
# #         mydb.commit()
# #         logging.info("Inserted records successfully into users table.")
# #     except Exception as e:
# #         logging.error(f"Error inserting records into users table: {e}")


# # def insert_records_aadhar(text_info):
# #     try:
# #         sql = "INSERT INTO aadhar(id, name, gender, dob, id_type, embedding) VALUES (%s, %s, %s, %s, %s, %s)"
# #         values = (
# #             text_info['ID'],
# #             text_info['Name'],
# #             text_info["Gender"],
# #             text_info['DOB'],
# #             text_info['ID Type'],
# #             str(text_info['Embedding'])
# #         )
# #         mycursor.execute(sql, values)
# #         mydb.commit()
# #         logging.info("Inserted records successfully into aadhar table.")
# #     except Exception as e:
# #         logging.error(f"Error inserting records into aadhar table: {e}")


# # def fetch_records(text_info):
# #     try:
# #         sql = "SELECT * FROM users WHERE id = %s"
# #         values = (text_info['ID'],)
# #         mycursor.execute(sql, values)
# #         result = mycursor.fetchall()
# #         if result:
# #             df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
# #             logging.info("Fetched records successfully from users table.")
# #             return df
# #         else:
# #             logging.info("No records found.")
# #             return pd.DataFrame()
# #     except Exception as e:
# #         logging.error(f"Error fetching records: {e}")
# #         return pd.DataFrame()


# # def fetch_records_aadhar(text_info):
# #     try:
# #         sql = "SELECT * FROM aadhar WHERE id = %s"
# #         values = (text_info['ID'],)
# #         mycursor.execute(sql, values)
# #         result = mycursor.fetchall()
# #         if result:
# #             df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
# #             logging.info("Fetched records successfully from aadhar table.")
# #             return df
# #         else:
# #             logging.info("No records found.")
# #             return pd.DataFrame()
# #     except Exception as e:
# #         logging.error(f"Error fetching records from aadhar: {e}")
# #         return pd.DataFrame()


# # def check_duplicacy(text_info):
# #     try:
# #         df = fetch_records(text_info)
# #         if df.shape[0] > 0:
# #             logging.info("Duplicate records found.")
# #             return True
# #         else:
# #             logging.info("No duplicate records found.")
# #             return False
# #     except Exception as e:
# #         logging.error(f"Error checking duplicacy: {e}")
# #         return False


# # def check_duplicacy_aadhar(text_info):
# #     try:
# #         df = fetch_records_aadhar(text_info)
# #         if df.shape[0] > 0:
# #             logging.info("Duplicate records found.")
# #             return True
# #         else:
# #             logging.info("No duplicate records found.")
# #             return False
# #     except Exception as e:
# #         logging.error(f"Error checking duplicacy for aadhar: {e}")
# #         return False
# import pymysql
# import pandas as pd
# import logging
# import os
# import toml

# # Logging configuration
# logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
# log_dir = "logs"
# os.makedirs(log_dir, exist_ok=True)
# logging.basicConfig(filename=os.path.join(log_dir, "ekyc_logs.log"), level=logging.INFO, format=logging_str, filemode="a")

# # Load database configuration from config.toml
# config = toml.load("config.toml")
# db_config = config.get("database", {})

# db_user = db_config.get("user")
# db_password = db_config.get("password")
# db_host = db_config.get("host", "localhost")
# db_name = db_config.get("database")

# if not db_user or not db_password:
#     logging.error("Database user or password not found in config.toml")
#     raise ValueError("Database user or password not found in config.toml")

# # Establish a connection to the MySQL server
# try:
#     mydb = pymysql.connect(
#         host=db_host,
#         user=db_user,
#         password=db_password,
#         database=db_name
#     )
#     mycursor = mydb.cursor()
#     logging.info("Connection established with database")
# except pymysql.MySQLError as err:
#     logging.error(f"Error connecting to the database: {err}")
#     raise

# # Function to insert into `users` table
# def insert_records(text_info):
#     try:
#         sql = "INSERT INTO users(id, name, father_name, dob, id_type, embedding) VALUES (%s, %s, %s, %s, %s, %s)"
#         values = (
#             text_info['ID'],
#             text_info['Name'],
#             text_info["Father's Name"],
#             text_info['DOB'],
#             text_info['ID Type'],
#             str(text_info['Embedding'])
#         )
#         mycursor.execute(sql, values)
#         mydb.commit()
#         logging.info("Inserted records successfully into users table.")
#     except Exception as e:
#         logging.error(f"Error inserting records into users table: {e}")

# # Function to insert into `aadhar` table
# def insert_records_aadhar(text_info):
#     try:
#         sql = "INSERT INTO aadhar(id, name, gender, dob, id_type, embedding) VALUES (%s, %s, %s, %s, %s, %s)"
#         values = (
#             text_info['ID'],
#             text_info['Name'],
#             text_info['Gender'],
#             text_info['DOB'],
#             text_info['ID Type'],
#             str(text_info['Embedding'])
#         )
#         mycursor.execute(sql, values)
#         mydb.commit()
#         logging.info("Inserted records successfully into aadhar table.")
#     except Exception as e:
#         logging.error(f"Error inserting records into aadhar table: {e}")

# # Fetch from `users`
# def fetch_records(text_info):
#     try:
#         sql = "SELECT * FROM users WHERE id = %s"
#         values = (text_info['ID'],)
#         mycursor.execute(sql, values)
#         result = mycursor.fetchall()
#         if result:
#             df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
#             logging.info("Fetched records successfully from users table.")
#             return df
#         else:
#             logging.info("No records found.")
#             return pd.DataFrame()
#     except Exception as e:
#         logging.error(f"Error fetching records: {e}")
#         return pd.DataFrame()

# # Fetch from `aadhar`
# def fetch_records_aadhar(text_info):
#     try:
#         sql = "SELECT * FROM aadhar WHERE id = %s"
#         values = (text_info['ID'],)
#         mycursor.execute(sql, values)
#         result = mycursor.fetchall()
#         if result:
#             df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
#             logging.info("Fetched records successfully from aadhar table.")
#             return df
#         else:
#             logging.info("No records found.")
#             return pd.DataFrame()
#     except Exception as e:
#         logging.error(f"Error fetching records: {e}")
#         return pd.DataFrame()

# # Check duplicacy in `users`
# def check_duplicacy(text_info):
#     try:
#         df = fetch_records(text_info)
#         if not df.empty:
#             logging.info("Duplicate records found.")
#             return True
#         else:
#             logging.info("No duplicate records found.")
#             return False
#     except Exception as e:
#         logging.error(f"Error checking duplicacy: {e}")
#         return False

# # Check duplicacy in `aadhar`
# def check_duplicacy_aadhar(text_info):
#     try:
#         df = fetch_records_aadhar(text_info)
#         if not df.empty:
#             logging.info("Duplicate records found.")
#             return True
#         else:
#             logging.info("No duplicate records found.")
#             return False
#     except Exception as e:
#         logging.error(f"Error checking duplicacy: {e}")
#         return False
import os
import logging
import toml
import pymysql
import pandas as pd

# ─── Logging Configuration ────────────────────────────────────────────────────
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "ekyc_logs.log"),
    level=logging.INFO,
    format=logging_str,
    filemode="a"
)

# ─── Load Database Config ─────────────────────────────────────────────────────
try:
    config = toml.load("config.toml")
    db_cfg = config.get("database", {})
    DB_USER = db_cfg["user"]
    DB_PASSWORD = db_cfg["password"]
    DB_HOST = db_cfg.get("host", "localhost")
    DB_NAME = db_cfg["database"]
except Exception as e:
    logging.error(f"Failed to load database config: {e}")
    raise

# ─── Establish Connection ─────────────────────────────────────────────────────
try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.Cursor
    )
    cursor = connection.cursor()
    logging.info("Connected to MySQL database successfully.")
except Exception as e:
    logging.error(f"Error connecting to database: {e}")
    raise

# ─── INSERT FUNCTIONS ─────────────────────────────────────────────────────────
def insert_records(text_info: dict):
    """
    Insert a new PAN user record into the `users` table.
    """
    try:
        sql = """
            INSERT INTO users
              (id, name, father_name, dob, id_type, embedding)
            VALUES
              (%s, %s, %s, %s, %s, %s)
        """
        params = (
            text_info["ID"],
            text_info["Name"],
            text_info["Father's Name"],
            text_info["DOB"],       # formatted 'YYYY-MM-DD'
            text_info["ID Type"],
            str(text_info["Embedding"])
        )
        cursor.execute(sql, params)
        connection.commit()
        logging.info(f"Inserted user {text_info['ID']} into `users`.")
    except Exception as e:
        logging.error(f"insert_records error: {e}")

def insert_records_aadhar(text_info: dict):
    """
    Insert a new Aadhar user record into the `aadhar` table.
    """
    try:
        sql = """
            INSERT INTO aadhar
              (id, name, gender, dob, id_type, embedding)
            VALUES
              (%s, %s, %s, %s, %s, %s)
        """
        params = (
            text_info["ID"],
            text_info["Name"],
            text_info["Gender"],
            text_info["DOB"],       # formatted 'YYYY-MM-DD'
            text_info["ID Type"],
            str(text_info["Embedding"])
        )
        cursor.execute(sql, params)
        connection.commit()
        logging.info(f"Inserted user {text_info['ID']} into `aadhar`.")
    except Exception as e:
        logging.error(f"insert_records_aadhar error: {e}")

# ─── FETCH FUNCTIONS ──────────────────────────────────────────────────────────
def fetch_records(text_info: dict) -> pd.DataFrame:
    """
    Fetch PAN user records by hashed ID. Returns a DataFrame.
    """
    try:
        sql = "SELECT * FROM users WHERE id = %s"
        cursor.execute(sql, (text_info["ID"],))
        rows = cursor.fetchall()
        if rows:
            cols = [col[0] for col in cursor.description]
            df = pd.DataFrame(rows, columns=cols)
            logging.info(f"Fetched {len(df)} record(s) from `users`.")
            return df
        else:
            logging.info("No records found in `users`.")
            return pd.DataFrame()
    except Exception as e:
        logging.error(f"fetch_records error: {e}")
        return pd.DataFrame()

def fetch_records_aadhar(text_info: dict) -> pd.DataFrame:
    """
    Fetch Aadhar user records by hashed ID. Returns a DataFrame.
    """
    try:
        sql = "SELECT * FROM aadhar WHERE id = %s"
        cursor.execute(sql, (text_info["ID"],))
        rows = cursor.fetchall()
        if rows:
            cols = [col[0] for col in cursor.description]
            df = pd.DataFrame(rows, columns=cols)
            logging.info(f"Fetched {len(df)} record(s) from `aadhar`.")
            return df
        else:
            logging.info("No records found in `aadhar`.")
            return pd.DataFrame()
    except Exception as e:
        logging.error(f"fetch_records_aadhar error: {e}")
        return pd.DataFrame()

# ─── DUPLICACY CHECKS ─────────────────────────────────────────────────────────
def check_duplicacy(text_info: dict) -> bool:
    """
    Returns True if a PAN user record exists, else False.
    """
    try:
        df = fetch_records(text_info)
        exists = not df.empty
        logging.info(f"check_duplicacy (users): {exists}")
        return exists
    except Exception as e:
        logging.error(f"check_duplicacy error: {e}")
        return False

def check_duplicacy_aadhar(text_info: dict) -> bool:
    """
    Returns True if an Aadhar user record exists, else False.
    """
    try:
        df = fetch_records_aadhar(text_info)
        exists = not df.empty
        logging.info(f"check_duplicacy_aadhar: {exists}")
        return exists
    except Exception as e:
        logging.error(f"check_duplicacy_aadhar error: {e}")
        return False

# ──────────────────────────────────────────────────────────────────────────────
