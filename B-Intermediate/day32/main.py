import smtplib

my_email = "email"
password = "password"

with smtplib.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(
        user=my_email,
        password=password)
    conn.sendmail(
        from_addr=my_email,
        to_addrs="email",
        msg="Subject:Test\n\nThis is a test smpt email")
