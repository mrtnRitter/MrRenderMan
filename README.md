# MrRenderMan
Multithread render manager for After Effects.

<img src="/Screens/Start.jpg" width="32%" /> <img src="/Screens/Settings.jpg" width="32%" /> <img src="/Screens/Workers.jpg" width="32%" />

### Motivation
When starting working professionally with After Effects in 2014, it doesn't fully utilize our computer hardware. Long rendering times with an idling CPU haven't been acceptable for serious business work (although it gets better, this is still an issue with After Effects in 2021).  
All professional solutions have been to expensive for a growing business, but playing around with the After Effects command line renderder soon reveals it's potential.  
I started digging deeper into Python with the aim to get a render manager done. The basic idea was to have the manager and the render-worker all in one script for easy use. The script will launch itself but with a different behaviour.  

This tool have been used and developed for over 4 years until we switched to a more network orientated solution. 

### Usage
1. Add After Effects composition in render queue, select an image sequence as output module and a valid path
2. For network rendering, make sure to select existing file skipping in render settings and select a path which is reachable for all nodes
3. Safe the project and close After Effects (we need all the RAM, so better close every programm which isn't needed)
4. Launch MrRenderMan using Python
5. Select project file, select "shutdown after rendering" options and how many workers should be launched
6. MrRenderMan will launch a new worker every 30 seconds (launching all at a time will lead to crashes)
7. If a worker crashes, it gets relaunched
8. When rendering is done, the next project file and all render settings can be selected

### Compatibility 
MrRenderMan was written against the German version of After Effects. This is only importent for the auto-restart after a crash, where the script analysis the subprocess output of aerender.exe in search of the special keyword "Fehler" (= Error).  

It was last updated to After Effects version CC2018, but should run with newer versions as well. The script doesn't check for After Effects by itself, therefore the path to aerender.exe has to edited in the code. 

All outputs are in German. I don't mind to make an Englisch translation if there is interest. Just drop me a line. 

### Limitations
MrRenderMan can be used as network renderer, when run in parallel on several computers and with the "skip exisiting frames" option checked in After Effects rendering settings. But if there are a lot of workers running and rendering speeds are fairly high, crashes of the workers are likely to happend. The workers crash because of file access errors, where two workers try to write to the same file. The crashed workers will restart, but they might produced corrupted frames. Therefore its good practice to always check the file sizes of the rendered images.



---
*MrRenderMan* is licensed under the [MIT License](https://github.com/mrtnRitter/MrRenderMan/blob/main/LICENSE).
