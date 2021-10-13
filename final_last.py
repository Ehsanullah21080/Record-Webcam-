#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 08:23:29 2021

@author: ho2869
"""

from easygui import *
import cv2
import datetime
import time



while True:
    message = "ボタンを押すと20秒間録画します、ワークを回してください"
    title = "ビデオ"
    image = "1.png"
    choices = ["ビデオ録画開始"]
    # print Message box for csv data recording
    reply = buttonbox(message, title, image=image, choices=choices)
    if reply==image:
            
            def save_webcam(outPath,fps,mirror=False):
                # Capturing video from webcam:
                cap = cv2.VideoCapture(0)
                frame_size = (int(cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)),
                              int(cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)))
                print (frame_size)
                
                currentFrame = 0
                
                # Get current width of frame
                width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
                # Get current height of frame
                height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
                
                # Define the codec and create VideoWriter object
                fourcc = cv2.VideoWriter_fourcc(*"XVID")
                out = cv2.VideoWriter(outPath, fourcc, fps, (int(width), int(height)))
                t0 = time.time() # start time in seconds
                while (cap.isOpened()):
                    
                    
                    # Capture frame-by-frame
                    ret, frame = cap.read()
    	                       
                    cv2.imshow('a', frame)
	# check for the key pressed
	           
                #k = cv2.waitKey(125)
                    if ret == True:
                        prev = time.time()
                        TIMER = int(20)
                        while TIMER >= 0:
                        
                            ret, frame = cap.read()
                            font = cv2.FONT_HERSHEY_SIMPLEX
   		                
                            cv2.putText(frame,str(TIMER),(10, 150), font, 3, (-255,255, 100), 8,cv2.LINE_AA)                         
			            
                            cv2.imshow('a', frame)
			            
                            #cv2.waitKey(125)
                            cur = time.time()

             			  
                            if cur-prev >= 1:
                                      prev = cur
                                      TIMER = TIMER-1
				                                    

                            if mirror == True:
                               # Mirror the output video frame
                               frame = cv2.flip(frame, 1)
                               # Saves for video
                               out.write(frame)
                            
                               # Display the resulting frame
                               t1 = time.time() # current time
                               num_seconds = t1 - t0 # diff
                               if num_seconds > 20:  # e.g. break after 30 seconds
                                   break
                         
                            
                            if cv2.waitKey(1) & 0xFF == ord('q'):  # if 'q' is pressed then quit
                               break
                            # To stop duplicate images
                            currentFrame += 1
                   
        
                        # When everything done, release the capture
                        cap.release()
                        out.release()
                        cv2.destroyAllWindows()
                    
            def main():
                now = str(datetime.datetime.now())[:19]
                now = now.replace(":","_")
                #workfilename = "screenshot"
                workfilename = str(now)
            
            
                save_webcam('NG_RECORD/'+workfilename+'output.avi', 30 ,mirror=True)
                        
            if __name__ == '__main__':
               main()
    if reply=="ビデオ録画開始":
                    def save_webcam(outPath,fps,mirror=False):
                        # Capturing video from webcam:
                        cap = cv2.VideoCapture(0)
                        frame_size = (int(cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)),
                                      int(cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)))
                        print (frame_size)
                
                        currentFrame = 0
                
                        # Get current width of frame
                        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
                        # Get current height of frame
                        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
                        
                        # Define the codec and create VideoWriter object
                        fourcc = cv2.VideoWriter_fourcc(*"XVID")
                        out = cv2.VideoWriter(outPath, fourcc, fps, (int(width), int(height)))
                        t0 = time.time() # start time in seconds
                        while (cap.isOpened()):
                            
                            
                            # Capture frame-by-frame
                            ret, frame = cap.read()
        	                       
                            cv2.imshow('a', frame)
	# check for the key pressed
	           
                #k = cv2.waitKey(125)
                            if ret == True:
                                prev = time.time()
                                TIMER = int(20)
                                while TIMER >= 0:
                        
                                    ret, frame = cap.read()
                                    font = cv2.FONT_HERSHEY_SIMPLEX
   		                
                                    cv2.putText(frame,str(TIMER),(10, 150), font, 3, (-255,255, 100), 8,cv2.LINE_AA)                         
			            
                                    cv2.imshow('a', frame)
			            
                            #cv2.waitKey(125)
                                    cur = time.time()

             			  
                                    if cur-prev >= 1:
                                              prev = cur
                                              TIMER = TIMER-1
				                                    

                                    if mirror == True:
                                              # Mirror the output video frame
                                       frame = cv2.flip(frame, 1)
                                       # Saves for video
                                       out.write(frame)
                            
                               # Display the resulting frame
                                       t1 = time.time() # current time
                                       num_seconds = t1 - t0 # diff
                                       if num_seconds > 20:  # e.g. break after 30 seconds
                                          break
                         
                            
                                    if cv2.waitKey(1) & 0xFF == ord('q'):  # if 'q' is pressed then quit
                                       break
                            # To stop duplicate images
                                    currentFrame += 1
                   
        
                        # When everything done, release the capture
                                cap.release()
                                out.release()
                                cv2.destroyAllWindows()
                    
                    def main():
                        now = str(datetime.datetime.now())[:19]
                        now = now.replace(":","_")
                #workfilename = "screenshot"
                        workfilename = str(now)
            
            
                        save_webcam('NG_RECORD/'+workfilename+'output.avi', 30 ,mirror=True)
                        
                    if __name__ == '__main__':
                       main()
