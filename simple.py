import smtplib
smtpObj= smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('pankajjb93@gmail.com', 'Papa.123')
smtpObj.sendmail('pankajjb93@gmail.com',"sunilkumarjangiar2012@gmail.com","subject:hello mr.\nhow do you do")
{}
smtpObj.quit()
