from Model.data.db_helper import DBHelper

def calc_bmi(req):

    db = DBHelper()
    data = db.load()
    unit = req["unit"]
    age = req["age"]
    sex = req["sex"]
    weight = req["weight"]
    types = req["func"]
    
    if unit == "US" or unit == "us":
        height_ft = req["height_ft"]
        height_in = req["height_in"]

        height = 12 * height_ft + height_in
        BMI = 703 * (weight / (height * height))
        
    if unit == "SI" or unit == "si":
        height = req["height"]
        height = height / 100

        BMI = (weight / (height * height))
    iters = data["bmi"]
    res = {}
    res["BMI"] = "{0:.2f}".format(BMI)

    if age >= 18:
        iters = iters["adult"]
        for element in iters.keys():
            if(BMI >= iters[element]["start"] and BMI <= iters[element]["end"]):
                res["status"] = element
                break
    else :
        iters = iters["child"]
        for element in iters.keys():
            if(BMI >= iters[element]["start"] and BMI <= iters[element]["end"]):
                res["status"] = element
                break

    return (res, 200)