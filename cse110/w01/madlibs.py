from configparser import NoSectionError


print('Welcome to MadLibs! Please respond to the following prompts:')

verb1 = input('Enter a Verb:')
noun1 = input('Enter a Noun:')
adj1 = input('Enter an Adjective:')
ani1 = input('Enter an Animal:')
adj4 = input('Enter an Adjective:')
verb2 = input('Enter a Verb:')
verb3 = input('Enter a Verb:')
adj2 = input('Enter an adjective:')
mov = input('Enter name of a movie:')
adj3 = input('Enter an Adjective:')
# yesterday, I was _ on top of the _, and I was feeling pretty _ about myself. However, I saw a _, and I lost my balance and fell off of _, the _ saw me and _ up to me and licked my NoSectionError
# and thats how me and that _ _ became the best of friends. The next week we went and visited the _, where we saw _. it was _

print(f'Yesterday, I was {verb1} on top of a {noun1}, and I was feeling pretty {adj1} about myself.')
print(f'However, I saw a {ani1}, and got {adj4} and lost my balance and fell off of the {noun1}.')
print(f'The {ani1} saw me fall, and {verb2} up to me and {verb3} my nose.')
print(f'And thats how that {adj2} {ani1} and I became the best of friends.')
print(f'The next week we visited the Theater, where we saw {mov.title()}.')
print(f'It was {adj3}')