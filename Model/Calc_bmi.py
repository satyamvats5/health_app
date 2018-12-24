def calc_bmi(req):
    unit = req["unit"]
    age = req["age"]
    sex = req["sex"]
    weight = req["weight"]
    
    if unit == "US" or unit == "us":
        height_ft = req["height_ft"]
        height_in = req["height_in"]

        height = 12 * height_ft + height_in
        BMI = 703 * (weight / (height * height))

        return ("{0:.2f}".format(BMI))
        
    if unit == "SI" or unit == "si":
        height = req["height"]
        height = height / 100

        BMI = (weight / (height * height))

        return ("{0:.2f}".format(BMI))