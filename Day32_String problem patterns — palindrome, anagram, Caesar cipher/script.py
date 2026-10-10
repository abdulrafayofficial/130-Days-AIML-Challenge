print('hello world!')

print('------------------Palindrome of Number --------------------')

def isPalindrome(number):
    reverse = 0 
    original = number
    while(number > 0):
        digit = number % 10
        reverse = reverse*10 + digit
        number = number // 10

    if original == reverse:
        return True
    else:
        return False
result = isPalindrome(5667)
if result:
    print('Palindrome AHHHH')
else:
    print('Not Palindrome AHHH')


print('------------------Palindrome of String --------------------')

def isPalindromeString(s):
    cleaned = "".join(ch for ch in s.lower() if ch.isalnum())
    reverse = cleaned[::-1]
    if cleaned == reverse:
        return True
    return False

print(isPalindromeString("madam"))        # True
print(isPalindromeString("Madam"))        # True
print(isPalindromeString("Nurses Run"))   # True
print(isPalindromeString("hello"))  
print(isPalindromeString("A man, a plan, a canal: Panama"))  


print('------------------Anagram.... --------------------')

def is_anagram(str1,str2):
    clean1 = "".join(ch for ch in str1.lower() if ch.isalnum())
    clean2 = "".join(ch for ch in str2.lower() if ch.isalnum())
    if len(clean1) != len(clean2):
        return False
    else:
        if sorted(clean1) == sorted(clean2):
            return True
        else:
            return False

str1 = 'earth'
str2 = 'heart'
result = is_anagram(str1,str2)

if result:
    print('Anagram!!')
else:
    print('Not Anagram!!')

print(is_anagram("earth", "hearts"))   
print(is_anagram("earth", "heart"))    
print(is_anagram("Dormitory", "Dirty Room"))  


print('------------------Caeser Cipher --------------------')
print(ord('a'),ord('z'))
print(chr(122))
print((30+3)%26)


def encrypt(text , key):
    result = ''
    for ch in text.lower():
        if ch.isalpha():
            num = ord(ch) - ord('a')
            shifted = (num + key) % 26
            new_ch = chr(shifted + ord('a'))
            result += new_ch
        else:
            result += ch

    return result


def decrypt(text , key):
    result = ''
    for ch in text.lower():
        if ch.isalpha():
            num = ord(ch) - ord('a')
            shifted = (num - key) % 26
            new_ch = chr(shifted + ord('a'))
            result += new_ch
        else:
            result += ch

    return result


print(encrypt('abc',3))
print(encrypt('xyz abc!', 3))


print(decrypt('abc',3))
print(decrypt('xyz abc!', 3))


print('------------------Run-Length Encoding --------------------')

def run_length_encode(text):
    if text == "":
        return ""

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    result += text[-1] + str(count)
    return result

print(run_length_encode('aaabbbcccaa'))   # a3b3c3a2
print(run_length_encode('abc'))           # a1b1c1
print(run_length_encode('zzzz'))          # z4