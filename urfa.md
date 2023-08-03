
<table rules=none>
 <tr>
<td> <img src="https://i.imgur.com/h3VBZMf.png"></td>
<td> <h2><a href="https://joshjetson.github.io">Universal Repository<br>of<br>Flagged<br>IP Addresses</a></h2><br>An ever growing lake of IP addresses from wannabe hackers</td>
</tr>
</table>


[View the actual project here](https://github.com/joshjetson/URFA)

------------------------------

## Backstory

*I have this laptop that I bought in 2015 for 150 dollars on craigslist that I wanted to continue to get use out of.*

<img src="https://imgur.com/gZddJpB.png">

It's an outdated machine and the gpu is not supported by nvidia anymore either (annoying to make work right now), but still pretty ok. So I decided to use it for:

- Cloud Services
- SQL/Database Stuff
- Multimedia (Jellyfin)
- Local Git Server
- Apache Web Server
- Project Management Software Server
- Remote Development Environment
- OpenSSH

*So everything is going well and im getting good use out of the machine.*
> Then one day I thought "Hmm I wonder if anyone has tried to login to this thing, (SSH in)" so I checked the failed login log and was shocked. Within a period of 3 days I had thousands of failed login attempts.


*Immediately I thought "I need to tighted security up" so I made a crazy long password and implemented this SSH firewall called Fail2Ban.*
> Then I thought .....
> Wait a second. These attacks are constant maybe I could study them and learn more about them. Things like:


- Where they are coming from geographically.
- The frequency of them, inidividually and collectively.
- In what area of the world is the highest concentration of attacks coming from ?
- What does the geographic distribution of the attacks looks like ?
- Are they from people using bots or not whats the percentage of each ?
- Is it from people behind a VPN or not and whats the percentage of each ?
- Could I train a machine learning model with this data to make it predict certain things ?

> I decided to ban people for an hour only after 5 failed login attempts. 
> That way I could get a better distribution of data and it would make it even more difficult for someone to actually break in, even though I ran the numbers and using a brute force attack would take thousands of years still to hack into my system.


*I began to understand I needed a simple file that would have:*

- The attemtped user/login name
- The IP address of the attack.
- The country where the IP address is tied to.
- The city where the IP address is tied to.
- The time and day of the attack.

> I decided to store the data in a simple CSV file just cause its a simple lazy solution.

## Creating the data pipeline

---------------------------------------

*The original server logs were not very pretty so I needed to clean them up and put the cleaned up data in the CSV file but in an automated way since the data was constantly flowing in*

I needed a pipeline !

*First, though, I needed to consider a few issues I would have in the process*

**Caveats**

After examining the logs I noticed a few issues but ill just discuss one here.

- There were 300 - 500 new attempts per hour.
> What if there were 600 or 200 though ?
> I don't want to keep cleaning the same data over and over from the log file as new entries are loggged, meaning I shouldnt clean the whole file everytime there is a new entry logged because thats gonna get really redundant really quick and its gonna use too much resources.


With the caveats in mind I need a pipeline that will (Hourly):

- Collect the last 700 entries in the log file, even if they are duplicates.
- Clean and organize the data (Used Python, Pandas and imported the OS)
> - Drop overlapping data / duplicates.
> - Drop log entries without an ip address or bad data.
> - Take the IP addresses and extract the geographic details
> - Take the geographic details and add them into new columns that correspond to the correct rows containing their matching IP addresses and login data.
- Update the CSV with the cleaned, enriched and organized new entries (Pandas)
> I want other people to be able to use the data or contribute ill so ill also include all the git actions in the pipline.
> - Add the files to the staging area (Cronjob)
> - Commit the files (Cronjob)
> - Push the changes (Cronjob)



I implemented all of this by setting up cronjobs in my crontab which runs (Hourly) a python script and all the git stuff automatically.
