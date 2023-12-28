# Revolut_stock_list
This block of scripts enable the user to exstract the list of available stocks from Revolut App

Updated!

## Get the video with all stocks

In order to get the full list (huge at the time of writing) of revolut stocks, the best way to get it is:

 - install Scrcpy on PC
 - install Automatic Scroll on Android phone
 - launch Scrcpy with this command:
       `scrcpy -r revolut.mkv`
 - one the file has been saved, cut it to the size of the sole stock list
       `ffmpeg -i revolut.mkv -vf "crop=in_w:in_h-700" -c:a copy revolut_cut.mkv`
 - extract all the pictures from the video so we can elaborate images to extract text
       `ffmpeg -i input.mp4 -filter:v fps=fps=1/3.5 ffmpeg_%0d.bmp`
   where 3.5 is the time for which the stock list is changed on the video (1 frame every 3.5 seconds)
 - run the OCR on all images
 - regex on the OCR text
