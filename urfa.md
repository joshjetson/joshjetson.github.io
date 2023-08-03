
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

It's an outdated machine and the gpu is not supported by nvidia anymore either (annoying to make work right now), but still pretty ok. So I decided to use it for the following:

- Cloud Services
- SQL/Database Stuff
- Multimedia (Jellyfin)
- Local Git Server
- Apache Web Server
- Project Management Software Server
- Remote Development Environment
- OpenSSH

So everything is going well and im getting good use out of the machine.
Then one day I thought "Hmm I wonder if anyone has tried to login to this thing" so I checked the login logs and was shocked. Within a period of 3 days I had thousands of failed login attempts.
<br>
Immediately I though "I need to tighted security up" I made a crazy long password and implemented this SSH firewall called Fail2Ban.
Then I thought .....
Wait a second. These attacks are constant maybe I could study them and learn more about them. I decided to ban people for an hour only after 5 failed login attempts. That way I could get a better distribution of data and it would make it even more difficult for someone to actually break in, even though I ran the numbers and using a brute force attack would take thousands of years still to hack into my system.
