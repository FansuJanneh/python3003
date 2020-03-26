def palindrome(word):
    wordReversed = ""
    for x in reversed(word):
        wordReversed = wordReversed + x
    return wordReversed

def reverse(word):
   length = len(word)
   reversed = ""
   while length > 0:
      reversed += word[length - 1]
      length -= 1
   return reversed

print(palindrome("python"))
print(reverse("python"))