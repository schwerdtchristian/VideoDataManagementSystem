import sqlite3
import matplotlib.pyplot as plt

# Connect to DB
sqliteConnection = sqlite3.connect('vdms_meta_data.db')
cursor = sqliteConnection.cursor()

cursor.execute(f"SELECT COUNT(*) FROM video_metadata")
total_nbr_videos = cursor.fetchall()[0][0]


cursor.execute(f"SELECT COUNT(*) FROM video_metadata WHERE dark_setting LIKE 'dark'")
nbr_dark_videos = cursor.fetchall()[0][0]

cursor.execute(f"SELECT COUNT(*) FROM video_metadata WHERE dark_setting LIKE 'light'")
nbr_light_video = cursor.fetchall()[0][0]

light_setting_data = {'dark': nbr_dark_videos, 'light': nbr_light_video, 'other': total_nbr_videos-nbr_dark_videos-nbr_light_video}

fig, ax = plt.subplots(1,1)

fig.suptitle(f"Total number of videos: {total_nbr_videos}")
ax[0].bar(x=list(light_setting_data.keys()), height=list(light_setting_data.values()))
plt.show()