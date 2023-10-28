from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class NavigationApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Navigation bar
        self.navigation_buttons = GridLayout(cols=6, size_hint=(1, None), height=50)
        buttons = [
            "Home", "Pembelian", "History", "Deposit", "Bantuan", "Profil"
        ]

        for button_text in buttons:
            button = Button(text=button_text)
            button.bind(on_release=self.navigate)
            self.navigation_buttons.add_widget(button)

        self.layout.add_widget(self.navigation_buttons)

        # Content area
        self.content_area = BoxLayout(orientation='vertical', padding=10)
        self.layout.add_widget(self.content_area)

        return self.layout

    def navigate(self, instance):
        self.content_area.clear_widgets()
        button_text = instance.text

        if button_text == "Home":
            # Show Home content
            self.show_home()
        elif button_text == "Pembelian":
            # Show Pembelian form
            self.show_pembelian()
        elif button_text == "History":
            # Show History table
            self.show_history()
        elif button_text == "Deposit":
            # Show Deposit form
            self.show_deposit()
        elif button_text == "Profil":
            # Show Profile information
            self.show_profile()

    def show_home(self):
        saldo_label = Label(text="Saldo: $1000")
        self.content_area.add_widget(saldo_label)

    def show_pembelian(self):
        pembelian_form = GridLayout(cols=2)
        layanan_label = Label(text="Pilih Layanan:")
        layanan_spinner = Spinner(
            text="Pilih Layanan",
            values=("A", "B", "C", "S")
        )
        harga_label = Label(text="Harga:")
        harga_input = TextInput(multiline=False)
        target_label = Label(text="Nomor Target:")
        target_input = TextInput(multiline=False)

        pembelian_form.add_widget(layanan_label)
        pembelian_form.add_widget(layanan_spinner)
        pembelian_form.add_widget(harga_label)
        pembelian_form.add_widget(harga_input)
        pembelian_form.add_widget(target_label)
        pembelian_form.add_widget(target_input)

        order_button = Button(text="Pesan")
        pembelian_form.add_widget(order_button)

        self.content_area.add_widget(pembelian_form)

    def show_history(self):
        history_table = GridLayout(cols=4)
        headers = ["Tgl. Transaksi", "Produk", "Jumlah", "Total"]
        for header in headers:
            history_table.add_widget(Label(text=header))

        # Sample data (replace with your actual data)
        sample_data = [
            ["2023-10-01", "Produk A", "5", "$50"],
            ["2023-09-15", "Produk B", "2", "$30"],
            ["2023-09-05", "Produk C", "3", "$45"]
        ]
        for data in sample_data:
            for value in data:
                history_table.add_widget(Label(text=value))

        self.content_area.add_widget(history_table)

    def show_deposit(self):
        deposit_form = GridLayout(cols=2)
        metode_label = Label(text="Metode Pembayaran:")
        metode_spinner = Spinner(
            text="Pilih Metode",
            values=("BRI", "BCA", "Lainnya")
        )
        jumlah_label = Label(text="Jumlah Deposit:")
        jumlah_input = TextInput(multiline=False)

        deposit_form.add_widget(metode_label)
        deposit_form.add_widget(metode_spinner)
        deposit_form.add_widget(jumlah_label)
        deposit_form.add_widget(jumlah_input)

        deposit_button = Button(text="Deposit")
        deposit_form.add_widget(deposit_button)

        self.content_area.add_widget(deposit_form)

    def show_profile(self):
        profile_layout = GridLayout(cols=2)
        labels = ["Nama:", "Username:", "Email:", "No. HP:", "Saldo:"]
        for label_text in labels:
            label = Label(text=label_text)
            profile_layout.add_widget(label)
            if label_text == "Saldo:":
                saldo_label = Label(text="$1000")
                profile_layout.add_widget(saldo_label)
            else:
                text_input = TextInput(multiline=False)
                profile_layout.add_widget(text_input)

        self.content_area.add_widget(profile_layout)

if __name__ == '__main__':
    NavigationApp().run()
