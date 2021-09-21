# MrRenderMan
Multithread render manager for After Effects.

<img src="/Screens/Start.jpg" width="33%" /> <img src="/Screens/Settings.jpg" width="33%" /> <img src="/Screens/Workers.jpg" width="33%" />

### Motivation
When starting working professionally with After Effects in 2014, it doesn't fully utilize our computer hardware. Long rendering times with an idling CPU haven't been acceptable for serious business work (although it gets better, this is still an issue with After Effects in 2021).  
All professional solutions have been to expensive for a growing business, but playing around with the After Effects command line renderder soon reveals it's potential.  
So I started to dig deeper into Python and tried to get a render manager done.  

This tool have been used for 4 years until we switched to a more network orientated solution (AE internal mutli-node rendering system is terrible and the workers did often crash because of access errors).  
It was continously developed over that time. This is the last stable version from 2018. 

### Usage
