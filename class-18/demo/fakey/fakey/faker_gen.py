from faker import Faker

fake_en = Faker()

print(fake_en.name())
print(fake_en.first_name())

fake_ar = Faker('ar_PS')
print(fake_ar.name())
print(fake_ar.first_name())


content = ''

for i in range(10):
    temp = ''
    temp += fake_en.paragraph() + "\t"
    temp += fake_en.phone_number() + "\t"
    temp += fake_ar.paragraph() + "\t"
    temp += fake_en.email() + "\t"
    temp += fake_ar.first_name() + "\t"
    temp += fake_en.paragraph()
    temp += '\n'
    content += temp

with open('fake_text.txt', 'w') as f:
    f.write(content)


import shutil
shutil.copy('fake_text.txt', '..')