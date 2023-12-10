import sqlite3

sqliteConnection = sqlite3.connect('vdms_meta_data.db')
cursor = sqliteConnection.cursor()

print("Do you want to search for videos in dark or light setting? Please write 'dark' or 'light'")
darkOrLightSetting = input()

cursor.execute(f"SELECT filename FROM video_metadata WHERE dark_setting LIKE '{darkOrLightSetting}'")
print(cursor.fetchall())