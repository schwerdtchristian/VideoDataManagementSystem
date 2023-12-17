import sqlite3

def searchDarkLightVideos(dark_light_setting):

    sqliteConnection = sqlite3.connect('vdms_meta_data.db')
    cursor = sqliteConnection.cursor()

    cursor.execute(f"SELECT filename FROM video_metadata WHERE dark_setting LIKE '{dark_light_setting}'")
    return cursor.fetchall()[0]