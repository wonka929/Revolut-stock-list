# Revolut_stock_list
This block of scripts enable the user to exstract the list of available stocks from Revolut App

Updated!

## Get the video with all stocks

In order to get the full list (huge at the time of writing) of revolut stocks, the best way to get it is:

 - install Scrcpy on PC
 - install Automatic Scroll on Android phone (https://play.google.com/store/apps/details?id=com.sm.autoscroll&hl=en_US)
 - launch Scrcpy with this command:
   `scrcpy -r revolut.mkv`
 - run the automatic scroll on the stock page in Revolut app so the final revolut.mkv file will have all the stocks recorded
 - onece the file has been saved, cut it to the size of the sole stock list
   `ffmpeg -i revolut.mkv -vf "crop=in_w:in_h-700" -c:a copy revolut_cut.mkv`
 - extract all the pictures from the video so we can elaborate images to extract text
   `ffmpeg -i input.mp4 -filter:v fps=fps=1/2.5 ffmpeg_%0d.bmp`
   where 2.5 is the time for which the stock list is changed on the video (1 frame every 2.5 seconds)
 - run the OCR.py on all images
 - regex.py on the OCR text (list.txt)
 - metadata.py on the list (list_final.csv)
 - final list with Ticker and company name in list_final_with_names.csv
