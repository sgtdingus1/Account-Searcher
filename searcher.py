from colorama import Fore, Back, Style
import time
#print(Fore.GREEN)

Base = '[+] '

Repl = 'repl.it:  https://replit.com/@'
About = 'About.me:  https://about.me/'
Github = 'Github:  https://www.github.com/'
Codecademy = 'Codecademy: https://www.codecademy.com/profiles/'
Roblox = 'Roblox:  https://www.roblox.com/user.aspx?username='
Slack1 = 'Slack: https://'
Slack2 = '.slack.com'
Spotify = 'Spotify:  https://open.spotify.com/user/'
Scratch = 'Scratch:  https://scratch.mit.edu/users/'
PokemonShowdown = 'Pokemon Showdown: https://pokemonshowdown.com/users/'
Pastebin = 'Pastebin:  https://pastebin.com/u/'
Patreon = 'Patreon: https://www.patreon.com/'
Steam = 'Steam:  https://steamcommunity.com/id/'
TikTok = 'TikTok: https://tiktok.com/@'
Giphy = 'Giphy: https://giphy.com/'
FortniteTracker = 'FortniteTracker: https://fortnitetracker.com/profile/all/'
Facebook = 'Facebook:  https://www.facebook.com/'
Duolingo = 'Duolingo:  https://www.duolingo.com/profile/'



print('What is the users name?  ')

print(Fore.BLUE)

user = input()

print(Fore.GREEN)

print(Base + 'Finding accounts unser the name of:  ' + user)

time.sleep(0.5)

print('Found!')

print()

print(Fore.RED + 'Here are the account links with the user ' + user + ' accociated:  ')

print(Fore.BLUE)

Repl = (Base + Repl + user)
Github = (Base + Github + user)
About = (Base + About + user)
Codecademy = (Base + Codecademy + user)
Roblox = (Base + Roblox + user)
Slack = (Base + Slack1 + user + Slack2)
Spotify = (Base + Spotify + user)
Scratch = (Base + Scratch + user)
PokemonShowdown = (Base + PokemonShowdown + user)
Pastebin = (Base + Pastebin + user)
Patreon = (Base + Github + user)
Steam = (Base + Steam + user)
TikTok = (Base + TikTok + user)
Giphy = (Base + Giphy + user)
FortniteTracker = (Base + FortniteTracker + user)
Facebook = (Base + Facebook + user)
Duolingo = (Base + Duolingo + user)

print()

print(Repl)
print(Github)
print(About)
print(Codecademy)
print(Roblox)
print(Slack)
print(Spotify)
print(Scratch)
print(PokemonShowdown)
print(Pastebin)
print(Patreon)
print(Steam)
print(TikTok)
print(Giphy)
print(FortniteTracker)
print(Facebook)
print(Duolingo)
