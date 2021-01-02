l = []#defines l as a list.
x = str

card = str(input("enter your card number"))
cardlen = len(card)
short_card = (card[(cardlen-4):(cardlen)])#finds the last 4 digits of the card number.
l.append("*" * (cardlen-4))#adds (amount of digits in card number -4) of *
l.append(short_card)#adds last 4 digits of card to list
s = "".join(l)#joins the two data values in l(last 4 digits of card and *s)
print(s)