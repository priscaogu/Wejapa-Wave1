
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
length = len(verse)


index_and = verse.index("and", 1)
index_you = verse.index("you", 180, -1)
count_you = verse.count("you", 1, -1)

#using sring formatting 

print("The length of the string variable verse is {}.\nThe index of the first occurrence of the word 'and' in verse is {} .\nThe index of the last occurrence of the word 'you' in verse is {}.\nThe count of occurrences of the word 'you' in the verse is {}".format(length,index_and,index_you,count_you))