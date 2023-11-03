# https://alecaddd.com/davinci-resolve-ffmpeg-cheatsheet-for-linux/

mkdir transcoded;
for i in *.mp4;
do ffmpeg -i "$i" -vcodec dnxhd -acodec pcm_s16le -s 1920x1080 -r 30000/1001 -b:v 36M -pix_fmt yuv422p -f mov "transcoded/${i%.*}.mov";
# do ffmpeg -i "$i" -vcodec mjpeg -q:v 2 -acodec pcm_s16be -q:a 0 -f mov "transcoded/${i%.*}.mov";
done
