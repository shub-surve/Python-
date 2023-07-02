from email.message import EmailMessage
from apppass import password
import ssl
import smtplib

emil_sender = 'shubhamsurve30803@gmail.com'
email_pass = password

email_receiver = emil_sender

sub = 'HELLO HOW ARE YOU, HOPE YOU ARE DOING FINE'
body = """
I hope this email finds you in good health and high spirits. Today, I felt compelled to take a moment and extend my heartfelt well wishes and encouragement to you.

As you embark on your new journey, whether it's a new job, a fresh chapter in your education, or a personal endeavor, I want you to know that you have my full support and belief in your capabilities. Your determination, passion, and dedication have always inspired those around you, and I have no doubt that you will excel in whatever you set your mind to.

Remember, each step you take is an opportunity to grow, learn, and discover your true potential. Embrace the challenges that come your way, as they will mold you into an even stronger and more resilient individual. Embrace the successes, no matter how big or small, and use them as fuel to drive you forward.

In the face of uncertainty, keep your faith in yourself and your abilities. You have the talent and the tenacity to overcome any obstacles that may arise. Trust in your intuition, for it will guide you towards making the right decisions.

Surround yourself with positive influences and lean on your support system whenever needed. Family, friends, and mentors are here to uplift and encourage you throughout your journey. Together, we will celebrate your victories and provide a steady hand during moments of doubt.

Always remember that success is not merely defined by achievements, but also by the lessons learned along the way and the impact you make on others. Your kindness, generosity, and empathy have touched countless lives, and I have no doubt that you will continue to make a positive difference wherever you go.

As you move forward, stay true to yourself and your values. Stay curious, remain open to new ideas, and embrace the beauty of continuous growth. There will be highs and lows, but remember that every experience is an opportunity for growth and self-discovery.

Believe in yourself, because I certainly believe in you. You have the ability to make a meaningful impact on the world, and I cannot wait to witness your journey unfold.

Wishing you all the success, joy, and fulfillment that life has to offer. May your path be filled with opportunities and accomplishments, and may each day bring you closer to your dreams.

If there is anything you need, be it a listening ear, advice, or just someone to cheer you on, know that I am here for you.

Congratulations, and all the best for your exciting new venture
"""
em = EmailMessage()
em['From'] = emil_sender
em['To'] = email_receiver
em['Subject'] = sub
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emil_sender, email_pass)
    smtp.sendmail(emil_sender, email_receiver, em.as_string())

