# crawl data gmail form web
# import functions xu ly gmail
from mainexp import emailProcess, printMes


def main():
    emails = ['abc@gmail.com', 'hoang@gmail.com',
              'jav@gmail.com', 'wao@fpt.com', 'craw@edu.com.vn']
    for email in emails:
        username, domain = emailProcess(email)  # tao 2 biet moi
        printMes(username, domain)


if __name__ == "__main__":
    main()
