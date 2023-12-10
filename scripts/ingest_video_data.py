import moviepy.editor as moviepy
import uuid
import sqlite3 

sqliteConnection = sqlite3.connect('vdms_meta_data.db')
cursor = sqliteConnection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS video_metadata
                  (filename TEXT, description TEXT, duration REAL)
               """)
sqliteConnection.commit()


print("Please specify the filepath the video you like to store in the VDMS:")
filepath = input()
print("Please describe the video:")
description = input()

clip = moviepy.VideoFileClip(filepath)
duration = clip.duration
filename = str(uuid.uuid4())
clip.write_videofile(f"video_data_catalog/{filename}.mp4")

cursor.execute("INSERT INTO video_metadata (filename, description, duration) VALUES (?, ?, ?)",(filename, description, duration))
sqliteConnection.commit()

cursor.execute("SELECT * FROM video_metadata")
print(cursor.fetchall())

#./raw_data/IMG_0881.MOV
