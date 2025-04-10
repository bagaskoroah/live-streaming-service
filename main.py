from tabulate import tabulate

# Dictionary yang menyimpan data pengguna: nama, plan aktif, durasi berlangganan, dan kode referral
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

class User:
    """
    Class User digunakan untuk mewakili pelanggan yang sudah terdaftar.
    Menyediakan fitur untuk mengecek benefit plan, detail plan pengguna, dan upgrade plan.
    """

    # Tabel berisi fitur dan harga berdasarkan jenis plan
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
        """
        Konstruktor untuk membuat instance User.
        :param username: Nama pengguna
        :param duration_plan: Durasi langganan (dalam bulan)
        :param current_plan: Jenis plan yang aktif
        """
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan

    def check_benefit(self):
        """
        Menampilkan seluruh daftar benefit yang tersedia untuk semua plan.
        """
        headers = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Services']
        print('PacFlix Plan List\n')
        print(tabulate(User.benefit_table, headers=headers))

    def check_plan(self, username):
        """
        Menampilkan detail plan dan benefit berdasarkan plan yang dimiliki pengguna.
        :param username: Nama pengguna
        """
        for key, value in data.items():
            if key == username:
                try:
                    # Tampilkan plan dan durasi aktif
                    print(value[0])
                    print(f'{value[1]} Bulan')

                    # Filter benefit sesuai jenis plan
                    if value[0] == 'Basic Plan':
                        filtered_data = [[column[0], column[3]] for column in User.benefit_table]
                        filtered_headers = ['Basic Plan', 'Services']
                        print('\nBasic Plan PacFlix Benefit List\n')
                        print(tabulate(filtered_data, headers=filtered_headers))

                    elif value[0] == 'Standard Plan':
                        filtered_data = [[column[1], column[3]] for column in User.benefit_table]
                        filtered_headers = ['Standard Plan', 'Services']
                        print('\nStandard Plan PacFlix Benefit List\n')
                        print(tabulate(filtered_data, headers=filtered_headers))

                    elif value[0] == 'Premium Plan':
                        filtered_data = [[column[2], column[3]] for column in User.benefit_table]
                        filtered_headers = ['Premium Plan', 'Services']
                        print('\nPremium Plan PacFlix Benefit List\n')
                        print(tabulate(filtered_data, headers=filtered_headers))

                    else:
                        raise ValueError('Format jenis plan salah, bukan berupa angka!')

                except ValueError as e:
                    print(f'Error: {e}. Silakan coba lagi sesuai dengan format yang diminta!\n')

    def upgrade_plan(self, current_plan, new_plan):
        """
        Melakukan upgrade plan pengguna ke plan yang lebih tinggi jika memenuhi syarat.
        :param current_plan: Plan yang sedang aktif
        :param new_plan: Plan tujuan upgrade
        :return: Harga plan baru setelah diskon jika ada, atau pesan kesalahan
        """
        for key, value in data.items():
            if self.username == key:
                if new_plan != self.current_plan:
                    # Jika saat ini Basic Plan
                    if self.current_plan == 'Basic Plan':
                        if self.duration_plan > 12:
                            # Diskon 5% jika langganan > 12 bulan
                            if new_plan == 'Standard Plan':
                                self.current_plan = new_plan
                                return 160000 - (0.05 * 160000)
                            elif new_plan == 'Premium Plan':
                                self.current_plan = new_plan
                                return 200000 - (0.05 * 200000)
                            else:
                                raise Exception('Plan yang kamu maksud tidak tersedia.')
                        else:
                            if new_plan == 'Standard Plan':
                                self.current_plan = new_plan
                                return 160000
                            elif new_plan == 'Premium Plan':
                                self.current_plan = new_plan
                                return 200000
                            else:
                                raise Exception('Plan yang kamu maksud tidak tersedia.')

                    # Jika saat ini Standard Plan
                    elif self.current_plan == 'Standard Plan':
                        if self.duration_plan > 12:
                            if new_plan == 'Basic Plan':
                                return 'Kamu tidak bisa downgrade plan!'
                            elif new_plan == 'Premium Plan':
                                self.current_plan = new_plan
                                return 200000 - (0.05 * 200000)
                            else:
                                raise Exception('Plan yang kamu maksud tidak tersedia.')
                        else:
                            if new_plan == 'Basic Plan':
                                return 'Kamu tidak bisa downgrade plan!'
                            elif new_plan == 'Premium Plan':
                                self.current_plan = new_plan
                                return 200000
                            else:
                                raise Exception('Plan yang kamu maksud tidak tersedia.')

                    # Jika saat ini Premium Plan
                    elif self.current_plan == 'Premium Plan':
                        return 'Plan kamu sudah plan yang maksimum, tidak bisa di-upgrade ke plan lain!'
                else:
                    raise Exception('Kamu tidak bisa upgrade plan ke plan yang sama.')

class NewUser:
    """
    Class NewUser digunakan untuk calon pelanggan yang belum terdaftar.
    Menyediakan fitur untuk memilih plan dan memanfaatkan referral code.
    """

    def __init__(self, username):
        """
        Konstruktor untuk membuat instance NewUser.
        :param username: Nama pengguna baru
        """
        self.username = username

    def pick_plan(self, new_plan, code_referral):
        """
        Memilih plan saat registrasi awal dan mengecek validitas referral code.
        :param new_plan: Plan yang dipilih
        :param code_referral: Kode referral dari pengguna lain
        :return: Harga plan setelah potongan 4% jika referral valid
        """
        referral_list = list()

        # Ambil seluruh referral code dari data pengguna
        for key, value in data.items():
            referral_list.append(value[2])

        # Cek referral code dan jenis plan
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
