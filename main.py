from tabulate import tabulate

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

class User:

  # tabel benefit Pacflix users
  benefit_table = [
          [True, True, True, 'Bisa Stream'],
          [True, True, True, 'Bisa Download'],
          [True, True, True, 'Kualitas SD'],
          [False, True, True, 'Kualitas HD'],
          [False, False, True, 'Kualitas UHD'],
          [1, 2, 4, 'Number of Devices'],
          ['3rd party Movie only', 'Basic Plan Content + Sports', 'Basic Plan + Standard Plan + PacFlix Original Series', 'Jenis Konten'],
          [120000, 160000, 200000, 'Harga']
      ]

  def __init__(self, username, duration_plan, current_plan):
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan

  def check_benefit(self):
      headers = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Services']
      print('PacFlix Plan List\n')
      print(tabulate(User.benefit_table, headers=headers))

  def check_plan(self, username):
    for key, value in data.items():
      if key == self.username:
        try:
          print(value[0])
          print(f'{value[1]} Bulan')

          if value[0] == 'Basic Plan':
            filtered_data = [[column[0], column[3]] for column in User.benefit_table]
            filtered_headers = ['Basic Plan', 'Services']

            print('\nBasic Plan PacFlix Benefit List\n')
            print(tabulate(filtered_data, headers=filtered_headers))

          elif value[0] == 'Standard Plan':
            filtered_data = [[column[1], column[3]] for column in User.benefit_table]
            filtered_headers = ['Standard Plan', 'Services']

            print('\nBasic Plan PacFlix Benefit List\n')
            print(tabulate(filtered_data, headers=filtered_headers))

          elif value[0] == 'Premium Plan':
            filtered_data = [[column[2], column[3]] for column in User.benefit_table]
            filtered_headers = ['Premium Plan', 'Services']

            print('\nBasic Plan PacFlix Benefit List\n')
            print(tabulate(filtered_data, headers=filtered_headers))

          else:
            raise ValueError('Format jenis plan salah, bukan berupa angka!')

        except ValueError as e:
          print(f'Error: {e}. Silakan coba lagi sesuai dengan format yang diminta!\n')

  def upgrade_plan(self, current_plan, new_plan):
    for key, value in data.items():
      if self.username == key:
        if new_plan != self.current_plan:
          if self.current_plan == 'Basic Plan':
            if self.duration_plan > 12:
              if new_plan == 'Standard Plan':
                return 160000 - (0.05*160000)
              elif new_plan == 'Premium Plan':
                return 200000 - (0.05*200000)
              else:
                raise Exception('Plan yang kamu maksud tidak tersedia.')
            else:
              if new_plan == 'Standard Plan':
                return 160000
              elif new_plan == 'Premium Plan':
                return 200000
              else:
                raise Exception('Plan yang kamu maksud tidak tersedia.')

          elif self.current_plan == 'Standard Plan':
            if self.duration_plan > 12:
              if new_plan == 'Basic Plan':
                return 'Kamu tidak bisa downgrade plan!'
              elif new_plan == 'Premium Plan':
                return 200000 - (0.05*200000)
              else:
                raise Exception('Plan yang kamu maksud tidak tersedia.')
            else:
              if new_plan == 'Basic Plan':
                return 'Kamu tidak bisa downgrade plan!'
              elif new_plan == 'Premium Plan':
                return 200000
              else:
                raise Exception('Plan yang kamu maksud tidak tersedia.')

          elif self.current_plan == 'Premium Plan':
            return 'Plan kamu sudah plan yang maksimum, tidak bisa di-upgrade ke plan lain!'

        else:
          raise Exception('Kamu tidak bisa upgrade plan ke plan yang sama.')

class NewUser:

  def __init__(self, username):
    self.username = username

  def pick_plan(self, new_plan, code_referral):
    referral_list = list()

    for key, value in data.items():
      referral_list.append(value[2])

    if code_referral in referral_list:
      if new_plan == 'Basic Plan':
        return 120000 - (120000 * 0.04)
      elif new_plan == 'Standard Plan':
        return 160000 - (160000 * 0.04)
      elif new_plan == 'Premium Plan':
        return 200000 - (200000 * 0.04)
      else:
        raise Exception('Plan yang kamu maksud tidak tersedia.')
    else:
        raise Exception('Referral code tidak dapat ditemukan.')
    
user_1 = User('Shandy', 12, 'Basic Plan')
user_1.check_plan(user_1.username)
print()
print(user_1.upgrade_plan(user_1.current_plan, 'Standard Plan'))
print()
user_2 = User("Cahya", 24, "Standard Plan")
user_2.check_plan(user_2.username)
print()
print(user_2.upgrade_plan(user_2.current_plan, "Premium Plan"))

