from flask import Flask, render_template, request
import os
from scripts.data_inventory import getInventoryDashboard
from scripts.ingest_video_data import uploadVideo
from scripts.search_videos import searchDarkLightVideos
  
# Flask constructor  
app = Flask(__name__)  

@app.get('/') 
def main_page():    
    return render_template('index.html')

@app.route('/video_upload', methods=['GET', 'POST']) 
def videoUpload():
    if request.method == 'GET':
        return render_template('video_upload_page.html')
    
    filepath = request.form.get('filepath')
    description = request.form.get('description')
    uploadVideo(filepath, description)
    
    return render_template('video_upload_page.html', success = "Video successfully analyzed and stored")

@app.route('/search_videos', methods=['GET', 'POST']) 
def searchVideos():
    search_result = []
    if request.method == 'GET':
        return render_template('search_video.html', search_result = search_result)
    
    dark_light_setting = request.form.get('dark_light_setting')
    search_result = searchDarkLightVideos(dark_light_setting)
    print(search_result)
    return render_template('search_video.html', search_result = search_result)



@app.get('/data_inventory') 
def getDataInventry():   
    dashboard = getInventoryDashboard()  
    dashboard.savefig(os.path.join('static', 'images', 'data_inventory_dashboard.png')) 
    return render_template('data_inventory_dashboard.html') 
  
# Main Driver Function  
if __name__ == '__main__': 
    # Run the application on the local development server  
    app.run(debug=True) 