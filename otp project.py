import random
import string
from twilio.rest import Client
otp_length=5
otp_number=""
otp_letters=string.digits+string.ascii_letters
for i in range(otp_length):
    otp_number+=random.choice(otp_letters)
print(otp_number)
b="YOUR OTP NUMBER IS: "+otp_number

account_sid="AC67c9f4d7a2ac57232976768592a1d295"
auth_token="4fa93918b909cb7e8cf6f289a9d6c5cd"
client=Client(account_sid,auth_token)
message=client.messages\
         .create(
            to="+919500461337",
            from_="+12057549165",
            body=b)
message.sid

user_input=input()

if(otp_number==user_input):
    print("Your otp is correct")

else:
    print("Your otp is not correct")
