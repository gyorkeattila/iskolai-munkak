from _typeshed import OpenTextModeWriting
import datetime

ev = datetime.datetime.now().year

print('Köszöntelek az első programomban')

vezeteknev = input ("Mi a vezetékneved?")
keresztnev = input ("Mi a keresztneved?")


print("Szia "+keresztnev+"") 
kor = input ("Mikor születtél?")

print (+vezeteknev+" "+keresztnev+"") 
#print(keresztnev+" melyik évben születtél?" ,end="")
#ev=input()

szulvev = input(keresztnev+ "melyik évben születtél?")
print (vezeteknev, keresztnev," te most")
(ev-szulvev)," éves vagy"

print(vezeteknev, keresztnev, " te most",
kor," éves vagy")

print(5 - kor % 5, "év múlva leszel", kor + 5-kor %5)

mulva= 5 - kor % 5

print(mulva, "év múlva leszel" , kor + mulva)

print(kor // 5* 5 + 5)

