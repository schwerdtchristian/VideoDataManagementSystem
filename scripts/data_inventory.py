from scripts.data_inventory_help_methods import connectToDB, getTotalNbrOfVideos, getVideoLightSettings, nbrPeopleInVideos, durationOfVideos, getFpsOfVideos, get_dashboard

def getInventoryDashboard():
    cursor = connectToDB('vdms_meta_data.db')

    total_nbr_videos =  getTotalNbrOfVideos(cursor)
    video_light_settings = getVideoLightSettings(cursor, total_nbr_videos)
    nbr_people_in_videos = nbrPeopleInVideos(cursor)
    duration_of_videos = durationOfVideos(cursor)
    fps_of_videos = getFpsOfVideos(cursor)
    
    return get_dashboard(total_nbr_videos,
        video_light_settings,
        nbr_people_in_videos,
        duration_of_videos,
        fps_of_videos)
