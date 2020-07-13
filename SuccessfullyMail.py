import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("sukhdeepsinghsoni1998@gmail.com", "8003322337")


    # message
message_success = "Achieved your desired accuracy without tweeking . Congrats "


    # sending the mail
s.sendmail("sukhdeepsinghsoni1998", message_success)


    # terminating the session
s.quit()
