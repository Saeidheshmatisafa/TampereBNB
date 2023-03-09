from flask import Flask, render_template
import pandas as pd
import random

df = pd.read_csv('data/Tampere_BNB_training_listing.csv')
df["ID"] = df.index
df['Krs'] = df['Krs'].fillna(0)
df['Rv'] = df['Rv'].fillna(0)
df['Kunto'] = df['Kunto'].fillna("unknown")
df['Kunto'] = df['Kunto'].replace(['huono'], 'bad')
df['Kunto'] = df['Kunto'].replace(['hyvä'], 'good')
df['Kunto'] = df['Kunto'].replace(['tyyd.'], 'satisfactory')

df['Asunnon tyyppi'] = df['Asunnon tyyppi'].replace(['Yksiö'], 'Studio apartment')
df['Asunnon tyyppi'] = df['Asunnon tyyppi'].replace(['Kaksi huonetta'], 'Two rooms')
df['Asunnon tyyppi'] = df['Asunnon tyyppi'].replace(['Kolme huonetta'], 'Three rooms')
df['Asunnon tyyppi'] = df['Asunnon tyyppi'].replace(['Neljä huonetta tai enemmän'], 'Four rooms or more')

app = Flask(__name__)

home_adj = ["Beautiful", "Prodigious", "Luxurious", "Dream house", "Lavish", "Alluring", "Damnably huge",	"Commodious",	"Cozy",
            "Furnished", "Timbered",	"Baronial", "Elegant",	"Wooden",	"Sturdy", "Ancestral",	"Marbled", "Gigantic",	"Grand",	"Ancient",
            "Lovely",	"Enchanting", "Heavenly",	"Captivating",	"Beguiling", "Safe", "Roomy", "Spacious",	"Ravishing",	"Tranquil",
            "Aesthetic",	"Ideal",	"Capacious", "Cavernous", "Homely",	"Modern", "Amenities", "Splendid",	"Royal", "Exquisite",
            "Delectable",	"Opulent",	"Sumptuous"]

headings = ("Index","Link")

@app.context_processor
def random_adj():
    home_rand_adj = random.choice(home_adj)
    return {'home_rand_adj': home_rand_adj}

@app.context_processor
def random_num():
    num = random.randint(1, 12)
    return {'num': num}

@app.route('/')
def index():  # put application's code here
    data = list()
    data_link = list()
    for i in df['ID'].iteritems():
        data.append([i[0], 'https://joda-tuni.azurewebsites.net/accom/M20{}23'.format(i[0])])
    return render_template('index.html', headings=headings, data=data)

@app.route('/accom/M20<accom_id>23')
def show_accom_url(accom_id):
    id_ = None
    accom_neighbour = None
    accom_id = int(accom_id)
    price = None
    elevator = None
    if accom_id in df['ID']:
        id_ = df["ID"].loc[accom_id]
        accom_neighbour = df["Kaupunginosa"].loc[accom_id]
        price = df["Hinta"].loc[accom_id]
        floor = df["Krs"].loc[accom_id]
        year = df['Rv'].loc[accom_id]
        condition = df["Kunto"].loc[accom_id]
        ap_type = df['Asunnon tyyppi'].loc[accom_id]
        area = df['m2'].loc[accom_id]
        longitude = df['Pituusaste'].loc[accom_id]
        latitude = df['Leveysaste'].loc[accom_id]

        if "on" in df["Hissi"].values:
            elevator = "does have"
        else:
            elevator = "does not have"

        if floor == 0:
            floor = floor
        else:
            floor = floor.split("/")[0]

    return render_template('accom.html', id_=id_, accom_neighbour=accom_neighbour, accom_id=accom_id, condo_price=price,
                           floor=floor, year=year, condition=condition, ap_type=ap_type, area=area, longitude=longitude, latitude=latitude, elevator=elevator)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0")
