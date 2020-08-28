# NvidiaKDEGraphicFix
Now, KDE users got rid of the graphics glitches of the nvidia graphics card! You will never see damn broken graphics again.
# How does this work?
This modifies the 95hdparm-apm file, which has a similar name in most Linux, and says what to do when the computer wakes up from sleep mode. I added a code into it that allows the user to log out. In this way, when the computer wakes up, all KDE software that the user runs are restarted. The disadvantage of this is that it takes a long time to open but this solved my problem. I hope it resolves yours too.
# What is the problem?
When you put a computer using Nvidia to sleep and wake the computer from sleep mode, the texts disappear, the window size is distorted and graphical errors like this occur. Would occur. Thankfully, we got rid of this problem now.
<img src="kde_nvidia_error.jpg">
# How I found that method?
I bought a new computer and never researched KDE. I have an Nvidia graphics card in my computer. This also pillaged KDE. I searched for solutions on the internet for 3 days, but because other people's solutions did not solve all the errors, I got to work myself one evening. I have tried many things. Eventually I accidentally pressed the "logout" button and realized that the problems were resolved. Then I found the system files that Linux runs when it wakes up. How Does? I looked at "locate sleep" and all directories. Finally something came out. I modded the "thaw | resume)" part by accepting the risk of disrupting the sleep mode feature of my computer in that file starting with 95. I entered the logout code there. Problem solved.
# Requirements
* Python3
* Root permission
# Follow me!
Twitter:@0rbianta<br/>
And nothing else. I'm not a virtual social person. 😂
