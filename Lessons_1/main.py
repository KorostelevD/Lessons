def print_hi(name):
    print(f'Привіт, {name}')

def print_t(name):
    print(f'{name}')

print_hi('мій найкращій друг!')
print_t('будь-ласка')

name = input("Вкажи своє ім'я : ")
print_hi(name)

if name == "Дмитро":
    print("Ты молодець!")
else:
    print("Супер!")
