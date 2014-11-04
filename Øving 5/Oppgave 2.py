__author__ = 'Morten Stulen'
import sys

antall_kvinner = 0
antall_menn = 0
antall_sosmedier = 0
antall_facebook = 0
antall_timer_sosmedier = 0



undersøkelse = True
text = open("text_antall", "w")


def validate(user_input):
    if str(user_input) == "hade":
        print()
        print("Antall kvinner: \t %s \nAntall menn: \t\t %s \nAntall Sosmedier: \t %s \nAntall Facebook: \t %s \nAntall Timer: \t\t %s" % (antall_kvinner, antall_menn, antall_sosmedier, antall_facebook, antall_timer_sosmedier/(antall_menn + antall_kvinner)))
        text.close()
        sys.exit("Du avsluttet. Takk for at du svarte på under søkelsen. Hade!")


def getInput(input_string):
    user_input = input(input_string)
    validate(user_input)
    return user_input

def get_alder():
    try:
        alder = int(getInput("Skriv inn alder: "))
        if (alder >= 16 and alder <= 25):
            sosiale_medier()
        else:
            print("Du er utenfor aldersgruppen")
    except ValueError:
        print("Skriv inn et tall...")


def sosiale_medier():
    aktiv_sosmedier = False
    sosiale_medier_boolean = getInput("Bruker du et eller flere sosiale medier? Svar ja/nei ")
    if (sosiale_medier_boolean == "Ja" or sosiale_medier_boolean == "ja"):
        aktiv_sosmedier = True
    if aktiv_sosmedier == True:
        global antall_sosmedier
        antall_sosmedier += 1
        text.write("Antall Sosmedier: \t%s\n" % (antall_sosmedier))
        facebook()
    elif (sosiale_medier_boolean == "Nei" or sosiale_medier_boolean == "nei"):
        print("Takk for at du svarte! Du trenger ikke å svare på de neste spørsmålene. \n")
    else:
        print("Skriv inn ja eller nei...")
        sosiale_medier()




def facebook():
    global antall_facebook
    medlem_facebook = ""
    if (kjønn == "k" or kjønn == "K"):
        medlem_facebook = getInput("Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse? Svar ja/nei ")

    elif (kjønn == "m" or kjønn == "M"):
        medlem_facebook = getInput("Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse? ")

    if (medlem_facebook == "Ja" or medlem_facebook == "ja"):
        antall_facebook += 1
        text.write("Antall Facebook: \t%s\n" % (antall_facebook))
        antall_timer()
    elif (medlem_facebook == "Nei" or medlem_facebook == "nei"):
        antall_timer()
    else:
        print("Skriv ja eller nei...")
        facebook()


def antall_timer():
    timer_sosmedier = int(getInput("Hvor mange timer bruker du i snitt daglig på sosiale medier? "))
    if (timer_sosmedier > 0 and timer_sosmedier < 24):
        global antall_timer_sosmedier
        antall_timer_sosmedier += timer_sosmedier
        text.write("Antall Timer: \t\t%s\n" % (antall_timer_sosmedier/(antall_kvinner+antall_menn)))
        print("Takk for at du var med i undersøkelsen!")
    else:
        print("Skriv et realistisk tall...")
        antall_timer()


while undersøkelse:
    kjønn = getInput("Skriv inn kjønn m/k: ")
    if (kjønn == "m" or kjønn == "M"):
        antall_menn += 1
        text.write("Antall menn: \t\t%s\n" % (antall_menn))
        get_alder()
    elif (kjønn == "k" or kjønn == "K"):
        antall_kvinner += 1
        text.write("Antall kvinner: \t%s\n" % (antall_kvinner))
        get_alder()
    else:
        print("Skriv inn M eller K!")


