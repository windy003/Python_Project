from moviepy.video.io.VideoFileClip import VideoFileClip

import os

# 获取当前目录路径
current_directory = os.getcwd()

# 初始化mp4文件列表
video_files = []

# 遍历当前目录中的所有文件和文件夹
for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
         # 如果文件是mp4文件，将其文件名添加到列表中
        if os.path.isfile(file_path) and file_name.endswith('.mp4'):
                video_files.append(file_name)

# 打印mp4文件列表
print(video_files)
                            

# 初始化时长总和为0
total_duration = 0

# 遍历视频文件列表，获取每个视频文件的时长并累加到时长总和中
for video_file in video_files:
    clip = VideoFileClip(video_file)
    duration = clip.duration
    total_duration += duration
    clip.close()

# 打印时长总和
print(f'视频文件的时长总和为：{total_duration} 秒,{total_duration/60}分钟,{total_duration/3600}小时,')
