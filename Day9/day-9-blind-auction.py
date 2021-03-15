###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 9 project - Christopher Hagan
#
###################################

from art import logo

print('{}\n'.format(logo))

secret_bids = {}
end_bidding = False
while not end_bidding:
    person = input('What is your name : ')
    bid = int(input('What is your bid : £'))
    secret_bids[person] = bid

    if input('\nIs there another bid? (yes or no): ').lower().startswith('n'):
        end_bidding = True

highest_bidder = {
    'bid': 0,
    'people': []
}
for person in secret_bids:
    if secret_bids[person] > highest_bidder['bid']:
        highest_bidder['bid'] = secret_bids[person]
        highest_bidder['people'].clear()
        highest_bidder['people'].append(person)
    elif secret_bids[person] == highest_bidder['bid']:
        highest_bidder['people'].append(person)

print('The bid of £{} was highest, this was made by {}.'.format(highest_bidder['bid'], highest_bidder['people']))
