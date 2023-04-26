f = open("Sessions/0414_B2_session3/mbox-short.txt", "r")
text = f.readlines()
total = 0
emails = {}

for line in text:
    if line.startswith("From:"):
        total += 1
        email = (line.strip("\n")).split(" ")[1]
        if email in emails:
            emails[email] += 1
        else:
            emails[email] = 1
                    
for email, count in emails.items():
    print(f"{email}: {count}")

for email, messages in emails.items():
    if messages == max(emails.values()):
        sender = email

print(f"\nTotal number of emails: {total}")
print(f"\nMost emails sent by: {sender} ({max(emails.values())})\n")
