from twilio.rest import TwilioRestClient

account_sid = "ACee9fefefd2b97657371e92735bfbe49f"
auth_token = "e0ad9de07e36e55efc0cca05d4f7e7cd"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "Moomie the bestest!",
    to = "+17788856670",
    from_= "+16042567980")
print message.sid
