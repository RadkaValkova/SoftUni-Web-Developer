n = int(input())
m = float(input())
kurs = float(input())

mes_zapl = n*m
bonus = mes_zapl*2.5
god_prih = 12*mes_zapl+bonus
god_dan = god_prih*25/100
prihod_USD = god_prih-god_dan
prhod_lv = prihod_USD*kurs
prihod_lv_den = prhod_lv/365

print('%.2f'% prihod_lv_den)