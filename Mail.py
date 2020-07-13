import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("sukhdeepsinghsoni1998@gmail.com", "8003322337")


    # message
 message = "Your accuracy is less than 90% .Try again"


    # sending the mail
s.sendmail("sukhdeepsinghsoni1998@gmail.com", message)


    # terminating the session
s.quit()
