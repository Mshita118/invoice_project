from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from invoice_database import insert_client, fetch_clients, insert_invoice
from tkinter import font

def open_client_form():
    def save_client():
        name = name_entry.get()
        address = address_entry.get()

        if name and address:
            try:
                insert_client(name, address)
                messagebox.showinfo("成功", "クライアントが正常に追加されました")
                form.destroy()
            except Exception as e:
                messagebox.showerror("ERROR", f"データベースエラー: {e}")
        else:
            messagebox.showwarning("検証エラー", "全てのフィールドを入力してください")

    form = tk.Toplevel()
    form.title("取引先の作成")
    form.geometry("300x200")

    tk.Label(form, text="会社名：").grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(form)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(form, text="連絡先：").grid(row=1, column=0, padx=0, pady=0)
    address_entry = tk.Entry(form)
    address_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(form, text="登録", command=save_client).grid(row=2, column=0, columnspan=2, pady=10)


def open_invoice_form():
    def save_invoice():
        selected_client = client_combo.get()
        client_id = client_ids.get(selected_client, None)
        date = date_entry.get()
        try:
            subtotal = float(subtotal_entry.get().replace("$", "").replace(",", "").strip())
            total = float(total_entry.get().replace("$", "").replace(",", "").strip())
        except ValueError:
            messagebox.showerror("入力エラー", "小計や合計には有効な数値を入力してください")
            return

        if client_id and date and subtotal and total:
            try:
                insert_invoice(client_id, date, subtotal, total)
                messagebox.showinfo("成功", "請求情報が正常に登録されました")
                form.destroy()
            except Exception as e:
                messagebox.showerror("エラー", f"データベースエラー： {e}")
        else:
            messagebox.showwarning("入力エラー", "全てのフィールドを入力してください")
    form = tk.Toplevel()
    form.title("請求情報の作成")
    form.geometry("400x300")

    tk.Label(form, text="取引先： ").grid(row=0, column=0, padx=10, pady=10)
    clients = fetch_clients()
    client_ids = {name: id for id, name in clients}
    client_combo = ttk.Combobox(form, values=list(client_ids.keys()), state="readonly")
    client_combo.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(form, text="日付 (YYYY-MM-DD)： ").grid(row=1, column=0, padx=10, pady=10)
    date_entry = tk.Entry(form)
    date_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(form, text="小計： ").grid(row=2, column=0, padx=10, pady=10)
    subtotal_entry = tk.Entry(form)
    subtotal_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(form, text="合計： ").grid(row=3, column=0, padx=10, pady=10)
    total_entry = tk.Entry(form)
    total_entry.grid(row=3, column=1, padx=10, pady=10)

    tk.Button(form, text="登録", command=save_invoice).grid(row=4, column=0, columnspan=2, pady=20)


root = Tk()


custom_font = font.Font(family="Noto Sans CJK JP", size=12)
root.option_add("*Font", custom_font)

root.title("請求書自動化アプリ")
root.geometry("800x400")  # 幅を広げる
root.maxsize(1024, 576)
root.minsize(640, 360)

client_button = tk.Button(root, text="取引先の作成", command=open_client_form)
client_button.pack(pady=20)

invoice_button = tk.Button(root, text="請求情報の作成", command=open_invoice_form)
invoice_button.pack(pady=20)

root.mainloop()
