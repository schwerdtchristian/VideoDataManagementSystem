import moviepy.editor as moviepy
import uuid
import sqlite3 
import os
import scripts.ingest_video_data_help_methods as helper

def uploadVideo(filepath, description):
   # create DB
   sqliteConnection = sqlite3.connect('vdms_meta_data.db')
   cursor = sqliteConnection.cursor()
   cursor.execute("""CREATE TABLE IF NOT EXISTS video_metadata
                     (filename TEXT, description TEXT, duration REAL, dark_setting TEXT, nbr_people INTEGER, fps INTEGER)
                  """)
   sqliteConnection.commit()

   # get manual metadata input
   #print("Please specify the filepath the video you like to store in the VDMS:")
   #filepath = input()
   #print("Please describe the video:")
   #description = input()


   # convert and save file with UUID
   clip = moviepy.VideoFileClip(filepath)
   filename = str(uuid.uuid4())
   if not os.path.exists("./video_data_catalog"):
      os.mkdir("./video_data_catalog")
   clip.write_videofile(f"video_data_catalog/{filename}.mp4")

   # get automatic metadata
   video_dark_setting = helper.darkSetting(filepath)
   nbr_people = helper.nbrPeopleInVideo(filepath)
   duration = clip.duration
   fps = clip.fps


   # save video metadata in DB 
   cursor.execute("INSERT INTO video_metadata (filename, description, duration, dark_setting, nbr_people, fps) VALUES (?, ?, ?, ?, ?, ?)",(filename, description, duration, video_dark_setting, nbr_people, fps))
   sqliteConnection.commit()





   cursor.execute("SELECT * FROM video_metadata")
   print(cursor.fetchall())


   #./raw_data/IMG_0881.MOV
   #./raw_data/IMG_0882.MOV
   #./raw_data/IMG_0888.MOV
   #./raw_data/IMG_0891.MOV
   #./raw_data/IMG_0894.MOV