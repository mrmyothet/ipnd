from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1fb92f50fc9559fcc66ff2d0e4367525"
# Your Auth Token from twilio.com/console
auth_token  = "28d49bcc889f2bc6352c952366fd3269"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+9509687917578",
    from_="+(959) 551-5502",
    body="Hello! I'm Khun Cho.")

print(message.sid)
