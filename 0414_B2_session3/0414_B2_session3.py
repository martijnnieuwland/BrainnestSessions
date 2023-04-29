# f = open("Sessions/0414_B2_session3/mbox-short.txt", "r")
# text = f.readlines()
# total = 0
# emails = {}

# for line in text:
#     if line.startswith("From:"):
#         total += 1
#         email = (line.strip("\n")).split(" ")[1]
#         if email in emails:
#             emails[email] += 1
#         else:
#             emails[email] = 1
                    
# for email, count in emails.items():
#     print(f"{email}: {count}")

# for email, messages in emails.items():
#     if messages == max(emails.values()):
#         sender = email

# print(f"\nTotal number of emails: {total}")
# print(f"\nMost emails sent by: {sender} ({max(emails.values())})\n")


# 2. Write a list comprehension to generate a list of all possible pairs of numbers from two given lists.

# x = [1, 2, 3]
# y = [4, 5, 6]

# xy = [i * n for i in x for n in y]

# print(xy)


# 3. Write a list comprehension to find all the prime numbers between 1 and 100.

primes = [prime for prime in range(2, 101) if all(prime % number != 0 for number in range(2, prime))]

# for p in range(1, 101):
#     primes.append(p)
#     for i in range(2, p):
#         if p % i == 0:
#             primes.remove(p)
#             break

            
print(primes)

