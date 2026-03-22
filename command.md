# Linux Commands — My Reference

Commands I use and learn. Updated as I go.



## Navigation

`pwd` — show where you are right now  
`ls` — list files in directory  
`ls -a` — show hidden files too (dotfiles)  
`ls -la` — full list with permissions, owner, size  
`cd /path` — move to directory  



## Files & Directories

`mkdir name` — create directory  
`cp file1 file2` — copy file  
`mv file1 file2` — move or rename, same command for both  
`rm file` — remove file, no trash, gone forever  
`cat file` — dump file content to terminal  
`head file` — first 10 lines, useful for big files  
`less file` — read file page by page, q to quit  
`nano file` — simple terminal editor, easier than vim  
`find /path -name "file"` — search file by name  
`grep "text" file` — search text inside file, use this constantly  



## Permissions & Users

`chmod 755 file` — change permissions, 7=owner, 5=group, 5=others  
`chown user:group file` — change who owns the file  
`sudo command` — run as root, use carefully  
`whoami` — check which user you are right now  
`id` — shows your UID, GID and groups  
`adduser username` — create new user properly  



## Processes

`ps aux` — show all running processes  
`top` — live process monitor  
`htop` — same but nicer, needs to be installed  
`kill -15 PID` — ask process to stop gracefully, try this first  
`kill -9 PID` — force kill, use only if -15 didn't work  



## System Info

`df -h` — how much disk space is left  
`du -sh /path` — how heavy is this folder  
`free -h` — RAM usage at this moment  
`uname -a` — system info, kernel version etc  
`uptime` — how long server has been running  



## Networking

`ping host` — check if host is reachable  
`curl url` — fetch URL, useful for testing APIs  
`wget url` — download file from URL  
`ss -tulnp` — show open ports and what's listening  
`netstat -tulnp` — same as ss, older systems  
`dig domain` — DNS lookup, shows what resolves where  
`ssh user@host -p port` — connect to remote server  



## Logs

`tail -f /var/log/syslog` — follow log in real time, used this a lot in Bandit  

