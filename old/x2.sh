# DOUBLE VIDEO SPEED WHILE PITCH SCALING AUDIO TO REMAIN SAME PITCH AS ORIGINAL PLAYBACK
# ffmpeg -i input_video -filter_complex "[0:v]setpts=<1/x>*PTS[v];[0:a]atempo=<x>[a]" -map "[v]" -map "[a]" output_video
NAME=$1
NEW_NAME=$NAME"_X2"
# echo $NEW_NAME
ffmpeg -i $NAME -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" $NEW_NAME
