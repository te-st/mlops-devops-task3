import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("nilesh0109choubisa@gmail.com", "7414893737")


    # message
message = "Your accuracy is less than 90% .Try again"


    # sending the mail
s.sendmail("nilesh0109choubisa@gmail.com", message)


    # terminating the session
s.quit()
