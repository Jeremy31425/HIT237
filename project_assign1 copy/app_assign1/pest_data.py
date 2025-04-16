# app_assign1/pest_data.py

class Pest:
    def __init__(self, id, name, short_desc, full_desc, image_url):
        self.id = id
        self.name = name
        self.short_desc = short_desc
        self.full_desc = full_desc
        self.image_url = image_url

# 7 sample pests/diseases
pests = [
    Pest("fruitfly", "Fruit Fly", "Causes mango rotting.",
         "Fruit flies lay eggs under mango skin, introducing bacteria that cause the fruit to rot.",
         "images/fruitfly.jpg"),
    Pest("leafhopper", "Mango Leafhopper", "Sucks sap from mango leaves.",
         "Suck sap from young leaves and flowers, leading to withering and poor fruiting.",
         "images/leafhopper.jpg"),
    Pest("seedweevil", "Mango Seed Weevil", "Larvae tunnel into mango seeds.",
         "Feed inside the seed, causing internal damage with few external symptoms.",
         "images/seedweevil.jpg"),
    Pest("stemborer", "Mango Stem Borer", "Bores into tree trunks and branches.",
         "Larvae create tunnels in wood, leading to dieback and death of branches.",
         "images/stemborer.jpg"),
    Pest("leafwebber", "Mango Leaf Webber", "Webs and eats mango leaves.",
         "Creates webbed shelters in leaves, leading to defoliation and reduced fruit set.",
         "images/leafwebber.jpg"),
    Pest("gallmidge", "Mango Gall Midge", "Causes galls in leaves and flowers.",
         "Larvae form galls in inflorescences, reducing flowering and fruiting.",
         "images/gallmidge.jpg"),
    Pest("shootborer", "Mango Shoot Borer", "Affects new shoots and branches.",
         "Larvae bore into shoots, causing wilting and shoot death.",
         "images/shootborer.jpg"),
]
