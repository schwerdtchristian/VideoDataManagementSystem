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

cursor.execute(f"SELECT COUNT(*) FROM video_metadata WHERE nbr_people = 0")
nbr_people_0 = cursor.fetchall()[0][0]

cursor.execute(f"SELECT COUNT(*) FROM video_metadata WHERE nbr_people = 1")
nbr_people_1 = cursor.fetchall()[0][0]

cursor.execute(f"SELECT COUNT(*) FROM video_metadata WHERE nbr_people = 2")
nbr_people_2 = cursor.fetchall()[0][0]

nbr_people_data = {'0': nbr_people_0, '1': nbr_people_1, '2': nbr_people_2}

cursor.execute(f"SELECT duration FROM video_metadata")
video_durations = cursor.fetchall()
video_durations = [durations[0] for durations in video_durations]


fig, ax = plt.subplots(3,1)

fig.suptitle(f"Total number of videos: {total_nbr_videos}")
ax[0].bar(x=list(light_setting_data.keys()), height=list(light_setting_data.values()))
ax[1].bar(x=list(nbr_people_data.keys()), height=list(nbr_people_data.values()))
ax[2].hist(video_durations, bins = range(0, 10, 1))
ax[0].set_title("Distribution of dark and light setting")
ax[1].set_title("Distribution of number of people in videos")
ax[2].set_title("Distribution of time duration of videos")
plt.show()