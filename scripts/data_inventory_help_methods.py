import sqlite3
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("agg")


def connectToDB(db_name):
    sqliteConnection = sqlite3.connect(db_name)
    return sqliteConnection.cursor()


def getTotalNbrOfVideos(cursor):
    cursor.execute(f"SELECT COUNT(*) FROM video_metadata")
    return cursor.fetchall()[0][0]


def getVideoLightSettings(cursor, total_nbr_videos):
    cursor.execute(
        f"SELECT COUNT(*) FROM video_metadata WHERE dark_setting LIKE 'dark'"
    )
    nbr_videos_dark = cursor.fetchall()[0][0]

    cursor.execute(
        f"SELECT COUNT(*) FROM video_metadata WHERE dark_setting LIKE 'light'"
    )
    nbr_video_light = cursor.fetchall()[0][0]

    nbr_other_video = total_nbr_videos - nbr_videos_dark - nbr_video_light

    return {"dark": nbr_videos_dark, "light": nbr_video_light, "other": nbr_other_video}


def getNbrDarkVideos(cursor):
    cursor.execute(
        f"SELECT COUNT(*) FROM video_metadata WHERE dark_setting LIKE 'dark'"
    )
    return cursor.fetchall()[0][0]


def getNbrLightVideos(cursor):
    cursor.execute(
        f"SELECT COUNT(*) FROM video_metadata WHERE dark_setting LIKE 'light'"
    )
    return cursor.fetchall()[0][0]


def nbrPeopleInVideos(cursor):
    cursor.execute(f"SELECT nbr_people FROM video_metadata")
    nbr_people_in_videos = cursor.fetchall()
    return [nbr_people[0] for nbr_people in nbr_people_in_videos]


def durationOfVideos(cursor):
    cursor.execute(f"SELECT duration FROM video_metadata")
    video_durations = cursor.fetchall()
    return [durations[0] for durations in video_durations]


def getFpsOfVideos(cursor):
    cursor.execute(f"SELECT fps FROM video_metadata")
    fps_of_videos = cursor.fetchall()
    return [fps_of_video[0] for fps_of_video in fps_of_videos]


def plot_data(
    total_nbr_videos,
    video_light_settings,
    nbr_people_in_videos,
    duration_of_videos,
    fps_of_videos,
):
    fig, ax = plt.subplots(2, 2)
    fig.suptitle(f"Total number of videos: {total_nbr_videos}")
    ax[0, 0].bar(
        x=list(video_light_settings.keys()), height=list(video_light_settings.values())
    )
    ax[1, 0].hist(nbr_people_in_videos, bins=range(1, 10, 1))
    ax[0, 1].hist(duration_of_videos, bins=range(0, 10, 1))
    ax[1, 1].hist(fps_of_videos, bins=range(20, 40, 1))

    ax[0, 0].set_title("Distribution of dark and light setting")
    ax[1, 0].set_title("Distribution of number of people in videos")
    ax[0, 1].set_title("Distribution of time duration of videos")
    ax[1, 1].set_title("Distribution of fps of videos")
    plt.show()


def get_dashboard(
    total_nbr_videos,
    video_light_settings,
    nbr_people_in_videos,
    duration_of_videos,
    fps_of_videos,
):
    fig, ax = plt.subplots(2, 2)
    fig.suptitle(f"Total number of videos: {total_nbr_videos}")
    ax[0, 0].bar(
        x=list(video_light_settings.keys()), height=list(video_light_settings.values())
    )
    ax[1, 0].hist(nbr_people_in_videos, bins=range(1, 10, 1))
    ax[0, 1].hist(duration_of_videos, bins=range(0, 10, 1))
    ax[1, 1].hist(fps_of_videos, bins=range(20, 40, 1))

    ax[0, 0].set_title("Distribution of dark and light setting")
    ax[1, 0].set_title("Distribution of number of people in videos")
    ax[0, 1].set_title("Distribution of time duration of videos")
    ax[1, 1].set_title("Distribution of fps of videos")
    plt.subplots_adjust(wspace=0.65, hspace=0.65)
    return plt
