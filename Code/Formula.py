from string import digits, punctuation
some_big_number = 1000000 # temp value to let code run
some_small_number = 10 # temp value to let code run

# TODO: return a specific value for each type of possible error

# NOTE: this can be developed further to integrate with Ignition

def check_proof(proof):
    # if it's not a float or an int
    if type(proof) != float or type(proof) != int:
        # try to convert it
        try:
            proof = float(proof)
        except:
            # if there was an error then the user input some letters
            print("some error message about only using numbers")
            return False
    
    # otherwise it is a float so check the range
    if (proof > 150) or (proof < 50):
        print("some warning message to the user")
        return False
    # otherwise it's in a good range


def calc_RO_water_weight(ABVf):
    # get Wb, pRO, pB, & ABV0 from database
    Wb = 1.0
    pRO = 1.0
    pB = 1.0
    ABV0 = 1.0

    # get ABVf from user's input into HMI and check it
    ABVf_check = check_proof(ABVf)

    # check the initial proof
    ABV0_check = check_proof(ABV0)

    # were we given any bad values    
    if ABVf_check:
        # if so return
        return -1
    elif ABV0_check:
        # if so return
        return -1

    # if the weight of the bourbon is weird
    if Wb > some_big_number or Wb < some_small_number:
        print("some warning message to the user")
        return -1

    # if the density of the RO water is werid
    if pRO > some_big_number or pRO < some_small_number:
        print("some warning message to the user")
        return -1

    # if the density of the bourbon is weird
    if pB > some_big_number or pB < some_small_number:
        print("some warning message to the user")
        return -1

    # calc weight
    weight = Wb * (pRO/pB) * ((ABV0/ABVf) - 1)

    # sanity check weight value
    if weight > some_big_number:
        print("some warning message to the user")
        return -1

    # return the value
    return weight