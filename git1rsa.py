import math
def is_prime(a):
    flag=0
    if a>=2:
        for i in range(2,(a//2+1)):
            if (a % i) == 0 :
                flag=1
                break
            if(flag==0):
                return True
            else:
               return False
p=int(input("enter the value of p\n"))
while not(is_prime(p)==True):
    print("p is not prime")
    p=int(input("enter the value of p hint ..179\n"))

q=int(input("enter the value of q\n"))
while not(is_prime(q)==True):
    print("q is not prime")
    q=int(input("enter the value of q hint ..179\n"))

n = p * q
r= (p-1)*(q-1)
print("RSA Modulus(n) is:",n)
print("Eulers Toitent(r) is:",r)

def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e

def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b

def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s%r
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
print("The value of e is:",e)

eugcd(e,r)
d = mult_inv(e,r)
print("The value of d is:",d)
print("*****************************************************")
public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
def encrypt(pub_key, msg):
    e,n=pub_key

    msg_ciphertext = [pow(ord(c), e, n) for c in msg]
    return msg_ciphertext

    
def decrypt(priv_key, msg_ciphertext):
    d,n=priv_key
   
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    # No need to use ord() since c is now a number
    # After decryption, we cast it back to character
    # to be joined in a string for the final result
    return (''.join(msg_plaintext))
msg = input("What would you like encrypted:")
print("Your message is:",msg)
print([ord(c) for c in msg])
enc_msg=encrypt(public,msg)
print("Encrypted msg: ")
print(''.join(map(lambda x: str(x), enc_msg)))
print("Decrypted msg: ")

print(decrypt( private,enc_msg,))
