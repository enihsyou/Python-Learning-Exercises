# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup

SMTP_host = "192.168.1.103"
server = smtplib.SMTP(host=SMTP_host)
sender = "enihsyou@enihsyou.synology.me"
receiver = ["1131626817@qq.com"]


def send_mail(text):
    message = MIMEText(text, "plain")
    message['From'] = sender
    message['To'] = ", ".join(receiver)
    message['Subject'] = text
    try:
        server.send_message(message)
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def check_book(search_id, offset=2):
    response = requests.get(
        "http://opac.usst.edu.cn:8080/opac/item.php",
        params={"marc_no": search_id})
    soup = BeautifulSoup(response.content, "lxml")
    book_name = soup.select("#item_detail > dl:nth-of-type(1) > dd > a")[0].text

    books = soup.select("#item > tr")
    for book in books[offset:]:
        book = book.find_all("td")
        book_id = book[0].text
        book_status = book[4].text
        s = " ".join([book_name, book_id, book_status])
        print(s)
        if book_status == "可借":
            send_mail(s)


check_book("0000506934")
check_book("0000373998")
check_book("0000501786")
