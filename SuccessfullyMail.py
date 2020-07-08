import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("nilesh0109choubisa@gmail.com", "7414893737")


    # message
message_success = "Achieved your desired accuracy without tweeking . Congrats "


    # sending the mail
s.sendmail("nilesh0109choubisa", message_success)


    # terminating the session
s.quit()
