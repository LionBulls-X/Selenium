import re
import requests


class TelegramAuth:
    BASE_URL = "https://my.telegram.org"

    def __init__(self):
        self.session = requests.Session()
        self.phone_number = self.get_phone_number()
        self.send_code()

    def get_phone_number(self):
        while True:
Onur_header = render('Onur Meta ', colors=['white', 'blue'], align='center')
            number = input("•𝐇𝐄𝐒𝐀𝐏 𝐂𝐀𝐋𝐌𝐀 𝐏𝐀𝐍𝐄𝐋𝐈𝐍𝐄 𝐇𝐎𝐒 𝐆𝐄𝐋𝐃𝐈𝐍𝐈𝐙 𝐃𝐎𝐆𝐑𝐔𝐋𝐀𝐌𝐀 𝐈𝐂𝐈𝐍 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐍𝐔𝐌𝐀𝐑𝐀𝐍𝐈𝐙𝐈  𝐘𝐀𝐙𝐈𝐍𝐈𝐙 +90**""): ").strip()
            # + ile başlamalı ve ardından 10 ila 15 rakam içermeli
            if re.match(r"^\+\d{10,15}$", number):
                return number
            print("• INVALID FORMAT. Use full international format like +12345678900.")

    def send_code(self):
        url = f"{self.BASE_URL}/auth/send_password"
        data = {'phone': self.phone_number}
        headers = {'Accept-Language': 'en-US,en;q=0.9'}

        response = self.session.post(url, data=data, headers=headers)
        if 'random_hash' in response.text:
            self.random_hash = response.json().get('random_hash')
            print(f"• DONE GET HASH: {self.random_hash}")
            self.enter_code()
        else:
            print("• ERROR: Unable to get hash. Check your phone number.")
            self.__init__()

    def enter_code(self):
        code = input("• TELEGRAMA GÖNDERİLEN KODU GİRİN: ").strip()
        url = f"{self.BASE_URL}/auth/login"
        data = {
            'phone': self.phone_number,
            'random_hash': self.random_hash,
            'password': code
        }
        headers = {'Accept-Language': 'en-US,en;q=0.9'}

        response = self.session.post(url, data=data, headers=headers)
        if 'stel_token' in response.cookies:
            self.token = response.cookies['stel_token']
            print(f"• DONE GET TOKEN: {self.token}")
            self.get_hash()
        else:
            print("• ERROR: Invalid code.")
            self.__init__()

    def get_hash(self):
        url = f"{self.BASE_URL}/delete"
        headers = {
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0',
            'Cookie': f'stel_token={self.token}'
        }

        response = self.session.get(url, headers=headers).text
        match = re.search(r"hash: '([^']+)'", response)
        if match:
            self.delete_hash = match.group(1)
            print(f"• DONE GET HASH: {self.delete_hash}")
            self.delete_account()
        else:
            print("• ERROR: Failed to retrieve hash.")
            self.__init__()

    def delete_account(self):
        url = f"{self.BASE_URL}/delete/do_delete"
        data = {
            'hash': self.delete_hash,
            'message': ''
        }
        headers = {
            'Cookie': f'stel_token={self.token}',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = self.session.post(url, data=data, headers=headers).text
        if 'true' in response:
            print("• DONE: Your account has been deleted.")
        else:
            print("• ERROR: Failed to delete account.")
            self.__init__()


if __name__ == "__main__":
    TelegramAuth()
