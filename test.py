nasz_slownik = {'adam': 32, 'marek': 18, 44: 'Kamil', (1, 2): 'wow'}

print(nasz_slownik)
print(nasz_slownik['adam'])
print(nasz_slownik['marek'])
print(nasz_slownik[44])
print(nasz_slownik.get(666, -15))
print(nasz_slownik.get(1, 2), -15)
