import sys
import string
import random
random.seed(42)

def generate_coupons():
    coupon_codes = {}
    for char in string.ascii_lowercase:
        coupon_codes[char] = {}
        for idx in range(7):
            coupon_codes[char][idx] = random.randint(0,50)
    return coupon_codes

if __name__ == "__main__":
    c = generate_coupons()
    if len(sys.argv) < 3:
        print("Insufficient arguements provided")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Excess arguements provided!")
        sys.exit()
    else:
        days_dict = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
        coupon_code = sys.argv[1]
        if coupon_code not in c.keys():
            print("Invalid coupon")
            sys.exit()
        day = sys.argv[2].strip().lower()
        if day in days_dict.keys():
            day = days_dict[day]
        else:
            day = int(day)
        
        print("Discount offered: " + str(c[coupon_code][day]))

